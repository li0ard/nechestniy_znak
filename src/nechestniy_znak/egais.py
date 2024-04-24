import requests, urllib3
from typing import Union
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Egais:
    def __init__(self):
        pass
    
    def _get(self, url: str, params: str) -> Union[list, dict]:
        return requests.get(f"http://mobapi.fsrar.ru/api3/{url}?{params}", verify=False).json()
    
    def getInfoByMarkOld(self, pdf417: str, datamatrix: str) -> Union[list, dict]:
        return self._get("mark", f"DataMatrix={datamatrix}&Pdf417={pdf417}")

    def getInfoByMarkNew(self, datamatrix: str) -> Union[list, dict]:
        return self._get("marklong", f"Pdf417={datamatrix}")

    def getInfoByAlcCode(self, alc_code: str) -> Union[list, dict]:
        return self._get("product_info", f"alc_code={alc_code}")
    
    def getChains(self, datamatrix: str) -> Union[list, dict]:
        return self._get("chain", f"barcode={datamatrix}")