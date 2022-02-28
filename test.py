from nechestniy_znak import Lib

lib = Lib()
print(lib.infoFromEAN13(46494139))
print(lib.infoFromDataMatrix("00000046209849Uon<TYfACyAJPHJ"))
print(lib.infoFromQr("chek.markirovka.nalog.ru/kc/?kiz=RU-430302-AAA4050108"))