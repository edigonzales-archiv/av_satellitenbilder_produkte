#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

INPUT_ROOT_PATH = "/home/stefan/Downloads/Mosaik/clip/"
OUTPUT_PATH = "/home/stefan/Downloads/Mosaik/stretched_8bit/"

for i in range(9):
	if i == 2:
		continue
	elif i == 6:
		continue

	# scale values from QGIS 1-99 percent.

	cmd = "gdal_translate -scale_1 182 450 0 255 -scale_2 343 664  0 255 -scale_3 309 502 0 255 -ot Byte  -co TILED=YES -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE -co PREDICTOR=2 -a_srs EPSG:2056 " + INPUT_ROOT_PATH + "/clip_Mosaik" + str(i) + ".tif " + OUTPUT_PATH + "stretched_8_Mosaik" + str(i) + ".tif"
	os.system(cmd)

	cmd = "gdaladdo --config PHOTOMETRIC_OVERVIEW RGB --config COMPRESS_OVERVIEW DEFLATE " + OUTPUT_PATH + "stretched_8_Mosaik" + str(i) + ".tif 2 4 8 16 32 64"
	os.system(cmd)	
	
