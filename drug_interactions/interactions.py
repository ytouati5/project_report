# drug_interactions/interactions.py
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path, on_bad_lines='skip')
        data[['Drug1', 'Drug2']] = data.iloc[:, 0].str.split(';', expand=True)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def find_interaction(data: pd.DataFrame, drug1: str, drug2: str) -> bool:
    interactions = data[((data['Drug1'].str.lower() == drug1) & (data['Drug2'].str.lower() == drug2)) |
                        ((data['Drug1'].str.lower() == drug2) & (data['Drug2'].str.lower() == drug1))]
    return not interactions.empty

def find_all_interactions(data: pd.DataFrame, drug: str) -> pd.DataFrame:
    interactions = data[(data['Drug1'].str.lower() == drug) | (data['Drug2'].str.lower() == drug)]
    return interactions

def check_interaction(data: pd.DataFrame):
    choice = input("Do you want to (1) check interaction between two drugs or (2) check all interactions for one drug? Enter 1 or 2: ").strip()
    
    if choice == '1':
        drug1 = input("Enter the first drug name: ").strip().lower()
        drug2 = input("Enter the second drug name: ").strip().lower()
        if find_interaction(data, drug1, drug2):
            print("Do not associate these two drugs together.")
        else:
            print("No interaction. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional.")
    
    elif choice == '2':
        drug = input("Enter the drug name: ").strip().lower()
        interactions = find_all_interactions(data, drug)
        if not interactions.empty:
            print(f"List of interactions for {drug}:")
            for index, row in interactions.iterrows():
                print(f"{row['Drug1']} interacts with {row['Drug2']}")
            print(f"There are {len(interactions)} drugs interacting with {drug}.")
        else:
            print("No listed interactions. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional.")
    
    else:
        print("Invalid input. Please enter 1 or 2.")

