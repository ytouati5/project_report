import pytest
from drug_interactions.interaction_checker import DrugInteractionChecker

@pytest.fixture
def setup_checker():
    test_file_path = 'data/drug_interactions.csv'
    return DrugInteractionChecker(test_file_path)

def test_check_interaction(setup_checker):
    assert setup_checker.check_interaction('Aspirin', 'Warfarin') == "Do not associate these two drugs together."
    assert setup_checker.check_interaction('Aspirin', 'Vitamin C') == "No interaction detected."

def test_list_interactions(setup_checker):
    expected_output = "Interactions for Aspirin:\n- Warfarin"
    assert setup_checker.list_interactions('Aspirin') == expected_output
    assert setup_checker.list_interactions('Vitamin C') == "No listed interactions for this drug."

def test_invalid_drug_names(setup_checker):
    assert setup_checker.check_interaction('XXX', 'YYY') == "No interaction detected."
    assert setup_checker.list_interactions('XXX') == "No listed interactions for this drug."
