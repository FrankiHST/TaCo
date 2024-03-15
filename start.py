#!/usr/bin/python
"""
This program reads a config file.
After this generates configuration files for Theobald XTract Unsiversal.
"""
import json
import sys

class Extraktion:
    """
    Dies ist die Klasse Extraktion.
    https://www.hdm-stuttgart.de/~maucher/Python/html/Klassen.html
    Sie entspricht einer konfigurierten Extraktion im XTract Universal.
    """
    angelegteExtraktionen=0
    def __init__(self,extraktionsnamensuffix="V001",extraktionstyp="table"):
        self.__extraktionsnamensuffix=extraktionsnamensuffix
        self.__extraktionstyp=extraktionstyp
        Extraktion.angelegteExtraktionen+=1

    def __del__(self):
        Extraktion.angelegteExtraktionen-=1


def read_config_to_string(path):
    """
    That´s a method to read the coinfig file. 
    """
    with open(path,'r',encoding="utf-8") as file:
        obj = json.load(file)
        return obj

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
    