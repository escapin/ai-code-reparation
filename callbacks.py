import dash
import dash_core_components as dcc
import dash_html_components as html

import openai


# load OpenAI API Key
with open("./api_key.txt") as f:
    api_key = f.read()
openai.api_key = api_key


def find_bugs(code):
    if code == None:
        return "Please, specify some code"

    prompt = "##### Point bugs in the below function\n" + code + "\n##### Bugs:"

    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1,
        stop=["####"]
    )

    find_bugs_result = response["choices"][0]["text"]

    return find_bugs_result


def callback1(app):
    @app.callback(
        dash.dependencies.Output("output-container", "children"),
        [
            dash.dependencies.Input("submit-button", "n_clicks"),
            dash.dependencies.State("input", "value"),
        ],
    )
    def update_output(n_clicks, code):
        if n_clicks > 0:
            bug_results = find_bugs(code)
            bugs = bug_results.strip().split("\n")
            return html.Div(
                html.Ul(children=[html.Li(bug) for bug in bugs])
            )
