import src.logic as logic

def test_taxes_and_benefits_are_found():
    datasets = logic.get_useful_datasets()
    assert "Taxes and Benefits" in datasets[0]["title"]

def test_find_taxes_and_benefits_lastest_url():
    latest = logic.get_latest_taxes_and_benefits_url()    
    assert "tax-benefits-statistics/editions/time-series/versions" in latest