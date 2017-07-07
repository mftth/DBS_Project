
import math
import csv
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import sys

reload(sys)  
sys.setdefaultencoding('utf8')


if __name__ == "__main__":

# Aufgabe 1) k-Means
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
    print(kmeans.labels_)


# *******
# zu Aufgabe 2.3) Netzwerk mit aehnlichen Hashtags

    # in cl.csv werden die Labels der Cluster (1 bis 5) gespeichert
    c = kmeans.labels_
    with open('cl.csv', "wb") as o:
        wr= csv.writer( o , delimiter=';' )
        for i in range(0,len(c)):
            wr.writerow([(c[i]+1)])

    # in h_cl.csv werden in der 1.Spalte der Hashtagname
    # und in der 2.Spalte das zugehörige Cluster-Label gespeichert
    with open('anzahl.csv', 'rb') as f1, open('cl.csv', 'rb') as f2, open('h_cl.csv', "wb") as o1:
        rr1 = csv.reader(f1, delimiter= ';')
        rr2 = csv.reader(f2, delimiter= ';')
        wr1= csv.writer( o1 , delimiter=';' )
        l = []
        m = []

        for row1 in rr1:
           l.append(row1[0].splitlines()[0])
        for row2 in rr2:
           m.append(row2[0])

        for i in range(0,len(l)):
            wr1.writerow([l[i],m[i]])

# *******
# zu Aufgabe 1) Visualisierung des k-Means

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




