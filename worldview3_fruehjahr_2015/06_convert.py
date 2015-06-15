#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

INPUT_ROOT_PATH = "/home/stefan/Downloads/Mosaik/3band_8bit/"
OUTPUT_PATH = "/home/stefan/Downloads/Mosaik/convert/"

for i in range(9):
	if i == 2:
		continue
	elif i == 6:
		continue
		
	cmd = "convert " + INPUT_ROOT_PATH + "/3b_8_Mosaik" + str(i) + ".tif " + OUTPUT_PATH + "convert_Mosaik" + str(i) + ".tif"
	os.system(cmd)


