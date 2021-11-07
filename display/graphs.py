import pandas as pd
import plotly.express as px


def display_choropleth(df, geojson):
    fig = px.choropleth_mapbox(
        df, geojson=geojson, color='count',
        locations="polygon", featureidkey="properties.polygon",
        range_color=[0, 20], mapbox_style="open-street-map", center={"lat": 40.4667, "lon": -3.70325}, zoom=10)
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


#
# def display_historygram(df):
#     df_different_count = pd.DataFrame(df["count"].unique(), columns=["count"])
#     df_clear = df[["polygon", "count"]]
#     df_different_count["grids"] = None
#     for index, count in df_different_count.iterrows():
#         df_mask = df_clear["count"] == count.values[0]
#         df_different_count.loc[index, "grids"] = len(df_clear[df_mask])
#     return px.bar(df_different_count, y="count", x="grids")
