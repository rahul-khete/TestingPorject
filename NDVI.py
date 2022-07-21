

class NDVI_Index:
	def __init__(self,b4,b8,path,meta):
		self.red = b4.read()
		self.nir = b8.read()
		self.path=path
		self.meta=meta


	def ndviValue():
    		ndvi = (self.nir.astype(float)-self.red.astype(float))/(self.nir+self.red)
    		with rio.open(self.path+'NDVI.tif', 'w', self.**meta) as dst:
        		dst.write(ndvi.astype(rio.float32))

    		ndvi = rxr.open_rasterio(self.path+"NDVI.tif",masked=True).squeeze()
    		shp = os.path.join('shapeFile')
   		crop_extent = geopandas.read_file(shp)
    		ndvi_clipped = ndvi.rio.clip(crop_extent.geometry.apply(mapping),crop_extent.crs)
    		f, ax = plt.subplots(figsize=(10, 4))
    		ndvi_clipped.plot(ax=ax)
    		ax.set(title="Raster Layer Cropped to Geodataframe Extent")
    		ax.set_axis_off()
    		plt.show()
    		pd.DataFrame(ndvi_clipped.values).head()
    		ndvi_value=ndvi_clipped.mean()
    		return ndvi_value