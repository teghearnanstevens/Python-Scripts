import pytest
from chemistry import make_periodic_table

def test_make_periodic_table():

    assert make_periodic_table()[0] == ["Ac", "Actinium", 227]
    assert make_periodic_table()[1] == ["Ag", "Silver", 107.8682]
    assert make_periodic_table()[-1] == ["Zr", "Zirconium", 91.224]

pytest.main(["-v", "--tb=line", "-rN", __file__])