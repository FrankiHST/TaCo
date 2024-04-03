import subprocess
from loggingClass import Log

class Extraktion:
    """
    Dies ist die Klasse Extraktion.
    Sie entspricht einer konfigurierten Extraktion im XTract Universal.
    """
    angelegteExtraktionen=0
    def __init__(self,source, dest, extraktionsname, extraktionsnamensuffix="V001",extraktionstyp="table"):
        self._source=source
        self._dest=dest
        self._extraktionsname=extraktionsname
        self._extraktionsnamensuffix=extraktionsnamensuffix
        self._extraktionstyp=extraktionstyp
        Extraktion.angelegteExtraktionen+=1

    def __del__(self):
        Extraktion.angelegteExtraktionen-=1

    def __create_extraction__(self, path, table, source, destination, extraction_type="--table"):
        try:
            subprocess.run([path, "--extraction",source,destination, extraction_type,table], capture_output=True, check=True)
        except subprocess.CalledProcessError as e:
            formatted_stderr=f"{e.stderr}"
            Log.logging("a", formatted_stderr)
            if e.stderr:
                formatted_e=f"{e}"
                Log.logging("a", formatted_e)

