import pandas as pd

# Load data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path, delimiter=';', header=None, names=['Drug1', 'Drug2'])
        return data
    except FileNotFoundError:
        print("The data file was not found.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing the file: {e}")
        return None

# Check interaction between two specific drugs
def check_interaction_between_two_drugs(data, drug1, drug2):
    interactions = data[((data['Drug1'] == drug1) & (data['Drug2'] == drug2)) |
                        ((data['Drug1'] == drug2) & (data['Drug2'] == drug1))]
    
    if not interactions.empty:
        return "Do not associate these two drugs together."
    else:
        return "No interaction. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional."

# Check all interactions for one drug
def check_all_interactions_for_one_drug(data, drug):
    interactions = data[(data['Drug1'] == drug) | (data['Drug2'] == drug)]
    if interactions.empty:
        return "No interactions found for this drug."
    else:
        interacting_drugs = pd.concat([interactions['Drug1'], interactions['Drug2']])
        interacting_drugs = interacting_drugs[interacting_drugs != drug].unique().tolist()  # Remove duplicates and exclude the input drug
        interacting_drugs.sort()
        interaction_count = len(interacting_drugs)
        result = f"Interactions for {drug}:\n"
        result += "\n".join(interacting_drugs)
        result += f"\n\nThere are {interaction_count} drugs interacting with {drug}."
        return result

def main():
    file_path = 'data/drug_interactions.csv'
    data = load_data(file_path)
    
    if data is None:
        return

    while True:
        choice = input("Do you want to check interaction between two drugs or all interactions for one drug? (two/one): ").strip().lower()
        if choice == 'two':
            drug1 = input("Enter the first drug name: ").strip()
            drug2 = input("Enter the second drug name: ").strip()
            result = check_interaction_between_two_drugs(data, drug1, drug2)
            print(result)
        elif choice == 'one':
            drug = input("Enter the drug name: ").strip()
            result = check_all_interactions_for_one_drug(data, drug)
            print(result)
        else:
            print("Invalid choice. Please enter 'two' or 'one'.")
        
        another_check = input("Do you want to check another interaction? (yes/no): ").strip().lower()
        if another_check != 'yes':
            break

if __name__ == "__main__":
    main()
