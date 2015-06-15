#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

INPUT_ROOT_PATH = "/home/stefan/Downloads/Mosaik"
OUTPUT_PATH = "/home/stefan/Downloads/Mosaik/"

for i in range(9):
	if i == 2:
		continue
	elif i == 6:
		continue

	cmd = "gdal_translate -co TILED=YES -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE -co PREDICTOR=2 -a_srs EPSG:2056 " + INPUT_ROOT_PATH + str(i) + "/Mosaik" + str(i) + ".IMG " + OUTPUT_PATH + "Mosaik" + str(i) + ".tif"
	#os.system(cmd)

	cmd = "gdaladdo --config PHOTOMETRIC_OVERVIEW RGB --config COMPRESS_OVERVIEW DEFLATE " + OUTPUT_PATH + "Mosaik" + str(i) + ".tif 2 4 8 16 32 64"
	#os.system(cmd)
	
	cmd = "listgeo -tfw " + OUTPUT_PATH + "Mosaik" + str(i) + ".tif"
	os.system(cmd)
