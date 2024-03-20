class Extraktion:
    """
    Dies ist die Klasse Extraktion.
    Sie entspricht einer konfigurierten Extraktion im XTract Universal.
    """
    angelegteExtraktionen=0
    def _init_(self,extraktionsname, extraktionsnamensuffix="V001",extraktionstyp="table"):
        self.__extraktionsname=extraktionsname
        self.__extraktionsnamensuffix=extraktionsnamensuffix
        self.__extraktionstyp=extraktionstyp
        Extraktion.angelegteExtraktionen+=1

    def _del_(self):
        Extraktion.angelegteExtraktionen-=1