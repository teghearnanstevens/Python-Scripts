from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
   
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    
   
    assert make_full_name("Jean-Paul", "Sartre") == "Sartre; Jean-Paul"
    
    
    assert make_full_name("A", "B") == "B; A"
    
    
    assert make_full_name("Alexander", "TheGreat") == "TheGreat; Alexander"


def test_extract_family_name():
   
    assert extract_family_name("Toussaint; Marie") == "Toussaint"
    
   
    assert extract_family_name("Sartre; Jean-Paul") == "Sartre"
    
    
    assert extract_family_name("B; A") == "B"
    
    
    assert extract_family_name("TheGreat; Alexander") == "TheGreat"

def test_extract_given_name():
    
    assert extract_given_name("Toussaint; Marie") == "Marie"
    
    
    assert extract_given_name("Sartre; Jean-Paul") == "Jean-Paul"
    
    
    assert extract_given_name("B; A") == "A"
    
    
    assert extract_given_name("TheGreat; Alexander") == "Alexander"

pytest.main(["-v", "--tb=line", "-rN", __file__])