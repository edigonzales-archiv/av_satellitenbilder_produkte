#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

INPUT_ROOT_PATH = "/home/stefan/Downloads/Mosaik/stretched_8bit/"
OUTPUT_PATH = "/home/stefan/Downloads/Mosaik/3band_8bit/"

for i in range(9):
	if i == 2:
		continue
	elif i == 6:
		continue
		
	cmd = "gdal_translate  -b 1 -b 2 -b 3 -ot Byte  -co TILED=YES -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE -co PREDICTOR=2 -a_srs EPSG:2056 " + INPUT_ROOT_PATH + "/stretched_8_Mosaik" + str(i) + ".tif " + OUTPUT_PATH + "3b_8_Mosaik" + str(i) + ".tif"
	os.system(cmd)
	
	cmd = "gdaladdo --config PHOTOMETRIC_OVERVIEW RGB --config COMPRESS_OVERVIEW DEFLATE " + OUTPUT_PATH + "3b_8_Mosaik" + str(i) + ".tif 2 4 8 16 32 64"
	os.system(cmd)	
