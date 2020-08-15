# -*- coding: UTF-8 -*-
import os

import arcpy
from arcpy import env


# 定义查找根目录，文件后缀方法getFiles
def getFiles(dir , suffix):
    res = []
    for root , directory , files in os.walk ( dir ):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            name , suf = os.path.splitext ( filename )  # =>文件名,文件后缀
            if suf == suffix:
                # res.append ( filename )
                res.append ( os.path.join ( root , filename ) )  # =>把一串字符串组合成路径

    return res


# shift_features() USE ArcGIS methord
def shift_features(infeatures , x_shift=None , y_shift=None):
    with arcpy.da.UpdateCursor ( infeatures , ['SHAPE@XY'] ) as cursor:
        for row in cursor:
            cursor.updateRow ( [[row[0][0] + (0) ,
                                 row[0][1] + (y_shift)]] )
    return


# 主文件main
def main():
    list_name = []
    print("nihao")  # text arcpy is output
    path = "C:\\Users\\fuxy\\Desktop\\shapefile"

    # 调用方法getFiles查找shp文件 Use getFiles method to look up *.shpfiles
    for file in getFiles ( path , '.shp' ):  # =>查找以.py结尾的文件

        print("file has %s " % (file))

        list_name.append ( file )

    print("list name has %s" % (list_name))

    env.workspace = r"C:\\Users\\fuxy\\Desktop\\shapefile"  # =>工作空间，选择自己的

    for i in range ( len ( list_name ) ):  # =>选择数组里的shp文件

        name = list_name[i]

        print(name)
        # 调用shift_features()
        infeatures = name  # =>input shp filepaths'array 'name '

        shift_features ( infeatures , x_shift=0 , y_shift=200000 )
        print("坐标转换好了")  # just for confirm it is running


print("Excellent!")  # for text

if __name__ == "__main__":
    main ()
