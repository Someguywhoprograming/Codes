import geopandas as gpd
import plotly.express as px

# Betöltjük az ország adatokat
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Plotly-hoz kell külön oszlop az ország nevekből
world["name"] = world["name"]

fig = px.choropleth(
    world,
    geojson=world.geometry,
    locations=world.index,
    color=world.index,
    hover_name="name"
)

# 3D gömb nézet
fig.update_geos(
    projection_type="orthographic",  # ez adja a gömb hatást
    showland=True,
    showcountries=True,
)

fig.update_layout(
    title="Forgatható Földgömb - Összes Ország",
    height=800
)

fig.show()