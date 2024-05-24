import unittest
import pandas as pd
from drug_interactions.interactions import load_data, find_interaction, find_all_interactions

class TestDrugInteractions(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Charger les données de test
        file_path = '/mnt/data/drug_interactions_corrected.csv'
        print(f"Attempting to load data from {file_path}")  # Ajout de l'impression pour débogage
        cls.data = load_data(file_path)
        if cls.data.empty:
            print(f"Data failed to load from {file_path}")  # Ajout de l'impression pour débogage
            raise RuntimeError("Failed to load data for testing")
        else:
            print("Data loaded successfully")  # Ajout de l'impression pour débogage

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
