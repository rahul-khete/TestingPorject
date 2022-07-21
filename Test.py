from sentinelDataBands import sentinelData
from NDVI import NDVI_Index
from NDWI import NDWI_Index
from EVI import EVI_Index
'''
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon
import folium



class test:
	def __init__(self,coords, polygon_name):
		self.coords=coords
		self.polygon_name=polygon_name

	def create_polygon(self):
  		polygon = Polygon(self.coords)
  		gdf = gpd.GeoDataFrame(crs = 'epsg:4326')
  		gdf.loc[0,'name'] = self.polygon_name
  		gdf.loc[0, 'geometry'] = polygon
  		return gdf

	def getPath(self,b2):
		name=b2.split('_')[2][4:8]
		name=name[2:]+name[:2]
		if not os.path.exists('TIF_'+name):
    			os.mkdir('TIF_'+name)
		path='TIF_'+name+'/'
		return path

	def getMeta(self,b4):
		meta = b4.meta
		meta.update(driver='GTiff')
		meta.update(dtype=rio.float32)
		return meta


test1=test(coordinates, 'Farm_Name') #coordinates = [(74.882083,17.057028), (74.882472,17.056917), (74.882444,17.056722), (74.882028,17.056833),(74.882083,17.057028)]
shapefile =test1.create_polygon()
shapefile.to_file("Farm_Name.shp")

sentinelDataObj=sentinelData('shapePath')
b2,b3,b4,b5,b8,b11=sentinelDataObj.getBands()


path=test1.getPath(b2)
meta=test1.getMeta(b4)

ndvi=NDVI_Index(b4,b8,path,meta)
ndwi=NDWI_Index(b3,b8,path,meta)
evi=EVI_Index(b2,b4,b8,path,meta)
'''