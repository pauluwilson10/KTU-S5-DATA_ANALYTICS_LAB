import csv
import math

# Step 1: Read the CSV Data
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Step 2: Calculate Entropy
def entropy(data, target_attribute):
    total = len(data)
    if total == 0:
        return 0
    count_yes = 0
    count_no = 0
    for row in data:
        if row[target_attribute] == 'yes':
            count_yes += 1
        else:
            count_no += 1
    p_yes = count_yes / total
    p_no = count_no / total
    entropy_yes = -p_yes * math.log2(p_yes) if p_yes > 0 else 0
    entropy_no = -p_no * math.log2(p_no) if p_no > 0 else 0
    return entropy_yes + entropy_no

# Step 3: Calculate Information Gain
def information_gain(data, attribute, target_attribute):
    total_entropy = entropy(data, target_attribute)
    values = set()
    for row in data:
        values.add(row[attribute])
    weighted_entropy = 0
    for value in values:
        subset = []
        for row in data:
            if row[attribute] == value:
                subset.append(row)
        weighted_entropy += (len(subset) / len(data)) * entropy(subset, target_attribute)
    return total_entropy - weighted_entropy

# Step 4: Split Data
def split_data(data, attribute, value):
    subset = []
    for row in data:
        if row[attribute] == value:
            subset.append(row)
    return subset

# Step 5: Build Decision Tree
def build_tree(data, attributes, target_attribute):
    if all(row[target_attribute] == 'yes' for row in data):
        return 'yes'
    if all(row[target_attribute] == 'no' for row in data):
        return 'no'
    if not attributes:
        count_yes = 0
        for row in data:
            if row[target_attribute] == 'yes':
                count_yes += 1
        return 'yes' if count_yes >= len(data) / 2 else 'no'
    
    best_attribute = max(attributes, key=lambda attr: information_gain(data, attr, target_attribute))
    tree = {best_attribute: {}}
    values = set()
    for row in data:
        values.add(row[best_attribute])
        for value in values:
        # Create a subset of data where best_attribute has the specific value
            subset=split_data(data, best_attribute, value)
            # Create a list of remaining attributes, excluding the best_attribute
            remaining_attributes = []
            for attr in attributes:
                if attr != best_attribute:
                    remaining_attributes.append(attr)
            # Recursively build a subtree for the subset
            subtree = build_tree(subset, remaining_attributes, target_attribute)
            # Add this subtree to the tree under the branch for the specific value of best_attribute
            tree[best_attribute][value] = subtree
    return tree


# Step 6: Display the Decision Tree
def display_tree(tree):
    if isinstance(tree, dict):
        for key, value in tree.items():
            print(f"{key}")
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, dict):
                    print(f"  {sub_key} ->")
                    display_tree(sub_value)  # Recursive call without indentation
                else:
                    print(f"  {sub_key} -> {sub_value}")
    else:
        if tree == 'yes':
            print("Predict: Yes")
        else:
            print("Predict: No")


# Step 7: Predict Function
def predict(tree, instance):
    if not isinstance(tree, dict):
        return tree
    attribute = next(iter(tree))
    value = instance[attribute]
    subtree = tree[attribute].get(value, 'no')
    return predict(subtree, instance)

# Step 8: User Input
def get_user_input():
    age = input("Enter age (youth/middle_aged/senior): ")
    income = input("Enter income (high/medium/low): ")
    student = input("Are you a student? (yes/no): ")
    credit_rating = input("Enter credit rating (fair/excellent): ")
    return {'age': age, 'income': income, 'student': student, 'credit_rating': credit_rating}

# Main Function
def main():
    data = read_csv('decision_tree.csv')
    print(data)
    attributes = list(data[0].keys())
    target_attribute = 'class_buys_computer'  # Replace with your target attribute
    attributes.remove(target_attribute)
    tree = build_tree(data, attributes, target_attribute)
    display_tree(tree)
    instance = get_user_input()
    prediction = predict(tree, instance)
    print(f"Prediction for class_buys_computer: {prediction}")

if __name__ == "__main__":
    main()