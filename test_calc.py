from calc import add

def test_add():
    # This is the challenge: 2+3 is NOT 6, so CI will fail!
    assert add(2, 3) == 6
