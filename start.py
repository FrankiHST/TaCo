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
        #print(len(obj['tables']))
        print(obj)
        return(obj)

def strings_by_extractiontype(json_string):
    """
    This method splits the json in single objects.
    """
    number_of_extractiontypes = len(json_string["tables"])
    for x in range(number_of_extractiontypes):
        extractiontype_line=json_string["tables"][x]["table_name"]
        print(extractiontype_line)

def main():
    """Main method.
    """
    config_path = "./config.json"
    file_string = read_config_to_string(config_path)
    strings_by_extractiontype(file_string)

if __name__ == "__main__":
    sys.exit(main())
    