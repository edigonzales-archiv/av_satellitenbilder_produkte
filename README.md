Eventuell erst am Ende komprimieren?!
PREDICTOR=2 macht nochmals 20 prozent weniger.



gdal_translate -co TILED=YES -co PHOTOMETRIC=RGB -a_srs EPSG:2056 Mosaik0.IMG Mosaik0.tif
gdaladdo --config PHOTOMETRIC_OVERVIEW RGB --config COMPRESS_OVERVIEW DEFLATE -ro Mosaik0.tif 2 4 8 16 32 64


# Cutten 
gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -co TILED=YES -co PHOTOMETRIC=RGB -s_srs EPSG:2056 -t_srs EPSG:2056 -cutline worldview3_perimeter.shp -cl worldview3_perimeter -dstalpha -dstnodata "0 0 0 0" -co PHOTOMETRIC=RGB Mosaik0.tif cut_Mosaik0.tif

gdaladdo --config PHOTOMETRIC_OVERVIEW RGB -ro cut_Mosaik0.tif 2 4 8 16 32 64

# Alphachannel macht Probleme
gdal_translate -b 1 -b 2 -b 3 -co TILED=YES -co PHOTOMETRIC=RGB cut_Mosaik0.tif cut__3band_Mosaik0.tif
gdaladdo --config PHOTOMETRIC_OVERVIEW RGB -ro cut__3band_Mosaik0.tif 2 4 8 16 32 64

# QGIS
1-99 Prozent
TILED=YES
ALPHA=NO
NBITS=11
-> das liefert aber nur 8bit...

# händisch?
gdal_translate -scale_1 177 709 0 65535 -scale_2 333 1054  0 65535 -scale_3 300 786 0 65535 -co TILED=YES -co PHOTOMETRIC=RGB -ot UInt16  cut__3band_Mosaik0.tif cut__3band_scale_Mosaik0.tif

gdaladdo --config PHOTOMETRIC_OVERVIEW RGB -ro cut__3band_scale_Mosaik0.tif 2 4 8 16 32 64

# doch nur rgb wegen rawtherapee
gdal_translate -b 1 -b 2 -b 3 -co TILED=YES cut__3band_qgis_Mosaik0.tif cut__3band_qgis_3band_Mosaik0.tif 

gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -co TILED=YES -co PHOTOMETRIC=RGB -s_srs EPSG:2056 -t_srs EPSG:2056 -cutline worldview3_perimeter.shp -cl worldview3_perimeter -dstnodata "255 255 255" -co PHOTOMETRIC=RGB cut__3band_qgis_3band_Mosaik0.tif cut__3band_qgis_3band_cut_Mosaik0.tif


#WEGEN nodata
convert cut__3band_qgis_3band_cut_Mosaik0.tif fubar.tif

 Then I do 'gdalwarp -wo "INIT_DEST=255,0,255" square.tif square_cut.tif -cutline small_square_with_hole.csv' and I get a nice extract of my white square with a hole and a background of pink. 





gdalwarp -co TILED=YES -co PHOTOMETRIC=RGB -tr 0.9 0.9 cut__3band_scale_Mosaik0.tif cut__3band_scale_Mosaik0_small.tif


# Weiss (wegen rawtherapee)
# Weisse Pixel innerhalb????
gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -co TILED=YES -co PHOTOMETRIC=RGB -s_srs EPSG:2056 -t_srs EPSG:2056 -cutline worldview3_perimeter.shp -cl worldview3_perimeter -dstnodata "255 255 255" -co PHOTOMETRIC=RGB Mosaik0.tif cut_weiss_Mosaik0.tif

gdaladdo --config PHOTOMETRIC_OVERVIEW RGB -ro cut_weiss_Mosaik0.tif 2 4 8 16 32 64






-co PREDICTOR=2


--config PREDICTOR_OVERVIEW 2
--config COMPRESS_OVERVIEW DEFLATE
--config PHOTOMETRIC_OVERVIEW RGB

==================

gdal_translate -co TILED=YES -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE -a_srs EPSG:2056 ../worldview3_1/Mosaik0.tif Mosaik0.tif

gdaladdo --config PHOTOMETRIC_OVERVIEW RGB -ro Mosaik0.tif 2 4 8 16 32 64




gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -co TILED=YES -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE -s_srs EPSG:2056 -t_srs EPSG:2056 -cutline worldview3_perimeter.shp -cl worldview3_perimeter -dstalpha -dstnodata "0 0 0 0" -co PHOTOMETRIC=RGB Mosaik0.tif cut_Mosaik0.tif

gdaladdo -ro cut_Mosaik0.tif 2 4 8 16 32 64
