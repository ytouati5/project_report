import pandas as pd

data = pd.read_csv('/Users/yass/github/practical_programming/project_report/data/drug_interactions.csv')
data[['Drug1', 'Drug2']] = data.iloc[:, 0].str.split(';', expand=True)

def check_interaction():
    choice = input("Do you want to (1) check interaction between two drugs or (2) check all interactions for one drug? Enter 1 or 2: ")
    if choice == '1':
        drug1 = input("Enter the first drug name: ").strip().lower()
        drug2 = input("Enter the second drug name: ").strip().lower()
        interactions = data[(data['Drug1'].str.lower() == drug1) & (data['Drug2'].str.lower() == drug2) |
                            (data['Drug1'].str.lower() == drug2) & (data['Drug2'].str.lower() == drug1)]
        if not interactions.empty:
            print("Do not associate these two drugs together.")
        else:
            print("No interaction. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional.")
    elif choice == '2':
        drug = input("Enter the drug name: ").strip().lower()
        interactions = data[(data['Drug1'].str.lower() == drug) | (data['Drug2'].str.lower() == drug)]
        if not interactions.empty:
            print(f"List of interactions for {drug}:")
            for index, row in interactions.iterrows():
                print(f"{row['Drug1']} interacts with {row['Drug2']}")
        else:
            print("No listed interactions. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional.")
    else:
        print("Invalid input. Please enter 1 or 2.")

check_interaction()