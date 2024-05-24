import unittest
import pandas as pd
from drug_interactions.interactions import load_data, find_interaction, find_all_interactions

class TestDrugInteractions(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Charger les données de test
        cls.data = load_data('/mnt/data/drug_interactions_corrected.csv')
        if cls.data.empty:
            raise RuntimeError("Failed to load data for testing")

    def test_load_data(self):
        # Vérifier que les données sont correctement chargées
        self.assertIsInstance(self.data, pd.DataFrame)
        self.assertIn('Drug1', self.data.columns)
        self.assertIn('Drug2', self.data.columns)

    def test_find_interaction(self):
        # Tester la recherche d'interactions spécifiques entre deux médicaments
        self.assertTrue(find_interaction(self.data, 'aspirin', 'ibuprofen'))
        self.assertFalse(find_interaction(self.data, 'aspirin', 'vitamin C'))

    def test_find_all_interactions(self):
        # Tester la recherche de toutes les interactions pour un médicament donné
        interactions = find_all_interactions(self.data, 'aspirin')
        self.assertIsInstance(interactions, pd.DataFrame)
        self.assertGreater(len(interactions), 0)

if __name__ == '__main__':
    unittest.main()
