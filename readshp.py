# coding:utf-8
import os
import arcpy
import csv


def dirtread(directory):
    for root , dirs , files in os.walk ( directory ):
        ct = 0
        for file in files:
            if file.endswith ( ".shp" ):
                pth = os.path.join ( directory , file )
                filename = file.replace ( ".shp" , "" )
                if arcpy.Exists ( filename ):
                    arcpy.management.Delete ( filename )

                arcpy.MakeFeatureLayer_management ( pth , filename )
                result = arcpy.GetCount_management ( file )
                count = int ( result.getOutput ( 0 ) )

                print(file)
                print(count)

                arcpy.RefreshActiveView ()




def main():
    cxls = 'data.csv'
    with open ( cxls , 'r' ) as f:
        reader = csv.DictReader ( f )

        list_name = []
        for row in reader:
            list_name.append ( row['PATH'] )
        # print(list_name)

        for i in range ( len ( list_name ) ):
            print(list_name[i])


            directory = list_name[i]

            dirtread ( directory )




if __name__ == "__main__":
    main ()

