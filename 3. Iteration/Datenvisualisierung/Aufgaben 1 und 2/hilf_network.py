import csv, re

# pair_hashs.csv : Tabelle mit 2 Spalten (hashtag_name,hashtag_name)
#               --> ueber SQL-Abfrage bei phpPgAdmin erhalten und heruntergeladen

# erstelle nun eine Tabelle (node.csv), wo die zwei Spalten unterschiedliche Hashtags
# haben oder die 1.Spalte gefuellt ist und die 2.Spalte leer
# --> 1.Fall: es wird spaeter im Graphen eine Kante zwischen den 2 Hashtags gezeichnet
# --> 2.Fall: der Hashtag aus Spalte 1 ist nur ein Punkt im Graphen ohne ausgehende Kanten

# node.csv wird dann in gephi als Graph-Datei eingefuegt/ eingelesen

with open('pair_hashs.csv', "rb") as f, open ('node.csv', "wb") as o:
  read1= csv.reader( f , delimiter=',' )
  write1= csv.writer( o , delimiter=',' )
  
  for r in read1:
        if r[0] == "hashtag_name":
            continue
        elif r[0]!=r[1]:
            write1.writerow( [r[0],r[1]])
        else:
            write1.writerow([r[0]])


