import pytest

def test_pass():
    # Denne test vil passere
    assert 1 + 1 == 2


def test_fail():
    # Denne test vil fejle
    assert 1 * 1 == 3


@pytest.mark.skip(reason="Springes over med vilje") # Denne test bliver slet ikke kørt
def test_skip():
    assert False # failed test bliver ignoreret
    raise RuntimeError("Test crashede med vilje") # crash bliver også ignoreret


def test_crash():
    # Denne test crasher med en exception
    raise RuntimeError("Test crashede med vilje")
    assert False # failed test bliver ignoreret

def test_another_pass():
    # Endnu en test der vil passere
    #given
    length = 5
    width = 4
    expectedArea = 20

    #when
    actualArea = length * width

    #then
    assert actualArea == expectedArea

    
def test_another_fail():
    # Endnu en test der vil fejle
    #given
    base = 3
    height = 6
    expectedArea = 15

    #when
    actualArea = 0.5 * base * height

    #then
    assert actualArea == expectedArea

