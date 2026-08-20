from calculator.financial.revenue import subscription_revenue, annual_subscription_revenue


def test_subscription_revenue():
    assert subscription_revenue(1000, 15000) == 15000000


def test_subscription_revenue_with_collection_and_free():
    assert subscription_revenue(1000, 15000, 0.8, 100) == 10800000


def test_annual_subscription_revenue():
    assert annual_subscription_revenue(1000, 15000) == 180000000
