import src.logic as logic

def test_taxes_and_benefits_are_found():
    datasets = logic.get_useful_datasets()
    assert "Taxes and Benefits" in datasets[0]["title"]