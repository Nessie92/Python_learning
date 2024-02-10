import pandas as pd
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Convert CSV file into a DataFrame
df = pd.read_csv('ML_Learning/credircardinfo.csv')

# Mapping dictionaries
category_mappings = {
    'Gender': {'M': 0, 'F': 1},
    'Married': {'Y': 1, 'N': 0},
    'Job': {'Y': 1, 'N': 0}
}

for column, mapping in category_mappings.items():
    df[column] = df[column].map(mapping) #single [] because accessing a single column(series)


# Separate features from the target column
X = df[['Age', 'Gender', 'Salary', 'Job', 'Married', 'Num_children']]# double [] for selecting multiple columns 
y = df['type_credit']

# Create a Decision Tree Classifier instance
dtree = DecisionTreeClassifier()

# Train the Decision Tree Classifier on the dataset
dtree.fit(X, y)

# Create a figure for the decision tree visualization
plt.figure(figsize=(12, 6))

# Visualize the decision tree with feature names and filled nodes
plot_tree(dtree, feature_names=['Age', 'Gender', 'Salary', 'Job', 'Married', 'Num_children'], filled=True)
plt.show()

# Obtain client information
client_age = int(input("How old is the client? "))
client_gender = input("Is the client male(m) or female (f)? ").upper()
client_salary = int(input("How much does the client earn each month (in $)? "))
client_job = input("Is the client currently employed (y / n)? ").upper()
client_married = input("Is the client currently married (y/n)? ").upper()
client_children = int(input("How many children does the client have? "))

# Make a decision
client_data = [[client_age, category_mappings['Gender'].get(client_gender, 0), client_salary,
                category_mappings['Job'].get(client_job, 0),
                category_mappings['Married'].get(client_married, 0), client_children]]
decision = dtree.predict(client_data)

decision_labels = {0: "Client Declined",
                   1: "Client approved for regular credit card",
                   2: "Client approved for Gold Card"}

print(decision_labels.get(decision[0], "Invalid Decision"))

#category_mappings['Gender'][client_gender]
#print(decision_labels[decision[0]])

