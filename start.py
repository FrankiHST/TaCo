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
        print(obj)


def main():
    """Main method.
    """
    config_path = "./config.json"
    print("hello")
    print(config_path)
    read_config(config_path)

if __name__ == "__main__":
    sys.exit(main())
    