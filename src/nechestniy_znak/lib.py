import requests
from typing import Union


class Lib:
    def __init__(self):
        pass

    def _get(self, content: str, type: str) -> Union[list, dict]:
        return requests.get(f"https://mobile.api.crpt.ru/mobile/check?code={content}&codeType={type}").json()

    def _post(self, data: Union[dict, list]) -> Union[list, dict]:
        return requests.post(f"https://mobile.api.crpt.ru/mobile/check", json=data, headers={
            "content-type": "application/json",
            "accept"      : "application/json",
            "user-agent"  : "Platform: iOS 17.2; AppVersion: 4.47.0; AppVersionCode: 7630; Device: iPhone 14 Pro;",
            "client"      : "iOS 17.2; AppVersion: 4.47.0; Device: iPhone 14 Pro;"
        }).json()

    def infoFromDataMatrix(self, xyematrix: str) -> Union[list, dict]:
        return self._get(xyematrix, "datamatrix")

    def infoFromEAN13(self, ean13: str) -> Union[list, dict]:
        return self._get(ean13, "ean13")

    def infoFromQr(self, qr: str) -> Union[list, dict]:
        return self._get(qr, "qr")

    def infoFromReceipt(self, code: str) -> Union[list, dict]:
        return self._post({
            "code"    : code,
            "codeType": "qr",
        })