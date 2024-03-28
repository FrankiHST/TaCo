import json
class ExtraktionGeneral:
    """
    Dies ist die Klasse ExtraktionGeneral.
    Diese Klasse entspricht der general.json Konfigurationsdatei einer Extraktion.
    """
    def __init__(self, extraktionstyp, source, destination):
        self._extraktionstyp=extraktionstyp
        self._source=source
        self._destination=destination
        
    def __read_konfiguration__(self, path):
        with open(path,'r',encoding="utf-8") as file:
            obj = json.load(file)
        return obj
    
