import pytest
import cognates_scores

def test_pron_score_same_word():
    pron1 = ('APSNS', '')
    pron2 = ('APSNS', '')
    result = cognates_scores.pron_score(pron1, pron2)
    assert result == 1.0

def test_pron_score_different_word():
    pron1 = ('AFRNT', '')
    pron2 = ('PLTKNK', '')
    result = cognates_scores.pron_score(pron1, pron2)
    assert result == 0.18181818181818182

def test_pron_score_without_alsatian_word():
    pron1 = ('AFRNT', '')
    pron2 = ('', '')
    result = cognates_scores.pron_score(pron1, pron2)
    assert result == "."
