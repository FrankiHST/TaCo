from datetime import datetime
import subprocess
import getpass
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
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = getpass.getuser()
        try:
            subprocess.run([path, "--extraction",source,destination, extraction_type,table], capture_output=True, check=True)
        except subprocess.CalledProcessError as e:
            with open(".\\error_output.err", "a", encoding="utf-8") as f:
                    formatted_e=f"Error message: {e}"
                    f.write(f"\nTS: {log_time}\t")
                    f.write(formatted_e+"\t")
                    f.write("User: "+user_name+"\t")
            if e.stderr:
                with open(".\\error_output.err", "a", encoding="utf-8") as f:
                    formatted_stderr=f"Error message: {e.stderr}"
                    f.write(f"\nTS: {log_time}\t")
                    f.write(formatted_stderr+"\t")
                    f.write("User: "+user_name+"\t")
