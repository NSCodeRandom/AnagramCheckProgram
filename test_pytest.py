"""This module contains test programs to check if functions of app.py works as expected"""
# pylint: disable = W0621, C0200, C0201, C0206, C0303

import app

def test_check_total_comparisons_validity():
    """Test Function to validate check_total_comparisons_validity"""
    assert app.check_total_comparisons_validity(-5) == 0
    assert app.check_total_comparisons_validity(-5.544) == 0
    assert app.check_total_comparisons_validity(5.5444) == 0
    assert app.check_total_comparisons_validity(5) == 1

def test_compare_lengths():
    """Test Function to check compare_lengths"""
    assert app.compare_lengths("hell0", "helloo") == 0
    assert app.compare_lengths("","") == 1
    assert app.compare_lengths("", "hello") == 0
    assert app.compare_lengths("abcd", "abcd") == 1

def test_check_char_frequencies():
    """Test Function to check check_char_frequencies"""
    assert app.check_char_frequencies("hello", "hello") == 1
    assert app.check_char_frequencies("","") == 1
    assert app.check_char_frequencies("hell&&o", "#hell&&") == 0
    assert app.check_char_frequencies("hell#o", "helo#l") == 1

def test_check_anagram():
    """Test Function to check test_check_anagram"""
    assert app.check_anagram(["Restful", "Fluster"]) == 1
    assert app.check_anagram(["Room", "Dorm"]) == 0
    assert app.check_anagram(["Dormitory", "Dirty Room"]) == 1
    assert app.check_anagram(["Evil", "Vile"]) == 1
    assert app.check_anagram(["hell&& O", "o && hell"]) == 1
    assert app.check_anagram(["", ""]) == 1
    assert app.check_anagram(["#$", "$ #"]) == 1
    assert app.check_anagram(["hello", ""]) == 0


    
