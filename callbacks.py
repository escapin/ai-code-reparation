import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import openai

import re


# load OpenAI API Key
with open("./api_key.txt") as f:
    api_key = f.read()
openai.api_key = api_key


def find_bugs(code):
    if code == None:
        return "Please, specify some code"

    prompt = "##### Point bugs in the below function\n" + code + "\n##### Bugs:"

    print(prompt)

    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1,
        stop=["####"],
    )

    find_bugs_result = response["choices"][0]["text"]

    return find_bugs_result


def fix_code(code, bug):
    command = "Fix the following bug: " + bug

    response = openai.Edit.create(
        engine="code-davinci-edit-001",
        input=code,
        instruction="Fix the following bug: Cursor should be closed after use, but it isn't here",
        temperature=0,
        top_p=1,
    )

    fixed_code = response["choices"][0]["text"]

    return fixed_code


def filter_bug_text(line):
    return next((item for item in re.findall("#?\s?\d\.\s?(.+)", line)), None)


def callback1(app):
    """
    Summary: This function is the callback to find bugs in the users input text.

    Args:
        app (_type_): the WebApp Object

    Returns:
        _type_: Updates the 'bug-link' component
    """

    @app.callback(
        dash.dependencies.Output("output-container", "children"),
        [
            dash.dependencies.Input("submit-button", "n_clicks"),
            dash.dependencies.State("input", "value"),
        ],
    )
    def update_output(n_clicks, code):
        bug_results = find_bugs(code)
        bugs = bug_results.strip().split("\n")

        bug_items = map(lambda bug: filter_bug_text(bug), bugs)

        # TODO: add fixing on click or the error and write on output textblock
        # bug_item = next(
        #    (bug_item.strip() for bug_item in bug_items if bug_item), None
        # )
        #
        # if bug_item:
        #    fixed_code = fix_code(code, bug_item)

        # end TODO

        # Checklist

        checklist = html.Div(
            dbc.Checklist(
                id="bugs",
                options=[
                    {"label": bug_item, "value": bug_item}
                    for bug_item in bug_items
                    if bug_item
                ],
                inline=False,
                style={"margin": "30px"},
            )
        )

        return checklist


def callback2(app):
    """
    Summary: This function is the callback to apply the suggested bug fixes to the code (user input field).

    Args:
        app (_type_): the WebApp Object

    Returns:
        _type_: Updates the 'input' component
    """

    @app.callback(
        dash.dependencies.Output("input", "value"),
        [
            dash.dependencies.Input("apply-button", "n_clicks"),
            dash.dependencies.State("fixed-code", "value"),
        ],
    )
    def apply_code_suggestion(apply_button, fixed_code):
        return fixed_code

    return
