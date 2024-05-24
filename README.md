
![Project Logo](assets/banner.png)

![Coverage Status](assets/coverage-badge.svg)

<h1 align="center">
Drug Interaction Checker
</h1>

<br>

A Python package to check for negative interactions between drugs, allowing users to either check the interaction between two specific drugs or list all possible interactions for one drug.

## 🔥 Usage

```python
from interaction_checker import load_data, check_interaction_between_two, list_interactions

interaction_data = load_data('drug_interactions.csv')

option = input("Enter '1' to check the interaction between two drugs or '2' to check all possible interactions of one drug: ")

if option == '1':
    drug1 = input("Enter the name of the first drug: ")
    drug2 = input("Enter the name of the second drug: ")
    result = check_interaction_between_two(drug1, drug2, interaction_data)
    print(result)
elif option == '2':
    drug = input("Enter the name of the drug: ")
    result = list_interactions(drug, interaction_data)
    print(result)
else:
    print("Invalid option. Please enter '1' or '2'.")
```

This usage example shows how to quickly leverage the package's main functionalities. After loading the interaction data, you can either check the interaction between two drugs or list all possible interactions for one drug based on user input.

## 👩‍💻 Installation

Create a new environment, you may also give the environment a different name.

```
conda create -n drug_interactions python=3.10
```

```
conda activate drug_interactions
(drug_interactions) $ pip install .
```

If you need jupyter lab, install it

```
(drug_interactions) $ pip install jupyterlab
```

## 🛠️ Development installation

Initialize Git (only for the first time).

```
git init
git add *
git add .*
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:yourusername/drug_interactions.git
git push -u origin main
```

Then add and commit changes as usual.

To install the package, run

```
(drug_interactions) $ pip install -e ".[test,doc]"
```

### Run tests and coverage

```
(drug_interactions) $ pip install tox
(drug_interactions) $ tox
```

## 📖 Code Explanation

The script provides two main functionalities based on user input:

1. **Check Interaction Between Two Drugs**:
    - The user is prompted to enter the names of two drugs.
    - The script checks if these two drugs appear on the same line in the dataset.
    - If they do, it outputs: "Do not associate these two drugs together."
    - If they don't, it outputs: "No interaction. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional."
    - If one or both drugs are not found in the data, it outputs: "Unlisted."

2. **List All Possible Interactions of One Drug**:
    - The user is prompted to enter the name of a drug.
    - The script lists all drugs that interact negatively with the specified drug.
    - If no interactions are found, it outputs: "No known bad interactions."

