
import math
import csv


def euclideanDistance(x,y):
   return math.sqrt(sum([(a-b)**2 for (a,b) in zip(x,y)]))

def partition(points, k, means, d=euclideanDistance):
   thePartition = [ [] for _ in means]   # list of k empty lists

   for p in points:
      dist = []
      for i in range(0,len(means)):
         dist.append(d(p, means[i]))
      mini = min(dist)               # minimum distance between each point & the k cluster centers

      for j in range(0,len(dist)):
         if dist[j] == mini:
            thePartition[j].append(p) # assign each point to a cluster

   return thePartition


def mean(points):    # mean value of coordinates of each point of points-list
   n = len(points)
   medi = tuple(float(sum(x)) / n for x in zip(*points))
   return medi



if __name__ == "__main__":

    import matplotlib.pyplot as plt

    points = []

    with open('similar.csv', 'rb') as f:
        rr = csv.reader(f, delimiter= ';')
        for row in rr:
            points.append((float(row[0]),float(row[1])))
            # points = a list of tuples: 1.argument = #occurrences of a hashtag, 2.argument = length of a hashtag

    # 1. define threshold/ termination value
    delta = 0.5

    k = 5

    # 2. select k= 5 initial cluster centers
    center = []
    center.append([50.0, 15.0])
    center.append([100.0, 25.0])
    center.append([150.0, 15.0])
    center.append([200.0, 5.0])
    center.append([250.0, 20.0])

    while True:
    # 3.1 / 3.2
       cluster = partition(points, k, center, euclideanDistance)
    
    # 3.3 update the cluster centers    
       newcenter = []

       for cl in cluster:     #  cl = cluster lists
           c = mean(cl)
           newcenter.append(c)

       d = []
       for i in range(0,k):
           d.append(euclideanDistance(center[i],newcenter[i]))

       if d[0]<= delta and d[1]<= delta and d[2]<= delta and d[3]<= delta and d[4]<= delta:
           break
       else:
           center = newcenter
 
    # create list of x-values & y-values for each cluster
    xvalues1 = []
    yvalues1 = []
    xvalues2 = []
    yvalues2 = []
    xvalues3 = []
    yvalues3 = []
    xvalues4 = []
    yvalues4 = []
    xvalues5 = []
    yvalues5 = []

    for k in cluster[0]:        #  k/l/m/n/o = point-tuples in cluster list
       xvalues1.append(k[0])
       yvalues1.append(k[1])
    for l in cluster[1]:       
       xvalues2.append(l[0])
       yvalues2.append(l[1])
    for m in cluster[2]:       
       xvalues3.append(m[0])
       yvalues3.append(m[1])
    for n in cluster[3]:      
       xvalues4.append(n[0])
       yvalues4.append(n[1])
    for o in cluster[4]:      
       xvalues5.append(o[0])
       yvalues5.append(o[1])

    # scatter-plots of the cluster
    plt.scatter(xvalues1,yvalues1, c='k')
    plt.scatter(xvalues2,yvalues2, c='g')
    plt.scatter(xvalues3,yvalues3, c='r')
    plt.scatter(xvalues4,yvalues4, c='y')
    plt.scatter(xvalues5,yvalues5, c='b')
    plt.show()


