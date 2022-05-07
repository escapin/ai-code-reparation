import dash
import dash_core_components as dcc
import dash_html_components as html
import random

from sentiment_analysis_gpt3 import sentiment_anaysis_check

app = dash.Dash()

colors = {
    "background": "#111111",
    "text": "#7FDBFF",
    "sentiment": {
        "positive": "#00ff00",
        "neutral": "#ffff00",
        "negative": "#ff0000",
    },
}

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    children="Customer Review PoC",
                    style={
                        "text-align": "center",
                        "font-family": "helvetica",
                        "background-color": colors["background"],
                        "color": colors["text"],
                        "padding": "10px 20px",
                        "margin-top": "0px",
                    },
                )
            ],
            className="row",
        ),
        html.Div(
            [
                dcc.Input(
                    id="input",
                    type="text",
                    placeholder="Enter customer review here...",
                    style={"width": "100%", "height": "300px"},
                ),
                html.Button(
                    id="submit-button",
                    n_clicks=0,
                    children="Submit Review",
                    style={
                        "background-color": "lightblue",
                        "border": "none",
                        "color": "black",
                        "padding": "15px 32px",
                        "text-align": "center",
                        "text-decoration": "none",
                        "display": "inline-block",
                        "font-size": "16px",
                        "margin": "4px 2px",
                        "cursor": "pointer",
                    },
                ),
            ],
            className="row",
            style={"margin": "30px"},
        ),
        html.Div(id="output-container", children=[], style={"margin": "30px"}),
    ]
)


@app.callback(
    dash.dependencies.Output("output-container", "children"),
    [
        dash.dependencies.Input("submit-button", "n_clicks"),
        dash.dependencies.State("input", "value"),
    ],
)
def update_output(n_clicks, customer_review):
    if n_clicks > 0:
        sentiment, sentiment_colour = sentiment_anaysis_check(customer_review)
        return html.Div(
            [
                html.H1(f"The Feedback is {sentiment}"),
                html.Div(
                    style={
                        "background-color": sentiment_colour,
                        "width": "100%",
                        "height": "300px",
                    }
                ),
            ]
        )


if __name__ == "__main__":
    app.run_server()
