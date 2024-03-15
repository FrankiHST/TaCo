#!/usr/bin/python
"""
Dieses Programm erstellt aus einer eingelesenen Konfigurationsdatei die Konfigurationsdateien für die Extraktionen
im XTract Universal von Theobald.
###https://www.hdm-stuttgart.de/~maucher/Python/html/Klassen.html
v0.1 einlesen der Konfigurationsdatei
v0.2 Klasse Extraktion
v0.3 Klasse ExtraktionGeneral
v0.4 Klasse ExtraktionDestination 
"""
import json
import sys

def __lese_konfiguration__(self, path):
    with open(path,'r',encoding="utf-8") as file:
        obj = json.load(file)
    return obj

def __erstelle_extraktionen__(self):
    pass

class Extraktion:
    """
    Dies ist die Klasse Extraktion.
    Sie entspricht einer konfigurierten Extraktion im XTract Universal.
    """
    angelegteExtraktionen=0
    def __init__(self,extraktionsname, extraktionsnamensuffix="V001",extraktionstyp="table"):
        self.__extraktionsname=extraktionsname
        self.__extraktionsnamensuffix=extraktionsnamensuffix
        self.__extraktionstyp=extraktionstyp
        Extraktion.angelegteExtraktionen+=1

    def __del__(self):
        Extraktion.angelegteExtraktionen-=1
        
class ExtraktionGeneral:
    """
    Dies ist die Klasse ExtraktionGeneral.
    Diese Klasse entspricht der general.json Konfigurationsdatei einer Extraktion.
    """
    def __init__(self, extraktionstyp, source, destination, destinationtype, tablename):
        self.__extraktionstyp=extraktionstyp
        self.__source=source
        self.__destination=destination
        self.__destinationstype=destinationtype
        self.__tablename=tablename

    def __del__(self):
        pass

class ExtraktionDestination:
    """
    Dies ist die Klasse ExtraktionDestination.
    Diese Klasse entspricht der destination.json Konfigurationsdatei einer Extraktion.
    """
    def __init__(self):
        pass
    def __del__(self):
        pass


def table_extraction_data(json_string, extraction_type):
    """
    This method splits the json in single objects.
    """
    number_of_extractiontypes = len(json_string[extraction_type])
    extraction_lines_list={}
    for x in range(number_of_extractiontypes):
        extraction_list_table_name=json_string[extraction_type][x][extraction_type+"_name"]
        for y, extraction_list_table_name in enumerate(extraction_list_table_name):
            extractiontype_lines=[]
            extractiontype_lines.append(json_string[extraction_type][x][extraction_type+"_name"][y])
            extractiontype_lines.append(json_string[extraction_type][x]["source"])
            extractiontype_lines.append(json_string[extraction_type][x]["dest"])
            extractiontype_lines.append(json_string[extraction_type][x]["dest_type"])
            extractiontype_lines.append(json_string[extraction_type][x]["machine"])
            extractiontype_lines.append("Table")
            print(extraction_list_table_name)
            extraction_name=(
                json_string[extraction_type][x]["source"]+'_'+
                extraction_list_table_name+'_'+json_string[extraction_type][x]["dest"]+'_'+
                json_string[extraction_type][x]["name_suffix"])
            extraction_lines_list[extraction_name]=extractiontype_lines
    print(extraction_lines_list)

def main():
    """Main method.
    """
    x_type = "table"
    config_path = "./config.json"
    x_string = read_config_to_string(config_path)
    table_extraction_data(x_string, x_type)

if __name__ == "__main__":
    sys.exit(main())
    