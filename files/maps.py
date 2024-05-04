import streamlit as st
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import pydeck as pdk

global loc_file
    
    
@st.cache_data
def load_data(main_file):
    my_world_map = gpd.read_file('ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
    #my_world_map['geometry'] = my_world_map['geometry'].apply(str)
    main_file['Country'] = main_file['Country'].replace('England', 'United Kingdom')

    #st.dataframe(my_world_map)
    #st.write(my_world_map)
    gdf = my_world_map.merge(main_file, left_on='NAME_LONG', right_on='Country', how='inner')
    #st.write(loc_file)
    #st.write(gdf)
    return gdf

def create_map(gdf,league_chosen):
    country_data = gdf[gdf['League'] == league_chosen]
    center = country_data.geometry.centroid.iloc[0]  
    center_lat = center.y
    center_lon = center.x
    m = folium.Map(location=[center_lat, center_lon], zoom_start=3,width=400,height=400)
    geojson_data = gdf.to_json()
    folium.GeoJson(
        geojson_data,
        style_function=lambda feature: {
            'fillColor': 'red',
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.7
        },
        tooltip=folium.GeoJsonTooltip(
            fields=['NAME_LONG', 'League'],  
            aliases=['Country', 'League'],  
            localize=True
        )
    ).add_to(m)

    return m

def mapsViz(main_file,league):
    gdf = load_data(main_file)
    m = create_map(gdf,league)
    folium_static(m)
    #st.write(gdf)

    
    

    
    




# Display plot in Streamlit
