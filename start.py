#!/usr/bin/python
"""
This program reads a config file.
After this generates configuration files for Theobald XTract Unsiversal.
"""
import json
import sys

def read_config_to_string(path):
    """
    That´s a method to read the coinfig file. 
    """
    with open(path,'r',encoding="utf-8") as file:
        obj = json.load(file)
        return(obj)

def extraction_data(json_string, extraction_type):
    """
    This method splits the json in single objects.
    """
    number_of_extractiontypes = len(json_string[extraction_type])
    extractiontype_lines_list={}
    for x in range(number_of_extractiontypes):
        extractiontype_lines_list.update({json_string[extraction_type][x][extraction_type+"_name"][0]:json_string[extraction_type][x]["source"]})
    print(extractiontype_lines_list)

def main():
    """Main method.
    """
    x_type = "table"
    config_path = "./config.json"
    x_string = read_config_to_string(config_path)
    extraction_data(x_string, x_type)

if __name__ == "__main__":
    sys.exit(main())
    