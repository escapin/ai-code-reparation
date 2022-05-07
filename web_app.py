import dash
import random
import dash_bootstrap_components as dbc

from frontend import frontend
from callbacks import callback1, callback2, callback3

external_stylesheets = [dbc.themes.BOOTSTRAP]

# initialize app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# load the frontend
frontend(app)

# load the callbacks
callback1(app)
callback2(app)
callback3(app)


if __name__ == "__main__":
    app.run_server()
