#!/usr/bin/python
"""
This program reads a config file.
After this generates configuration files for Theobald XTract Unsiversal.
"""
import json
import sys

def read_config(path):
    """
    That´s a method to read the coinfig file. 
    """
    with open(path,'r',encoding="utf-8") as file:
        obj = json.load(file)
        #print(len(obj['tables']))
        print(obj)
        return(obj)

def single_items(json_string):
    """
    This method splits the json in single objects.
    """
    string = json_string
    print(string)

def main():
    """Main method.
    """
    config_path = "./config.json"
    file = read_config(config_path)
    single_items(file)

if __name__ == "__main__":
    sys.exit(main())
    