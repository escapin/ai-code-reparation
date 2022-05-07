from logging import PlaceHolder
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
                        children="AI-Powered Code Reparation",
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
                            dbc.Col(
                                [
                                    html.H2("Original Code"),
                                    dcc.Textarea(
                                        id="input",
                                        placeholder="Enter your code here...",
                                        style={"width": "100%", "height": "300px"},
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
                                    )
                                ]
                            ),
                            dbc.Col(
                                [
                                    html.H2("Fixed Code"),
                                    dcc.Textarea(
                                        id="fixed-code",
                                        placeholder="Your fixed code here...",
                                        style={"width": "100%", "height": "300px"},
                                    ),
                                    html.Button(
                                        id="apply-button",
                                        n_clicks=0,
                                        children="🠔 Use as Original Code",
                                        style={
                                            "background-color": "lightgreen",
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
                                    )
                                ]
                            ),
                        ],
                    ),
                    html.Div(id="output-container"),
                ],
                className="row",
                style={"margin": "30px"},
            ),
        ]
    )
