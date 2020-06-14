import requests
import json

class Dolar(object):
    __dolares = list
    def __init__(self):
        self.__dolares = []
    def actualizar(self):
        self.__dolares = []
        r = json.loads(requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales").content)
        for element in r:
            if "dolar" in element["casa"]["nombre"].lower() and element["casa"]["venta"] != "0" and element["casa"]["compra"].lower()!="no cotiza":
                d = { "compra": element["casa"]["compra"], "venta": element["casa"]["venta"], "nombre": element["casa"]["nombre"]}
                self.__dolares.append(d)
        return self.__dolares
    def obtener(self):
        return self.__dolares