import pytest
import clean

#standard cases
def test_clean_multiple_words():
    string = "verdiana [ACPA] ; verdeene [ACPA]"
    result = clean.clean(string)
    assert result == "verdiana;verdeene"

def test_clean_one_word():
    string = "Pfihler [ACPA]"
    result = clean.clean(string)
    assert result == "Pfihler"

def test_clean_multiple_codes():
    string = "Iltis [ACPA;OLCA67;OLCA68]"
    result = clean.clean(string)
    assert result == "Iltis"

#edge cases
def test_clean_no_codes():
    string = "Nüdle ; Nüdla ; Nüdel "
    result = clean.clean(string)
    assert result == "Nüdle;Nüdla;Nüdel"

def test_clean_empty_string():
    string = ""
    with pytest.raises(ValueError):
        clean.clean(string)

def test_clean_type():
    string = 3.6
    with pytest.raises(ValueError):
        clean.clean(string)
