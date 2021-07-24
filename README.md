# Нечестный знак
<img style="border: 1px solid #F2E208; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius:10px;" src="https://habrastorage.org/webt/7w/rw/6w/7wrw6w-k_woryibchbnbpezesag.jpeg">

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

P.S Я решил опубликовать это потому что меня уже достало качество реализации наших национальных проектов. Честный знак мог быть хорошим проектом, но его как обычно не доделали до надлежащего качества.
