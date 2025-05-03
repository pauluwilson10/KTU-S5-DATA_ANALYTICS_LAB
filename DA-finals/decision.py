# import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
import csv


# Step 1: Read the CSV Data
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
# Step 2: Build Decision Tree
def build_tree(data, target_attribute):
    X = data.drop(columns=[target_attribute])
    y = data[target_attribute]
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf

# Step 3: Display the Decision Tree
def display_tree(clf, feature_names):
    tree_rules = export_text(clf, feature_names=feature_names)
    print(tree_rules)

# Step 4: Predict Function
def predict(clf, instance):
    return clf.predict([instance])[0]

# Step 5: User Input
def get_user_input():
    age = input("Enter age (youth/middle_aged/senior): ")
    income = input("Enter income (high/medium/low): ")
    student = input("Are you a student? (yes/no): ")
    credit_rating = input("Enter credit rating (fair/excellent): ")
    return [age, income, student, credit_rating]

# Main Function
def main():
    data = read_csv('decision_tree.csv')
    print(data)
    target_attribute = 'class_buys_computer'  # Replace with your target attribute
    clf = build_tree(data, target_attribute)
    display_tree(clf, data.columns.drop(target_attribute))
    instance = get_user_input()
    prediction = predict(clf, instance)
    print(f"Prediction for class_buys_computer: {prediction}")

if __name__ == "__main__":
    main()