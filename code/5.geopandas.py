#pip install geopandas

import geopandas as gpd

url = 'https://raw.githubusercontent.com/jcanalesluna/bcn-geodata/master/districtes/districtes.geojson'

districts = gpd.read_file(url)

districts
#print(districts)

print(districts.crs)

districts['area'] = districts.area / 1000000

districts

## Visualisation
ax= districts.plot(figsize=(10,6))

