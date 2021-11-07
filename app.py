import dash
import dash_core_components as dcc
import dash_html_components as html

from display.graphs import display_choropleth, display_historygram
from utils.utils import get_dataframe, generate_table
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df, geojson = get_dataframe()


@app.callback(
    Output('click_result', 'children'),
    [Input('choropleth_graph', 'clickData')])
def display_click_data(custom_data):
    if custom_data is not None:
        polygon_id = custom_data['points'][0]['location']
        df_result = df.loc[df['polygon'] == polygon_id]
        return [
            html.P("perc: {}".format(df_result['perc'].tolist()[0])),
            html.P("time_stopped: {}".format(df_result['time_stopped'].tolist()[0])),
            html.P("vehicle_id: {}".format(df_result['vehicle_id'].tolist()[0]))
        ]
    return [
        html.P("perc: {}".format("")),
        html.P("time_stopped: {}".format("")),
        html.P("vehicle_id: {}".format(""))
    ]

app.layout = html.Div([
    html.H2("Data Mobility:"),
    dcc.Graph(
        id='choropleth_graph',
        figure=display_choropleth(df, geojson)
    ),
    html.Div(id="click_result"),
    generate_table(df),
    dcc.Graph(
        id='histogram-mobility',
        figure=display_historygram(df)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
