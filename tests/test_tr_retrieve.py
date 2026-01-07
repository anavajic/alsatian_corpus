import pytest
import als_retrieve_1

#standard cases
def test_tr_retrieve_present():
    word_to_check = "Apfel"
    list_of_words = ["Äpfel", "Apfel"]
    result = als_retrieve_1.tr_retrieve(word_to_check, list_of_words)
    assert result == True

def test_tr_retrieve_not_present():
    word_to_check = "Schule"
    list_of_words = ["gross", "groß", "größter"]
    result = als_retrieve_1.tr_retrieve(word_to_check, list_of_words)
    assert result == False

#edge cases
def test_tr_retrieve_empty_list():
    word_to_check = "parapluie"
    list_of_words = []
    result = als_retrieve_1.tr_retrieve(word_to_check, list_of_words)
    assert result == False

def test_tr_retrieve_types():
    word_to_check = "terre"
    list_of_words = "pomme de terre"
    with pytest.raises(ValueError):
        als_retrieve_1.tr_retrieve(word_to_check, list_of_words)

def test_tr_retrieve_non_alphanumerical():
    word_to_check = "_&(-èç:;;"
    list_of_words = ["_&(-èç:;;", "vaisseau"]
    result = als_retrieve_1.tr_retrieve(word_to_check, list_of_words)
    assert result == False

def test_tr_retrieve_word_with_dash():
    word_to_check = "couvre-chef"
    list_of_words = ["couvre-chef", "chapeau"]
    result = als_retrieve_1.tr_retrieve(word_to_check, list_of_words)
    assert result == True



