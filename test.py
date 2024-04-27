import pytest
from src.nechestniy_znak import Crpt, Egais

crpt = Crpt()

def test_crptEAN13():
    assert crpt.infoFromEAN13(46494139)["checkResult"] == True

def test_crptDataMatrix():
    assert crpt.infoFromDataMatrix("00000046209849Uon<TYfACyAJPHJ")["checkResult"] == True

def test_crptQR():
    assert crpt.infoFromQr("chek.markirovka.nalog.ru/kc/?kiz=RU-430302-AAA4050108")["checkResult"] == True

def test_crptReceipt():
    assert crpt.infoFromReceipt("t=20231203T2319&s=261.80&fn=7281440701309134&i=10027&fp=3516337491&n=1")["checkResult"] == True

egais = Egais()

def test_egaisMarkOld():
    assert egais.infoFromOldMark("22N00001543ZQO6QFMW37ZK80215021095854A4P1E4IHMW86GT5RTFHN5XXFABT9TZ9", "104-101355000854071217387105240265")["success"] == True

def test_egaisMarkNew():
    assert egais.infoFromNewMark("171200031066131018001EWB6ECS6IGT6L2OH7XP6QFJMTYQMXCZ5WWVPNDLUU7BCE4FWLCBM7QDHQSESJCTOIXMEAHE2EZLXRZXJJT4UJ4OKEFEIO7RE7J7LQK2ISDFXIA34UAYOZ5ZRYFLTXI4TQ")["success"] == True

def test_egaisChains():
    assert egais.getChains("171200031066131018001EWB6ECS6IGT6L2OH7XP6QFJMTYQMXCZ5WWVPNDLUU7BCE4FWLCBM7QDHQSESJCTOIXMEAHE2EZLXRZXJJT4UJ4OKEFEIO7RE7J7LQK2ISDFXIA34UAYOZ5ZRYFLTXI4TQ")["success"] == True