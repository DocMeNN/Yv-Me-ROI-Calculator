from calculator.financial.funding import funding_gap, funding_coverage


def test_funding_gap():
    assert funding_gap(1000000, 750000) == 250000


def test_no_funding_gap():
    assert funding_gap(1000000, 1500000) == 0


def test_funding_coverage():
    assert funding_coverage(1000000, 750000) == 0.75
