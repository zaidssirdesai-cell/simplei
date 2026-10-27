from simpleinterest import simInt

def test_simpleInt_pos():
    assert simInt(20000, 8, 12) == 19200

def test_simpleInt_zer():
    assert simInt(10000, 7, 0) == 0

def test_simpleInt_nev():
    assert simInt(20000, 8, -12) == -19200