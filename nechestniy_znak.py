# НЕЧестный Знак
# (C) 2021, li0ard, ЦРПТ

import requests, urllib

class Lib:
	def __init__(self):
		pass

	def _get(self, content, type):
		return requests.get(f"https://mobile.api.crpt.ru/mobile/check?code={content}&codeType={type}").json()

	def infoFromDataMatrix(self, xyematrix):
		return self._get(xyematrix, "datamatrix")

	def infoFromEAN13(self, ean13):
		return self._get(ean13, "ean13")