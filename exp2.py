import numpy as np

def nominal_dissimilarity(a, b):
    """Calculate dissimilarity between two nominal attributes."""
    return 1 if a != b else 0

def numeric_dissimilarity(a, b):
    """Calculate dissimilarity between two numeric attributes (using normalized absolute difference)."""
    return abs(a - b)

def mixed_dissimilarity(record1, record2, attribute_types):
    """Calculate dissimilarity between two records with mixed attribute types."""
    dissimilarity = 0
    for i, attr_type in enumerate(attribute_types):
        if attr_type == 'nominal':
            dissimilarity += nominal_dissimilarity(record1[i], record2[i])
        elif attr_type == 'numeric':
            dissimilarity += numeric_dissimilarity(record1[i], record2[i])
        else:
            raise ValueError(f"Unknown attribute type: {attr_type}")
    return dissimilarity

def normalize_numeric_values(records, numeric_indices):
    """Normalize numeric attributes in a dataset."""
    numeric_values = np.array([[record[i] for i in numeric_indices] for record in records])
    min_vals = numeric_values.min(axis=0)
    max_vals = numeric_values.max(axis=0)
    range_vals = max_vals - min_vals
    
    normalized_records = []
    for record in records:
        normalized_record = list(record)
        for i, index in enumerate(numeric_indices):
            normalized_record[index] = (record[index] - min_vals[i]) / range_vals[i] if range_vals[i] != 0 else 0
        normalized_records.append(normalized_record)
    
    return normalized_records

if __name__ == "__main__":
    num_records = int(input("Enter the number of records: "))
    records = []
    attribute_types = []

    print("\nEnter attribute types (nominal/numeric) for each attribute:")
    num_attributes = int(input("Enter the number of attributes: "))
    for i in range(num_attributes):
        attr_type = input(f"Attribute {i + 1} type: ")
        attribute_types.append(attr_type)
    
    print("\nEnter the records (one attribute per line, separated by spaces):")
    for i in range(num_records):
        record = input(f"Record {i + 1}: ").split()
        for j, attr_type in enumerate(attribute_types):
            if attr_type == 'numeric':
                record[j] = float(record[j])
        records.append(record)
    
    # Normalize numeric attributes
    numeric_indices = [i for i, attr_type in enumerate(attribute_types) if attr_type == 'numeric']
    normalized_records = normalize_numeric_values(records, numeric_indices)

    # Compute dissimilarity between all pairs of records
    print("\nDissimilarity between pairs of records:")
    for i in range(len(normalized_records)):
        for j in range(i + 1, len(normalized_records)):
            dissimilarity = mixed_dissimilarity(normalized_records[i], normalized_records[j], attribute_types)
            print(f"Dissimilarity between Record {i + 1} and Record {j + 1}: {dissimilarity:.4f}")
