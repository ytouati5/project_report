import pandas as pd

def load_data():
    return pd.read_csv('../data/drug_interactions.csv')

def check_interaction(df, drug1, drug2):
    interactions = df[(df['Drug1'] == drug1) & (df['Drug2'] == drug2) | (df['Drug1'] == drug2) & (df['Drug2'] == drug1)]
    if not interactions.empty:
        print("Do not associate these two drugs together.")
    else:
        print("No interaction. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional.")

def list_interactions(df, drug):
    associated_drugs = pd.concat([
        df[df['Drug1'] == drug]['Drug2'],  # If 'drug' is in 'Drug1', get corresponding 'Drug2'
        df[df['Drug2'] == drug]['Drug1']   # If 'drug' is in 'Drug2', get corresponding 'Drug1'
    ]).unique()  # Remove duplicates
    
    associated_drugs.sort()  # Alphabetically sort the drugs

    # Output the total count and the list of drugs that should not be associated with 'drug'
    print(f"{drug} should not be associated with {len(associated_drugs)} drugs in total:")
    for d in associated_drugs:
        print(d)

def main():
    df = load_data()
    while True:
        choice = input("Do you want to (1) check interaction between two drugs or (2) check all interactions for one drug? Enter 1 or 2: ")
        if choice == '1':
            drug1 = input("Enter the first drug: ")
            drug2 = input("Enter the second drug: ")
            check_interaction(df, drug1, drug2)
        elif choice == '2':
            drug = input("Enter the drug: ")
            list_interactions(df, drug)
        else:
            print("Invalid input, please enter 1 or 2.")

if __name__ == "__main__":
    main()
