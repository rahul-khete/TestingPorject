import geopandas
from sentinelsat import SentinelAPI
import numpy as np
import pandas as pd
import geopandas as gpd
import folium
from shapely.geometry import MultiPolygon, Polygon,mapping
import rasterio as rio
from rasterio.enums import Resampling
from rasterio import plot
from rasterio.plot import show
from zipfile import ZipFile
import matplotlib.pyplot as plt
from osgeo import gdal,osr
import os
import math
import fiona
from branca.element import Figure

import rioxarray as rxr
import xarray as xr
import earthpy as et
import earthpy.plot as ep

import glob
import zipfile
import shutil
import warnings
warnings.filterwarnings("ignore")


class sentinelData:

	def __init__(self,shapePath):
		nReserve = geopandas.read_file('/content/drive/MyDrive/PalmTreeSite.shp')#shape file path
		m2 = folium.Map([16.6231763,73.9119105], zoom_start=12)
		folium.GeoJson(nReserve).add_to(m2)

		footprint =None
		for i in nReserve['geometry']:
				footprint = i
		user = 'khet_e07042022' 
		password = 'Khet_E@2022' 
		api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

		products = api.query(footprint,
						date = ('20220601', '20220630'),
						platformname = 'Sentinel-2',
						processinglevel = 'Level-2A',
						cloudcoverpercentage = (0,100))

		products_gdf = api.to_geodataframe(products)
		api.download(products_gdf['uuid'][0])

		file=glob.glob("*.zip")
		with zipfile.ZipFile(file[0], 'r') as zip_ref:
				zip_ref.extractall()
		os.remove(file[0])

		bands=[]
		for root, dirs, files in os.walk("."):
			for f in files:
				s=os.path.relpath(os.path.join(root, f), ".")
				if s.find('R10m')!=-1 or s.find('R20m')!=-1:
					if s.find('B02')!=-1 and s.find('R10m')!=-1:
						bands.append(s)
					if s.find('B03')!=-1 and s.find('R10m')!=-1:
						bands.append(s)
					if s.find('B04')!=-1 and s.find('R10m')!=-1:
						bands.append(s)
					if s.find('B08')!=-1 and s.find('R10m')!=-1:
						bands.append(s)
					if s.find('B05')!=-1 and s.find('R20m')!=-1:
						bands.append(s)
					if s.find('B11')!=-1 and s.find('R20m')!=-1:
						bands.append(s)

		b2 = rio.open(bands[0])
		b3 = rio.open(bands[1])
		b4 = rio.open(bands[2])
		b8 = rio.open(bands[3])
		b5 = rio.open(bands[4])
		b11 = rio.open(bands[5])

	def getBands(self):
		return (self.b2,self.b3,self.b4,self.b5,self.b8,self.b11)