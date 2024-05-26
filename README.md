
![Project Logo](assets/banner.png)

![Coverage Status](https://codecov.io/gh/ytouati5/project_report/branch/main/graph/badge.svg)

<h1 align="center">
Drug Interaction Checker
</h1>

<br>

This package provides tools to check for potential drug interactions using a simple and accessible Python interface.

## 🔥 Usage

```python
from drug_interaction_checker import main

# Begin interaction checking
main()
```

This usage example demonstrates how to engage with the package's main functionality directly from the command line. After importing the `main` function, you simply run it, and it will interactively prompt you for inputs to either check interactions between two drugs or find all interactions for one drug.

## 👩‍💻 Installation

Create a new environment, you may also give the environment a different name.

```bash
conda create -n drugchecker python=3.10
```

```bash
conda activate drugchecker
(drugchecker) $ pip install .
```

If you need Jupyter Lab, install it:

```bash
(drugchecker) $ pip install jupyterlab
```

## 🛠️ Development installation

Initialize Git (only for the first time).

Note: You should have created an empty repository on `https://github.com/yourgithubusername/Drug-Interaction-Checker`.

```bash
git init
git add * 
git add .*
git commit -m "Initial commit" 
git branch -M main
git remote add origin git@github.com:yourgithubusername/Drug-Interaction-Checker.git 
git push -u origin main
```

Then add and commit changes as usual. 

To install the package, after cloning from GitHub, activate your Conda environment and run:

```bash
(drugchecker) $ pip install .
```

## 📖 Code Explanation

The script provides two main functionalities based on user input:

### Check Interaction Between Two Drugs:
- The user is prompted to enter the names of two drugs.
- The script checks if these two drugs appear on the same line in the dataset.
- If they do, it outputs: "Do not associate these two drugs together."
- If they don't, it outputs: "No interaction. Warning: The absence of drug interactions does not guarantee safety. Always consult a healthcare professional."
- If one or both drugs are not found in the data, it outputs: "Unlisted."

### List All Possible Interactions of One Drug:
- The user is prompted to enter the name of a drug.
- The script lists all drugs that interact negatively with the specified drug.
- If no interactions are found, it outputs: "No known bad interactions."

Each function uses Pandas dataframes to manage and query the dataset efficiently, ensuring quick responses even with large datasets.
```

Make sure to replace placeholders such as `yourgithubusername` with your actual GitHub username, and adjust any commands or details to better fit your specific package setup and repository settings. This README will help guide users on how to effectively get started with the package, from installation to utilizing its main features.
