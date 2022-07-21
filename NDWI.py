

class NDWI_Index:
	def __init__(self,b3,b8,path,meta):
		self.green = b3.read()
		self.nir = b8.read()
		self.path=path
		self.meta=meta


	def ndwiValue():
    		ndwi = (self.nir.astype(float)-self.green.astype(float))/(self.nir+self.green)
    		with rio.open(self.path+'NDWI.tif', 'w', self.**meta) as dst:
        		dst.write(ndwi.astype(rio.float32))

    		ndwi = rxr.open_rasterio(self.path+"NDWI.tif",masked=True).squeeze()
    		shp = os.path.join('shapeFile')
   		crop_extent = geopandas.read_file(shp)
    		ndwi_clipped = ndwi.rio.clip(crop_extent.geometry.apply(mapping),crop_extent.crs)
    		f, ax = plt.subplots(figsize=(10, 4))
    		ndwi_clipped.plot(ax=ax)
    		ax.set(title="Raster Layer Cropped to Geodataframe Extent")
    		ax.set_axis_off()
    		plt.show()
    		pd.DataFrame(ndwi_clipped.values).head()
    		ndwi_value=ndwi_clipped.mean()
    		return ndwi_value