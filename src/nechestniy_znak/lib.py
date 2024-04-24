# НЕЧестный Знак
# (C) 2021, li0ard, ЦРПТ

import requests
from dataclasses import dataclass
from typing import Optional
import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU')


@dataclass
class ProductCatalogCategory:
    cat_id: int
    cat_name: str


@dataclass
class ProductCatalogAttribute:
    attr_id: int
    attr_name: str
    attr_value: str
    attr_value_type: Optional[str]


@dataclass
class ProductCatalog:
    img_src: str
    categories: list[ProductCatalogCategory]
    attributes: list[ProductCatalogAttribute]


@dataclass
class Product:
    data: dict
    name: str
    code: str
    code_type: str
    product_id: int
    product_catalog: Optional[ProductCatalog]
    brand: Optional[str]
    cost: Optional[int]
    date_time_end: Optional[dt.datetime]


class Lib:
    def __init__(self):
        pass

    @staticmethod
    def fabric_ProductCatalogAttribute(json: dict) -> ProductCatalogAttribute:
        return ProductCatalogAttribute(
            attr_id=json.get("attr_id"),
            attr_name=json.get("attr_name"),
            attr_value=json.get("attr_value"),
            attr_value_type=json.get("attr_value_type") if json.get("attr_value_type") else None
        )

    @staticmethod
    def fabric_ProductCatalogCategory(json: dict) -> ProductCatalogCategory:
        return ProductCatalogCategory(
            cat_id=json.get("cat_id"),
            cat_name=json.get("cat_name")
        )

    def fabric_ProductCatalog(self, json: dict) -> ProductCatalog:
        return ProductCatalog(
            categories=list(map(self.fabric_ProductCatalogCategory, json["categories"])),
            img_src=json.get("good_img"),
            attributes=list(map(self.fabric_ProductCatalogAttribute, json["good_attrs"]))
        )

    def fabric_Product(self, json) -> Product | None:
        if not json.get("codeFounded") or not json.get("checkResult"):
            return None

        date_end = None
        expirations = json.get('expirations')
        if expirations:
            date_details = expirations[0]
            if date_details:
                expiration_description = date_details.get('expirationDescription')
                if expiration_description:
                    date_map = expiration_description[0]
                    if date_map:
                        date_string = date_map.get('conditions')
                        if date_string:
                            date_end = dt.datetime.strptime(date_string, "dd MMMM yyyy")

        return Product(
            data=json,
            name=json.get('productName'),
            code=json.get('code'),
            code_type=json.get('codeType'),
            product_id=json.get('id'),
            product_catalog=self.fabric_ProductCatalog(json.get('catalogData')[0]) if json.get('catalogData') else None,
            brand=json.get('brand'),
            date_time_end=date_end,
            cost=json.get('cost')
        )

    @staticmethod
    def _get(content: str, codeType: str) -> list | dict:
        return requests.get(f"https://mobile.api.crpt.ru/mobile/check?code={content}&codeType={codeType}").json()

    @staticmethod
    def _post(data: dict | list) -> list | dict:
        return requests.post(f"https://mobile.api.crpt.ru/mobile/check", json=data, headers={
            "content-type": "application/json",
            "accept"      : "application/json",
            "user-agent"  : "Platform: iOS 17.2; AppVersion: 4.47.0; AppVersionCode: 7630; Device: iPhone 14 Pro;",
            "client"      : "iOS 17.2; AppVersion: 4.47.0; Device: iPhone 14 Pro;"
        }).json()

    def infoFromDataMatrix(self, xyematrix: str) -> list | dict:
        return self._get(xyematrix, "datamatrix")

    def infoFromEAN13(self, ean13: str) -> list | dict:
        return self._get(ean13, "ean13")

    def infoFromQr(self, qr: str) -> list | dict:
        return self._get(qr, "qr")

    def infoFromReceipt(self, code: str) -> list | dict:
        return self._post({
            "code"    : code,
            "codeType": "qr",
        })

    def get_product_by_EAN13(self, ean13: str) -> Product | None:
        json = self.infoFromEAN13(ean13)
        return self.fabric_Product(json)

    def get_product_by_DataMatrix(self, xyematrix: str) -> Product | None:
        json = self.infoFromDataMatrix(xyematrix)
        return self.fabric_Product(json)
