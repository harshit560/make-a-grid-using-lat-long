#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd 

lat, lon = 20.5937, 78.9629  # put desired lat long

#put desired coordinate system
df = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lon],[lat]), crs="epsg:4326").to_crs(32644)  

#defining size of grid
df.geometry = df.geometry.buffer(2500).envelope 

#saving the grid in geojson
df.to_crs("epsg:4326").to_file(r"C:\\Users\\Harshit\\Desktop\\grid.geojson")


# In[ ]:




