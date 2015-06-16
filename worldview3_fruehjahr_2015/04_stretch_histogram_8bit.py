#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

INPUT_PATH = "/home/stefan/Downloads/Mosaik/clip/"
OUTPUT_PATH = "/home/stefan/Downloads/Mosaik/tmp/"
CLIP_FILE = "/home/stefan/Projekte/av_satellitenbilder_produkte/worldview3_fruehjahr_2015/perimeter/worldview3_perimeter.shp"

for i in range(9):
	if i == 2:
		continue
	elif i == 6:
		continue
		
	cmd = "listgeo -tfw " + INPUT_PATH + "Mosaik" + str(i) + ".tif"
	os.system(cmd)
	
	cmd = "cp " + INPUT_PATH + "Mosaik" + str(i) + ".tfw " + OUTPUT_PATH + "tmp3_Mosaik" + str(i) + ".tfw"
	os.system(cmd)

	cmd = "gdal_translate  -b 1 -b 2 -b 3 -ot Byte -co TILED=YES -co PHOTOMETRIC=RGB -a_srs EPSG:2056 " + INPUT_PATH + "Mosaik" + str(i) + ".tif " + OUTPUT_PATH + "tmp1_Mosaik" + str(i) + ".tif"
	print cmd

	# scale values from QGIS 1-99 percent.
	cmd = "gdal_translate -scale_1 182 450 0 255 -scale_2 343 664  0 255 -scale_3 309 502 0 255 -ot Byte -co ALPHA=NO -co TILED=YES -co PHOTOMETRIC=RGB -a_srs EPSG:2056 " + INPUT_PATH + "Mosaik" + str(i) + ".tif " + OUTPUT_PATH + "tmp1_Mosaik" + str(i) + ".tif"
	print cmd
	os.system(cmd)
	
	cmd = "gdal_translate  -b 1 -b 2 -b 3 -ot Byte -co TILED=YES -co PHOTOMETRIC=RGB -a_srs EPSG:2056 " + OUTPUT_PATH + "tmp1_Mosaik" + str(i) + ".tif " + OUTPUT_PATH + "tmp2_Mosaik" + str(i) + ".tif"
	print cmd	
	os.system(cmd)	
	
	cmd = "convert " + OUTPUT_PATH + "tmp2_Mosaik" + str(i) + ".tif " + OUTPUT_PATH + "tmp3_Mosaik" + str(i) + ".tif" 
	print cmd
	os.system(cmd)
	
	cmd = "gdal_edit.py -mo TIFFTAG_DOCUMENTNAME='' -a_srs EPSG:2056 " + OUTPUT_PATH + "tmp3_Mosaik" + str(i) + ".tif" 
	print cmd
	os.system(cmd)

	cmd = 'gdalwarp -wo NUM_THREADS=ALL_CPUS --config GDAL_CACHEMAX 1000 -wm 1000 -co TILED=YES -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE -co PREDICTOR=2 -s_srs EPSG:2056 -t_srs EPSG:2056 -cutline ' + CLIP_FILE + ' -cl worldview3_perimeter -dstalpha  -co PHOTOMETRIC=RGB ' + OUTPUT_PATH + 'tmp3_Mosaik' + str(i) + '.tif ' + OUTPUT_PATH + 'Mosaik' + str(i) + '.tif'	
	print cmd
	os.system(cmd)

	cmd = "gdaladdo --config PHOTOMETRIC_OVERVIEW RGB --config COMPRESS_OVERVIEW DEFLATE " + OUTPUT_PATH + "Mosaik" + str(i) + ".tif 2 4 8 16 32 64"
	os.system(cmd)	
	
	cmd = "rm " + OUTPUT_PATH + "tmp*"
	os.system(cmd)
		
