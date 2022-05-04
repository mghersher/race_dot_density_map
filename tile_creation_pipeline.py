import os

#Convert from shp to geojson
city = 'dc'
races = ['hispanic', 'nh_white', 'nh_black', 'nh_asian_pacific', 'nh_native', 'nh_other', 'nh_multiple']
for race in races:
    os.system(f'ogr2ogr -f GeoJSON data/processed_data/{city}_one_point_one_person_2020_{race}.geojson data/processed_data/{city}_one_point_one_person_2020_{race}.shp -progress')
    
#Generate Mapbox vector tile directory
tippecanoe_command = f'tippecanoe -f -e data/processed_data/{city}point -L white:data/processed_data/{city}_one_point_one_person_2020_nh_white.geojson -L black:data/processed_data/{city}_one_point_one_person_2020_nh_black.geojson -L hispanic:data/processed_data/{city}_one_point_one_person_2020_hispanic.geojson -L asian_pacific:data/processed_data/{city}_one_point_one_person_2020_nh_asian_pacific.geojson -L multiple:data/processed_data/{city}_one_point_one_person_2020_nh_multiple.geojson -L native:data/processed_data/{city}_one_point_one_person_2020_nh_native.geojson -L other:data/processed_data/{city}_one_point_one_person_2020_nh_other.geojson -L blocks:data/processed_data/{city}_blocks.geojson --minimum-zoom=10 --maximum-zoom=14'
os.system(tippecanoe_command)

#Move tile.json out of {city}point directory
os.system(f'mv data/processed_data/{city}point/tile.json tile.json')

#Upload vector tile directory
os.system(f"aws s3 cp data/processed_data/{city}point s3://tiles.mappingtiles.com/{city}point/ --recursive --content-type application/x-protobuf --content-encoding 'gzip'")

#Move the tile.json file back
os.system(f'mv tile.json data/processed_data/{city}point/tile.json')

#Upload the tile.json file
os.system(f"aws s3 cp data/processed_data/{city}point/tile.json s3://tiles.mappingtiles.com/{city}point/tile.json")

