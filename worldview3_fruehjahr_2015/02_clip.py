#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

INPUT_ROOT_PATH = "/home/stefan/Downloads/Mosaik/"
OUTPUT_PATH = "/home/stefan/Downloads/Mosaik/clip/"
CLIP_FILE = "/home/stefan/Projekte/av_satellitenbilder_produkte/worldview3_fruehjahr_2015/perimeter/worldview3_perimeter.shp"

for i in range(9):
	if i == 2:
		continue
	elif i == 6:
		continue
	cmd = 'gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -co TILED=YES -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE -co PREDICTOR=2 -s_srs EPSG:2056 -t_srs EPSG:2056 -cutline ' + CLIP_FILE + ' -cl worldview3_perimeter -dstalpha -dstnodata "0 0 0 0" -co PHOTOMETRIC=RGB ' + INPUT_ROOT_PATH + 'Mosaik' + str(i) + '.tif ' + OUTPUT_PATH + 'clip_Mosaik' + str(i) + '.tif'
	os.system(cmd)

	cmd = "gdaladdo --config PHOTOMETRIC_OVERVIEW RGB --config COMPRESS_OVERVIEW DEFLATE " + OUTPUT_PATH + "clip_Mosaik" + str(i) + ".tif 2 4 8 16 32 64"
	os.system(cmd)
