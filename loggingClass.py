"""
Das log module
"""
from datetime import datetime
import getpass
import platform

class Log:
    """
    Das ist die Log Klasse.
    Diese klasse stellt die Loggingfunktionalitäten bereit.
    """
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_name = getpass.getuser()
    maschine_name = platform.node()
    file_name = ".\\error_output.err"

    def __init__(self):
        pass

    def logging(self, message, ts=log_time, maschine=maschine_name, file=file_name, user=user_name):
        """
        Die logging Funktion, zum übrmitteln von Einträgen an das log
        """
        message_text = "\n"+ts+"\t"+message+"\t"+user+"\t"+maschine+"\t"
        try:
            with open(file, "r", encoding="utf-8") as log:
                with open(file, "a", encoding="utf-8") as log:
                    log.write(message_text)
        except FileNotFoundError:
            with open(file, "w", encoding="utf-8") as log:
                log.write("ts\terror message\tuser\tmaschine name\t")
            with open(file, "a", encoding="utf-8") as log:
                log.write(message_text)
