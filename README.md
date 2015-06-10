Eventuell erst am Ende komprimieren?!
PREDICTOR=2 macht nochmals 20 prozent weniger.



gdal_translate -co TILED=YES -co PHOTOMETRIC=RGB -a_srs EPSG:2056 Mosaik0.IMG Mosaik0.tif
gdaladdo --config PHOTOMETRIC_OVERVIEW RGB -ro Mosaik0.tif 2 4 8 16 32 64


gdalwarp --config GDAL_CACHEMAX 500 -wm 500 -co TILED=YES -co PHOTOMETRIC=RGB -s_srs EPSG:2056 -t_srs EPSG:2056 -cutline worldview3_perimeter.shp -cl worldview3_perimeter -dstalpha -dstnodata "0 0 0 0" -co PHOTOMETRIC=RGB Mosaik0.tif cut_Mosaik0.tif

gdaladdo --config PHOTOMETRIC_OVERVIEW RGB -ro cut_Mosaik0.tif 2 4 8 16 32 64



-co PREDICTOR=2


--config PREDICTOR_OVERVIEW 2
--config COMPRESS_OVERVIEW DEFLATE
--config PHOTOMETRIC_OVERVIEW RGB

==================