class ExtraktionGeneral:
    """
    Dies ist die Klasse ExtraktionGeneral.
    Diese Klasse entspricht der general.json Konfigurationsdatei einer Extraktion.
    """
    def _init_(self, extraktionstyp, source, destination):
        self._extraktionstyp=extraktionstyp
        self._source=source
        self._destination=destination

class ExtraktionDestination:
    """
    Dies ist die Klasse ExtraktionDestination.
    Diese Klasse entspricht der destination.json Konfigurationsdatei einer Extraktion.
    """
    def _init_(self, destinationtype):
        self._destinationtype=destinationtype
        pass