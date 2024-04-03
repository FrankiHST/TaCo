#!/usr/bin/python
"""
Dieses Programm erstellt aus einer eingelesenen Konfigurationsdatei 
die Konfigurationsdateien für die Extraktionen
im XTract Universal von Theobald.
"""
import sys
from extractionClass import Extraktion
from configurationClasses import ExtraktionGeneral



def main():
    """Main method.
    """
    i_configtool="\\xu-config.exe"
    i_extraction_type="table"
    i_config_path = "./config.json"
    object_json=ExtraktionGeneral.__read_konfiguration__("a", i_config_path)
    i_main_path=object_json["main_path"]
    i_tool_path=i_main_path+i_configtool
    number_of_extractiontypes = len(object_json[i_extraction_type])
    for x in range(number_of_extractiontypes):
        extraction_list_table=len(object_json[i_extraction_type][x][i_extraction_type+"_name"])
        for y in range(extraction_list_table):
            i_table_name=object_json[i_extraction_type][x][i_extraction_type+"_name"][y]
            i_source=object_json[i_extraction_type][x]["source"]
            i_destination=object_json[i_extraction_type][x]["dest"]
            print(i_table_name, i_source, i_destination)
            Extraktion.__create_extraction__("a", i_tool_path, i_table_name, i_source, i_destination)


if __name__ == "__main__":
    sys.exit(main())
