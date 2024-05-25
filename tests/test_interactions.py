import unittest
import pandas as pd
from io import StringIO
from drug_interactions import load_data, check_interaction_between_two_drugs, check_all_interactions_for_one_drug

class TestDrugInteractions(unittest.TestCase):

    def setUp(self):
        
        self.csv_data = StringIO("""Drug1;Drug2
DrugA;DrugB
DrugA;DrugC
DrugB;DrugD
""")
        self.data = pd.read_csv(self.csv_data, delimiter=';', header=0, names=['Drug1', 'Drug2'])

    def test_load_data(self):
        # Test with valid data
        result = load_data('data/drug_interactions.csv')
        self.assertIsNotNone(result)
        self.assertIn('Drug1', result.columns)
        self.assertIn('Drug2', result.columns)

    def test_load_data_file_not_found(self):
        # Test with invalid file path
        result = load_data('data/non_existent_file.csv')
        self.assertIsNone(result)

    def test_check_interaction_between_two_drugs(self):
        # Test interaction exists
        result = check_interaction_between_two_drugs(self.data, 'DrugA', 'DrugB')
        self.assertEqual(result, "Do not associate these two drugs together.")
        
        # Test no interaction
        result = check_interaction_between_two_drugs(self.data, 'DrugA', 'DrugD')
        self.assertEqual(result, "No interaction. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional.")

    def test_check_all_interactions_for_one_drug(self):
        # Test interactions for a specific drug
        result = check_all_interactions_for_one_drug(self.data, 'DrugA')
        expected_result = "Interactions for DrugA:\nDrugB\nDrugC\n\nThere are 2 drugs interacting with DrugA."
        self.assertEqual(result, expected_result)
        
        # Test no interactions
        result = check_all_interactions_for_one_drug(self.data, 'DrugE')
        self.assertEqual(result, "No interactions found for this drug.")

if __name__ == '__main__':
    unittest.main()
