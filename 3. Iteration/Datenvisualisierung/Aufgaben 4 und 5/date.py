import csv, re
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
from pylab import*
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
 
 
with open('date.csv', "rb") as f13, open('hilfdate.csv', "wb") as o13:
  read13= csv.reader( f13 , delimiter=',' )
  next(read13, None)
  write13= csv.writer( o13 , delimiter=',' )
  for row in read13:
    r = row[2].split("T", 1)[0]   # entfernt die Uhrzeit aus der Spalte
    write13.writerow([row[0], row[1], r])
        
    
    
with open('hilfdate.csv', "rb") as f14, open('dump.csv', "rb") as f15, open('andate.csv', "wb") as o14:
  read14= csv.reader( f14 , delimiter=',' )
  next(read14, None)
  read15= csv.reader( f15 , delimiter=',' )
  next(read15, None)
  write14= csv.writer( o14 , delimiter=',' )
  liste1 = []  
  liste2 = []
  
  for row in read14:
    liste1.append((str(row[1]), str(row[2]))) # erstellt Liste 1 aus Tupeln aus den Spalten Hashtag und Datum mit Duplikaten
    
  for row in read15:
    liste2.append(str(row[0])) # erstellt Liste 2 aus der Spalte der Hashtags ohne Duplikate
  
  for r1 in range(0, len(liste2)):
    d = []
    for r2 in range(0, len(liste1)):  # wenn Hashtag aus Liste 1 gleich dem Hashtag aus Liste 2 ist, dann wird das Datum aus 
                                      # dem entsprechendem Tupel genommen
      if (liste2[r1] == liste1[r2][0]):
        d.append(liste1[r2][1])
    s = sorted(set(d), key=d.index)   # durch Erstellung eines sets, werden Duplikate der Daten entfernt
    l = len(s)                        # l entspricht die Anzahl der Tage, an dem der Hashtag liste2[r1] verwendet wurde
    write14.writerow([liste2[r1], l])
      
      
      
with open('andate.csv', "rb") as f16:
  read16 = csv.reader(f16, delimiter=',')
  dates = []
  hashtags =[]
  for row in read16:
    hashtags.append(row[0])        # Datum und Hashtag werden in Listen getan, die geplottet werden koennen
    dates.append(int(row[1]))    

  pos = arange(412)+.9
  plt.figure(figsize = (40,60))
  plt.barh(pos, dates, 0.2)
  plt.yticks(pos, hashtags)
  plt.ylim(0, 415)
  plt.xlabel('# Tage')
  plt.ylabel('Hashtags')
  plt.show()
  
  
  
with open('hilfdate.csv', "rb") as f17, open('auswahl.csv', "wb") as o17:
  read17= csv.reader( f17 , delimiter=',' )
  write17= csv.writer( o17 , delimiter=',' )
  l = []
  h = str(sys.argv[1])   #liest Hashtag aus dem Terminal ein
  for row in read17:
    r = str(row[1])
    if h in r:   # fuegt alle Daten in Liste l, bei denen der entsprechende Hashtag gleich h ist
      l.append(str(row[2]))
  s = sorted(set(l), key=l.index)  #Duplikate werden entfernt durch Erstellung eines Sets (das die Reihenfolge beibehaelt)
  #sl = list(s)
  for r1 in range(0, len(s)): # wenn Datum aus Liste l gleich dem Datum aus Liste s ist, dann wird das Datum mit 
                              # Duplikaten in Liste d geschrieben
    d = []
    for r2 in range(0, len(l)):
      if s[r1] == l[r2]:
        d.append(l[r2])
    n = len(d)                # n entspricht der Haeufigkeit vom Hashtag h an dem Datum s[r1]
    write17.writerow([s[r1], n])



with open('auswahl.csv', "rb") as f18:
  read18 = csv.reader(f18, delimiter=',')
  daten = []
  anzahl =[]
  for row in read18:
    daten.append(row[0])
    anzahl.append(int(row[1]))    # Datum und Anzahl vom Datum werden in Listen getan, die geplottet werden koennen
   
  D = OrderedDict(zip(daten, anzahl)) # die beiden Listen werden in ein geordnetes Dictionary eingefuegt
  D1 = OrderedDict(reversed(list(D.items()))) #chronologische Reihenfolge wird hergestellt
  plt.figure(figsize = (60,15))
  plt.bar(range(len(D1)), D1.values(), 0.2)
  plt.xticks(range(len(D1)), D1.keys(), rotation='vertical')
  plt.xlim(-5, 130)
  plt.xlabel('Datum')
  plt.ylabel('# Vorkommen vom Hashtag' + h)
  plt.show()









