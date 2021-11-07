import dash
import dash_core_components as dcc
import dash_html_components as html

from display.graphs import display_choropleth
from utils.utils import get_dataframe

app = dash.Dash(__name__)

df, geojson = get_dataframe()


app.layout = html.Div([
    html.H2("Data Mobility:"),
    dcc.Graph(
        id='choropleth_graph',
        figure=display_choropleth(df, geojson)
    ),
    # html.Div(id="click_result"),
    # generate_table(df),
    # dcc.Graph(
    #     id='histogram-mobility',
    #     figure=display_historygram(df)
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True)
