import csv, re
import collections


with open('hash.csv', "rb") as f9 , open('anzahl.csv', "wb") as o9:
  read9= csv.reader( f9 , delimiter=';' )
  write9= csv.writer( o9 , delimiter=';' )
  hashtags = collections.defaultdict(int)
  for row in f9:
    hashtags[row] += 1  #zählt wie oft ein Hashtag verwendet wurde
  for row in hashtags.items():
    write9.writerow(row)
 
with open('anzahl.csv', "rb") as f10, open ('similar.csv', "wb") as o10:
  read10= csv.reader( f10 , delimiter=';' )
  write10= csv.writer( o10 , delimiter=';' )
  for row in read10:
      l = len(row[0])-2  #berechnet die Länge eines Hashtags
      write10.writerow([row[1],l]) 

    
    
    
    
    
    
    
    
