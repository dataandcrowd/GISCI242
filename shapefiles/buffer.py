layerName = 'NZL_rails_27200'
outFn = '/Users/hshi103/Downloads/buffered.shp'
bufferDist = 500

# Retrieve the specific layer
layers = QgsProject.instance().mapLayersByName(layerName)
if not layers:
    print("Layer not found!")
    exit()

layer = layers[0]

# Initialize the writer with correct parameters, this should be done after buffer calculation
fields = layer.fields()
writer = QgsVectorFileWriter(outFn, 'UTF-8', fields, QgsWkbTypes.Polygon, layer.sourceCrs(), 'ESRI Shapefile')

# Buffer operation and feature writing
for feat in layer.getFeatures():
    geom = feat.geometry()
    buff = geom.buffer(bufferDist, 5)  # Adjust segment count if needed for smoother curves
    feat.setGeometry(buff)
    writer.addFeature(feat)

# Clean up and load the layer
del(writer)  # Ensure to close the writer to flush features to disk
iface.addVectorLayer(outFn, '', 'ogr')
