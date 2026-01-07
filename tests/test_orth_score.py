import pytest
import cognates_scores

def test_orth_score_with_alsatian_word():
    word1 = "Kugelschreiber"
    word2 = "Kegalaschriwer"
    result = cognates_scores.orth_score(word1, word2)
    assert result == 0.7142857142857143

def test_orth_score_identical_words():
    word1 = "Flora"
    word2 = "Flora"
    result = cognates_scores.orth_score(word1, word2)
    assert result == 1.0

def test_orth_score_without_alsatian_word():
    word1 = "zehla"
    word2 = "."
    result = cognates_scores.orth_score(word1, word2)
    assert result == "."

def test_orth_score_empty_string():
    word1 = ""
    word2 = "pomme"
    with pytest.raises(ValueError):
        cognates_scores.orth_score(word1, word2)

def test_orth_score_type():
    word1 = ["kirche", "église"]
    word2 = "Kirche"
    with pytest.raises(ValueError):
        cognates_scores.orth_score(word1, word2)