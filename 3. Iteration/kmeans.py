
import math
import csv
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


if __name__ == "__main__":

    a1 = []
    a2 = []

    with open('similar.csv', 'rb') as f:
        rr = csv.reader(f, delimiter= ';')
        for row in rr:
            a1.append(row[0])   # #Vorkommen von Hashtags
            a2.append(row[1])   # Laenge eines Hashtags


    # Matrix mit den x-Werten (aus a1) & y-Werten (aus a2)
    X = np.matrix(zip(a1,a2))
    # kMeans Alg. fuer k=5; initiale Cluster-Center werden zufaellig
    # durch die integrierte Funktion 'KMeans' bestimmt
    kmeans = KMeans(n_clusters=5).fit(X)
    print("End-Cluster-Center:")
    print(kmeans.cluster_centers_)

    colormap = np.array(['lime', 'black', 'red', 'cyan', 'yellow'])

    plt.figure(figsize=(15,15))

    # ordne jedem Punkt entsprechend seines Clusters eine Farbe zu
    plt.scatter(a1,a2, c=colormap[kmeans.labels_],s=80)
    # markiere im Plot die Cluster-Center mit einem Kreuz
    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],marker='x', s= 200, linewidth=2,c='black')
    plt.xlabel('# Vorkommen eines Hashtags')
    plt.ylabel('Laenge eines Hashtags')
    plt.title('k-Means fuer k=5 Cluster')
    plt.show()




