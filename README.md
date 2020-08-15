# ArcpyScript
# arcgis arcpy scripts

arcgis：10.3.1

背景：第一次尝试运用arcpy批量脚本，解决工作实践中遇到的繁琐的任务；

## shiftpolygons.py

Discription:

In order to shift multiple polygons in files;

介绍：

用来批量读取有多级目录的文件夹里的shp文件，需要shp里面的图形的y坐标往上移20000
通过 arcpy.da.UpdateCursor方法完成

## readshp.py

 []任务背景：需要比对转换坐标后的shp文件字段是否丢失，数据量过大，  
