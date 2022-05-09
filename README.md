### Race dot density map

This repository contains the code associated with www.mappingtiles.com, where I have mapped every person who responded to the US 2020 Census by their race/ethnicity.

- Chicago_create_point_layer.ipynb: This file contains the code used to disaggregate the 2020 block-level population data into a shapefile with one point for every person, positioned in the block they live. The strategy was identical for all cities.
- tile_creation_pipeline.py: This file contains the code use to process the point data for DC. The code runs a series of commands on the command line to generate a Mapbox Vector Tile directory with layers for each race. This directory is then uploaded to an AWS S3 bucket.
