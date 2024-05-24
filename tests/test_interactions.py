import unittest
import pandas as pd
from drug_interactions.interactions import load_data, find_interaction, find_all_interactions

class TestDrugInteractions(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data = load_data('data/drug_interactions.csv')

    def test_load_data(self):
        self.assertIsInstance(self.data, pd.DataFrame)
        self.assertIn('Drug1', self.data.columns)
        self.assertIn('Drug2', self.data.columns)

    def test_find_interaction(self):
        self.assertTrue(find_interaction(self.data, 'aspirin', 'ibuprofen'))
        self.assertFalse(find_interaction(self.data, 'aspirin', 'vitamin C'))

    def test_find_all_interactions(self):
        interactions = find_all_interactions(self.data, 'aspirin')
        self.assertIsInstance(interactions, pd.DataFrame)
        self.assertGreater(len(interactions), 0)

if __name__ == '__main__':
    unittest.main()
