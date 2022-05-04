import os

#Convert from shp to geojson
races = ['hispanic', 'nh_white', 'nh_black', 'nh_asian_pacific', 'nh_native', 'nh_other', 'nh_multiple']
for race in races:
    os.system(f'ogr2ogr -f GeoJSON data/processed_data/dc_one_point_one_person_2020_{race}.geojson data/processed_data/dc_one_point_one_person_2020_{race}.shp -progress')
    
#Generate Mapbox vector tile directory
# tippecanoe_command = 'tippecanoe -f -e dcpoint -L white:data/processed_data/dc_one_point_one_person_2020_nh_white.geojson -L black:data/processed_data/dc_one_point_one_person_2020_nh_black.geojson -L hispanic:data/processed_data/dc_one_point_one_person_2020_hispanic.geojson -L asian_pacific:data/processed_data/dc_one_point_one_person_2020_nh_asian_pacific.geojson -L multiple:data/processed_data/dc_one_point_one_person_2020_nh_multiple.geojson -L native:data/processed_data/dc_one_point_one_person_2020_nh_native.geojson -L other:data/processed_data/dc_one_point_one_person_2020_nh_other.geojson --minimum-zoom=10 --maximum-zoom=14'
tippecanoe_command = 'tippecanoe -f -e data/processed_data/dcpoint -L white:data/processed_data/dc_one_point_one_person_2020_nh_white.geojson -L black:data/processed_data/dc_one_point_one_person_2020_nh_black.geojson -L hispanic:data/processed_data/dc_one_point_one_person_2020_hispanic.geojson -L asian_pacific:data/processed_data/dc_one_point_one_person_2020_nh_asian_pacific.geojson -L multiple:data/processed_data/dc_one_point_one_person_2020_nh_multiple.geojson -L native:data/processed_data/dc_one_point_one_person_2020_nh_native.geojson -L other:data/processed_data/dc_one_point_one_person_2020_nh_other.geojson -L blocks:data/processed_data/dc_blocks.geojson --minimum-zoom=10 --maximum-zoom=14'
os.system(tippecanoe_command)

#Move tile.json out of dcpoint directory
os.system('mv data/processed_data/dcpoint/tile.json tile.json')

#Upload vector tile directory
os.system("aws s3 cp data/processed_data/dcpoint s3://tiles.mappingtiles.com/dcpoint/ --recursive --content-type application/x-protobuf --content-encoding 'gzip'")

#Move the tile.json file back
os.system('mv tile.json data/processed_data/dcpoint/tile.json')

#Upload the tile.json file
os.system("aws s3 cp data/processed_data/dcpoint/tile.json s3://tiles.mappingtiles.com/dcpoint/tile.json")

