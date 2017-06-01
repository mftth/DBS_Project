import csv, re

# Die 'american-election-tweets.csv'-Datei wird bereinigt indem 3 Spalten nicht in die 'election.csv'-Datei uebernommen werden

with open('american-election-tweets.csv',"rb") as source, open('election.csv',"wb") as result:
    rdr= csv.reader( source, delimiter=';' )
    wtr= csv.writer( result, delimiter=';' )

    for r in rdr:
       wtr.writerow( (r[0], r[1], r[2], r[3], r[4], r[6], r[7], r[8]) )


# Erstellt 'us.csv'-Datei, in der fuer jeden Tweet der User notiert ist
with open('election.csv',"rb") as f1, open('us.csv',"wb") as o1:
    read1= csv.reader( f1 , delimiter=';' )
    write1= csv.writer( o1 , delimiter=';' )

    for r in read1:
        if r[0] != "handle":
            write1.writerow( [r[0]])


# Erstellt die 'user.csv'-Datei (bereinigte 'us.csv'-Datei), die die beiden vorkommenden User angibt ohne Duplikate
with open('us.csv', "rb") as f8, open ('user.csv', "wb") as o8:
  seen = set()   # leere Liste, in der die schon gesehenen Handels aufgenommen werden
  for line in f8:
    if line in seen: # sollte der Handle schon enthalten sein, passiert nichts
      continue
    else: # andernfalls wird er in "seen" aufgenommen und in die 'user.csv'-Datei uebernommen
      seen.add(line)
      o8.write(line)



# Erstellt die 'tweet.csv'-Datei, in der alle benoetigten Attribute aus 'election.csv' uebernommen werden
with open('election.csv',"rb") as f2, open('tweet.csv',"wb") as o2:
    read2= csv.reader( f2 , delimiter=';' )
    write2= csv.writer( o2 , delimiter=';' )

    i = 1 # erhoeht sich mit jedem Tweet um ein -> Bildung der Tweet-ID
    for r in read2:
        if r[1] != "text":
          write2.writerow([i , r[1], r[3],r[7],r[5],r[2],r[6]])
          i= i+1


# Erstellt die 'postet.csv'-Datei, in der alle benoetigten Attribute aus 'election.csv' uebernommen werden
with open('election.csv',"rb") as f3, open('postet.csv',"wb") as o3:
    read3= csv.reader( f3 , delimiter=';' )
    write3= csv.writer( o3 , delimiter=';' )

    i = 1 # erhoeht sich mit jedem Tweet um ein -> Bildung der Tweet-ID
    for r in read3:
        if r[0] != "handle":
           write3.writerow([i,r[0], r[4]])
           i= i+1


# Erstellt 'text.csv', die nur den Text des Tweets enthaelt. Wird benoetigt spaeter bei der 'enthaelt.csv'-Datei
with open('election.csv',"rb") as f_text, open('text.csv',"wb") as r_text:
    read_text= csv.reader( f_text , delimiter=';' )
    write_text= csv.writer( r_text , delimiter=';' )

    for r in read_text:
        if r[1] != "text":
           write_text.writerow([r[1]])


# Erstellt die 'enthaelt.csv'-Datei, die aus 'text.csv' alle Hashtags als Attribut isoliert und dazu die 
# Tweet-ID's mitaufnimmt
with open('text.csv', "rb") as f4, open ('enthaelt.csv', "wb") as o4:
  read4 = csv.reader( f4, delimiter=';')
  write4 = csv.writer( o4, delimiter=';') 
  j = 1 # erhoeht sich mit jedem Tweet um ein -> Bildung der Tweet-ID
  for r in read4:
    j = j+1 # wird nur aufgenommen, wenn ein Tweet einen Hashtag enthaelt
    for st in range(len(r)): # iteriere durch jeden Tweet, die in Listen gespeichert sind
      s = ''.join(r) # wandelt die Listen in Strings um 
      h = [i  for i in s.split() if i.startswith("#") ] # speichert alle Hashtags eines Tweets in eine Liste
                                                        # sobald ein "#" entdeckt wird, wird der String an der Stelle gesplittet
      for i in range(len(h)):                           
        if "https" in h[i] : # uebernommene Links sollen entfernt werden
          continue
        else:
          h[i] = re.sub(r'[?|!|"|.|,|:|;|)|(|*|-|_]', r'', h[i])  # angegebene Sonderzeichen werden durch '' ersetzt
          write4.writerow([j, h[i].lower()])

          


# Erstellt die 'hash.csv'-Datei, in der alle Hashtags aus 'enthaelt.csv' uebernommen werden
with open('enthaelt.csv',"rb") as f6, open('hash.csv',"wb") as o6:
    read6= csv.reader( f6 , delimiter=';' )
    write6= csv.writer( o6 , delimiter=';' )

    for r in read6:
      write6.writerow( [r[1]])



# Erstellt die 'hashtags.csv'-Datei, in der alle (bereinigten) Hashtags aus 'hash.csv' uebernommen werden. 
# Enthaelt keine Duplikate 
with open('hash.csv', "rb") as f5, open ('hashtags.csv', "wb") as o5:
  seen = set() # leere Liste, in der die schon gesehenen Hashtags aufgenommen werden
  for line in f5:
    if line in seen: # sollte der Hashtag schon enthalten sein, passiert nichts
      continue
    else: # andernfalls wird er in "seen" aufgenommen und in die 'hashtags.csv'-Datei uebernommen
      seen.add(line)
      o5.write(line)






