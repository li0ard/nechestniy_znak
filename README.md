<img src="https://habrastorage.org/webt/7w/rw/6w/7wrw6w-k_woryibchbnbpezesag.jpeg">

[Github](https://github.com/li0ard/nechestniy_znak)

Библеотека обертка для API ГИС МТ "Честный Знак"
### Установка
Просто скачайте и переместите файл `nechestniy_znak.py` и импортируйте его как показано в примере.
### Пример
```py
from nechestniy_znak import Lib

lib = Lib()
print(lib.infoFromEAN13(46494139))
print(lib.infoFromDataMatrix("%1D0104601026065163211G0AAGA54V0AU%1D91EE06%1D92o9c61AE0Mk9pQRmoXG0C7drBBF+CIQQhuLlyZ6rQM7o="))
```
