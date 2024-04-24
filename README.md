<p align="center">
    <img src="https://habrastorage.org/webt/7w/rw/6w/7wrw6w-k_woryibchbnbpezesag.jpeg">
</p>
<p align="center">
    <img src="https://img.shields.io/pypi/v/nechestniy_znak.svg">&nbsp;&nbsp;<img src="https://img.shields.io/pypi/pyversions/nechestniy_znak.svg">
</p>

Библеотека обертка для API ГИС МТ "Честный Знак" и API ЕГАИС

[Документация](https://li0ard.gitbook.io/nechestniy_znak/)

### Установка

**Требуется Python версии 3.8 или выше**
```
pip install nechestniy_znak
```

### Пример
```py
from nechestniy_znak import Crpt, Egais

crpt = Crpt()
print(crpt.infoFromEAN13(46494139))
print(crpt.infoFromDataMatrix("00000046209849Uon<TYfACyAJPHJ"))
print(crpt.infoFromQr("chek.markirovka.nalog.ru/kc/?kiz=RU-430302-AAA4050108"))
print(crpt.infoFromReceipt("t=20231203T2319&s=261.80&fn=7281440701309134&i=10027&fp=3516337491&n=1"))

egais = Egais()
print(egais.getInfoByMarkOld("22N00001543ZQO6QFMW37ZK80215021095854A4P1E4IHMW86GT5RTFHN5XXFABT9TZ9", "104-101355000854071217387105240265"))
print(egais.getInfoByMarkNew("171200031066131018001EWB6ECS6IGT6L2OH7XP6QFJMTYQMXCZ5WWVPNDLUU7BCE4FWLCBM7QDHQSESJCTOIXMEAHE2EZLXRZXJJT4UJ4OKEFEIO7RE7J7LQK2ISDFXIA34UAYOZ5ZRYFLTXI4TQ"))
print(egais.getInfoByAlcCode("0150320000003561384"))
print(egais.getChains("171200031066131018001EWB6ECS6IGT6L2OH7XP6QFJMTYQMXCZ5WWVPNDLUU7BCE4FWLCBM7QDHQSESJCTOIXMEAHE2EZLXRZXJJT4UJ4OKEFEIO7RE7J7LQK2ISDFXIA34UAYOZ5ZRYFLTXI4TQ"))
```
