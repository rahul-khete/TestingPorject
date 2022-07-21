

class EVI_Index:
	def __init__(self,b2,b4,b8,path,meta):
		self.blue=b2.read()
		self.red = b4.read()
		self.nir = b8.read()
		self.path=path
		self.meta=meta


	def ndviValue():
    		evi = (2.5*(self.nir.astype(float)-self.red.astype(float))/(self.nir+(6*self.red)-(7.5*self.blue)+1))
    		with rio.open(self.path+'EVI.tif', 'w', self.**meta) as dst:
        		dst.write(evi.astype(rio.float32))

    		evi = rxr.open_rasterio(self.path+"EVI.tif",masked=True).squeeze()
    		shp = os.path.join('shapeFile')
   		crop_extent = geopandas.read_file(shp)
    		evi_clipped = evi.rio.clip(crop_extent.geometry.apply(mapping),crop_extent.crs)
    		f, ax = plt.subplots(figsize=(10, 4))
    		evi_clipped.plot(ax=ax)
    		ax.set(title="Raster Layer Cropped to Geodataframe Extent")
    		ax.set_axis_off()
    		plt.show()
    		pd.DataFrame(evi_clipped.values).head()
    		evi_value=evi_clipped.mean()
    		return evi_value