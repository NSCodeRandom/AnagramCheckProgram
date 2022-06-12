import app

def test_checkTotalComparisonsValidity():
    assert app.checkTotalComparisonsValidity(-5) == 0
    assert app.checkTotalComparisonsValidity(-5.544) == 0
    assert app.checkTotalComparisonsValidity(5.5444) == 0
    assert app.checkTotalComparisonsValidity(5) == 1

def test_compareLengths():
    assert app.compareLengths("hell0", "helloo") == 0
    assert app.compareLengths("","") == 1
    assert app.compareLengths("", "hello") == 0
    assert app.compareLengths("abcd", "abcd") == 1

def test_checkCharFrequencies():
    assert app.checkCharFrequencies("hello", "hello") == 1
    assert app.checkCharFrequencies("","") == 1
    assert app.checkCharFrequencies("hell&&o", "#hell&&") == 0
    assert app.checkCharFrequencies("hell#o", "helo#l") == 1

def test_checkAnagram():
    assert app.checkAnagram(["Restful", "Fluster"]) == 1
    assert app.checkAnagram(["Room", "Dorm"]) == 0
    assert app.checkAnagram(["Dormitory", "Dirty Room"]) == 1
    assert app.checkAnagram(["Evil", "Vile"]) == 1
    assert app.checkAnagram(["hell&& O", "o && hell"]) == 1
    assert app.checkAnagram(["", ""]) == 1
    assert app.checkAnagram(["#$", "$ #"]) == 1
    assert app.checkAnagram(["hello", ""]) == 0


    
