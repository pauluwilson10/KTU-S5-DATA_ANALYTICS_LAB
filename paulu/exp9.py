import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def initialize_centroids(data, k):
    """Randomly initialize centroids."""
    indices = np.random.choice(data.shape[0], k, replace=False)
    return data[indices]

def assign_clusters(data, centroids):
    """Assign clusters based on the closest centroid."""
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def update_centroids(data, labels, k):
    """Update centroids as the mean of the assigned clusters."""
    return np.array([data[labels == i].mean(axis=0) for i in range(k)])

def kmeans(data, k, max_iters=100):
    """Perform K-Means clustering."""
    centroids = initialize_centroids(data, k)
    for _ in range(max_iters):
        labels = assign_clusters(data, centroids)
        new_centroids = update_centroids(data, labels, k)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, labels

# Load data from CSV
df = pd.read_csv('kmean.csv')  # Ensure the CSV file is in the same directory or provide the full path

# Select the 'height' and 'weight' columns for clustering
data = df[['height', 'weight']].values

# Ask the user for the number of clusters
k = int(input("Enter the number of clusters (k): "))

# Run K-Means
centroids, labels = kmeans(data, k)

# Check the unique labels returned by K-Means
unique_labels = np.unique(labels)
print(f"Unique cluster labels: {unique_labels}")
print(f"Expected number of clusters: {k}, Actual number of clusters: {len(unique_labels)}")

# Print cluster information to terminal
for i in unique_labels:
    print(f"\nCluster {i+1}:")
    cluster_data = data[labels == i]
    print(cluster_data)

# Plot the results
plt.figure(figsize=(8, 6))
for i in unique_labels:
    plt.scatter(data[labels == i][:, 0], data[labels == i][:, 1], label=f'Cluster {i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='X', s=200, label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()





