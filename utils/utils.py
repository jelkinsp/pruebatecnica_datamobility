import glob
import json

import dash_html_components as html
import pandas as pd


def get_dataframe():
    file = glob.glob("data/dataset_motos.geojson")
    with open(file[0]) as json_data:
        geojson_read = json.load(json_data)
    properties_list = [value["properties"] for value in geojson_read["features"]]
    df_properties = pd.DataFrame(properties_list)
    return df_properties, geojson_read


def generate_table(df):
    index = df.index
    motorcycle_available = df["count"].sum()
    time_stopped = df["time_stopped"].max()
    index_polygon = index[df["time_stopped"] == time_stopped]
    polygon_id = df.loc[index_polygon, "polygon"]
    time_stopped_mean = df["time_stopped"].mean()

    style_table_thead = {
        "padding": ".25em .5em",
        "background-color": "#56A8D1",
        "color": "white",
    }
    style_table_tbody = {
        "padding": ".25em .5em",
        "background-color": "#abcad7",
        "border-color": "black"
    }
    style_table = {
        "width": "100%",
        "background-color": "#56A8D1",
        "border-color": "black",
    }

    return html.Table([
        html.Thead(
            html.Tr([html.Th("Data:"), html.Th("Valor:")])
            , style=style_table_thead),
        html.Tbody([
            html.Tr([html.Td("Cantidad total de motos disponibles:"),
                     html.Td(motorcycle_available)]),
            html.Tr(
                [html.Td("Máximo tiempo parada de un grid:"),
                 html.Td(time_stopped)], style={
                    "background-color": "white",
                }),
            html.Tr([html.Td("Grid id con Máximo tiempo de parada (campo polygon):"),
                     html.Td(polygon_id)]),
            html.Tr([html.Td("Media total de tiempo de parada de todos los grids:"),
                     html.Td(time_stopped_mean)], style={
                "background-color": "white",
            }),
        ], style=style_table_tbody)
    ], style=style_table)
