# drug_interactions/interactions.py
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    try:
        # Lire le fichier CSV en ignorant les lignes problématiques
        data = pd.read_csv(file_path, on_bad_lines='skip')
        # Diviser la colonne contenant les noms des médicaments en deux colonnes distinctes
        data[['Drug1', 'Drug2']] = data.iloc[:, 0].str.split(';', expand=True)
        return data
    except Exception as e:
        # Afficher une erreur en cas de problème lors du chargement des données
        print(f"Error loading data: {e}")
        # Retourner un DataFrame vide en cas d'erreur
        return pd.DataFrame()

def find_interaction(data: pd.DataFrame, drug1: str, drug2: str) -> bool:
    # Rechercher les interactions entre deux médicaments
    interactions = data[((data['Drug1'].str.lower() == drug1) & (data['Drug2'].str.lower() == drug2)) |
                        ((data['Drug1'].str.lower() == drug2) & (data['Drug2'].str.lower() == drug1))]
    # Retourner True si des interactions sont trouvées, False sinon
    return not interactions.empty

def find_all_interactions(data: pd.DataFrame, drug: str) -> pd.DataFrame:
    # Rechercher toutes les interactions pour un médicament donné
    interactions = data[(data['Drug1'].str.lower() == drug) | (data['Drug2'].str.lower() == drug)]
    return interactions

def check_interaction(data: pd.DataFrame):
    # Demander à l'utilisateur s'il veut vérifier une interaction entre deux médicaments ou toutes les interactions pour un médicament donné
    choice = input("Do you want to (1) check interaction between two drugs or (2) check all interactions for one drug? Enter 1 or 2: ").strip()
    
    if choice == '1':
        # Si l'utilisateur choisit de vérifier une interaction entre deux médicaments
        drug1 = input("Enter the first drug name: ").strip().lower()
        drug2 = input("Enter the second drug name: ").strip().lower()
        if find_interaction(data, drug1, drug2):
            print("Do not associate these two drugs together.")
        else:
            print("No interaction. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional.")
    
    elif choice == '2':
        # Si l'utilisateur choisit de vérifier toutes les interactions pour un médicament donné
        drug = input("Enter the drug name: ").strip().lower()
        interactions = find_all_interactions(data, drug)
        if not interactions.empty:
            print(f"List of interactions for {drug}:")
            for index, row in interactions.iterrows():
                print(f"{row['Drug1']} interacts with {row['Drug2']}")
        else:
            print("No listed interactions. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional.")
    
    else:
        # Si l'utilisateur entre une option invalide
        print("Invalid input. Please enter 1 or 2.")
