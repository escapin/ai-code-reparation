import dash
import random

from frontend import frontend
from callbacks import callback1

# initialize app
app = dash.Dash()

# load the frontend
frontend(app)

# load the callbacks
callback1(app)


if __name__ == "__main__":
    app.run_server()
