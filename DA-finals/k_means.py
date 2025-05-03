import csv
import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    data = []
    with open(filename,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

data = read_file('k-means.csv')

num_clusters = int(input("Enter the number of clusters: "))
centroids=[]
for i in range(1,num_clusters+1):
    centroids.append([float(data[i][1]),float(data[i][2])])

clusters = []
for i in range(num_clusters):
    clusters.append([])

counter = 0

while True:
    for i in range(num_clusters):
        clusters[i]=[]
    
    counter+=1
    for i in range(1,len(data)):
        x=float(data[i][1])
        y=float(data[i][2])
        distances=[]
        for j in range(num_clusters):
            distance=(x-centroids[j][0])**2+(y-centroids[j][1])**2
            distances.append(distance)
        min_distance_index=distances.index(min(distances))
        clusters[min_distance_index].append([x,y])

    new_centroids=[]
    for i in range(num_clusters):
        new_centroids.append([0,0])

    for j in range(num_clusters):
        if  len(clusters[j])>0:
            for point in clusters[j]:
                new_centroids[j][0]+=point[0]
                new_centroids[j][1]+=point[1]
            new_centroids[j][0]/=len(clusters[j])
            new_centroids[j][1]/=len(clusters[j])

    if new_centroids==centroids or counter>100:
        break
    centroids=new_centroids

for i in range(num_clusters):
    print(f"clusters{i+1}:",clusters[i])
    print(f"centroids{i+1}:",centroids[i])




for i in range(num_clusters):
    cluster_points=np.array(clusters[i])
    plt.scatter(cluster_points[:,0],cluster_points[:,1],label=f"cluster{i+1}")

centroids_points=np.array(centroids)
plt.scatter(centroids_points[:,0],centroids_points[:,1],s=300,c='red',marker='X',label='Centroids')

plt.title('K-means Clustering')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')    
plt.legend()
plt.show()
    