import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def frontend(app):
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
                        children="AI-enhanced Code Reparation and Performances",
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
                    dbc.Row(
                        [
                            dbc.Col(dcc.Textarea(
                                id="input",
                                placeholder="Enter your code here...",
                                style={"width": "100%", "height": "300px"},
                            )),
                            dbc.Col(dcc.Textarea(
                                id="fixed-code",
                                placeholder="Your fixed code here...",
                                style={"width": "100%", "height": "300px"},
                            ))
                        ],
                    ),
                    html.Button(
                        id="submit-button",
                        n_clicks=0,
                        children="Check code",
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
