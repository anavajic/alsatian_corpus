import pytest
import cognates_scores

def test_pron_score():
    pron1 = ('APSNS', '')
    pron2 = ('APSNS', '')
    result = cognates_scores.pron_score(pron1, pron2)
    assert result == 1.0