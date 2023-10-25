# Código Folium

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

import geopandas as gpd
import json
import geojson
import requests

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut

import folium
import osmnx as ox
from shapely import wkt
from folium.plugins import HeatMap
from shapely.geometry import Polygon

def get_reportes_resumen():

    conn = mysql.connector.connect(
        host="10.100.1.68",
        user="powerbi",
        password="Desarr0ll02022",
        database="nueveonce"
    )

    cursor = conn.cursor()

    query = "SELECT * FROM reportes_resumen"
    cursor.execute(query)
    reportes_resumen = cursor.fetchall()

    reportes_resumen = pd.DataFrame(reportes_resumen, columns = ['cod', 'id', 'longitud', 'latitud', 'creator_type', 'id_alert',
       'name_alert', 'id_report_status', 'name_status', 'id_agente', 'name',
       'last_name', 'oni', 'telefono', 'id_rol', 'title', 'id_sector',
       'nombre_sector', 'id_delegacion', 'nombre_delegacion', 'created_at',
       'updated_at', 'fecha', 'hoy', 'tipo', 'minutos', 'descripcion'])

    return reportes_resumen

reportes = get_reportes_resumen()
reportes = reportes[reportes["id_alert"]!=0]

reportes["latitud"] = reportes["latitud"].astype(float)
reportes["longitud"] = reportes["longitud"].astype(float)

df = reportes[reportes["nombre_delegacion"]=="DELEGACION SAN SALVADOR SUR"]

mapa = folium.Map(location=[df['latitud'].mean(),df['longitud'].mean()],zoom_start=15)

for index, row in df.iterrows():
        tooltip = f"Timestamp:{row['created_at']}"
        folium.CircleMarker(location=[row['latitud'], row['longitud']], radius=2, color= 'blue', fill=True, fill_color='blue', tooltip=tooltip).add_to(mapa)

mapa