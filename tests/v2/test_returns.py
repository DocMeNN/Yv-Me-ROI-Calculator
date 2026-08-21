from calculator.v2.returns import irr, npv


def test_npv_zero_discount_rate():
    assert npv([-100, 60, 60], 0) == 20


def test_npv_discounted():
    result = npv([-100, 60, 60], 0.10)
    assert round(result, 6) == 4.132231


def test_irr():
    result = irr([-100, 60, 60])
    assert result is not None
    assert round(result, 6) == 0.130662


def test_irr_requires_mixed_cash_flows():
    assert irr([100, 50, 25]) is None
    assert irr([-100, -50, -25]) is None
