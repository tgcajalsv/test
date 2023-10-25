import numpy as np
import pandas as pd
import geojson 
import geopandas as gpd
import matplotlib.pyplot as plt 

capa_test = gdp.read_file("https://github.com/tgcajalsv/test/blob/main/SUR%20SAN%20SALVADOR%20(DISTRITO).geojson")

capa_test.plot()
plt.show()