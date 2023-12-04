from nechestniy_znak import Lib

lib = Lib()
print(lib.infoFromEAN13(46494139))
print(lib.infoFromDataMatrix("00000046209849Uon<TYfACyAJPHJ"))
print(lib.infoFromQr("chek.markirovka.nalog.ru/kc/?kiz=RU-430302-AAA4050108"))
print(lib.infoFromReceipt("t=20231203T2319&s=261.80&fn=7281440701309134&i=10027&fp=3516337491&n=1"))