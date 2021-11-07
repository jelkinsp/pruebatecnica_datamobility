import glob
import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Data Mobility:"),
])

if __name__ == '__main__':
    app.run_server(debug=True)
