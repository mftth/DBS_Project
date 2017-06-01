import csv
import re


with open('american-election-tweets.csv',"rb") as source, open('election.csv',"wb") as result:
    rdr= csv.reader( source, delimiter=';' )
    wtr= csv.writer( result, delimiter=';' )

    for r in rdr:
       wtr.writerow( (r[0], r[1], r[2], r[3], r[4], r[6], r[7], r[8]) )


with open('election.csv',"rb") as f1, open('user.csv',"wb") as o1:
    read1= csv.reader( f1 , delimiter=';' )
    write1= csv.writer( o1 , delimiter=';' )

    write1.writerow(['screen_name'])

    for r in read1:
        if r[0] != "handle":
            write1.writerow( [r[0]])



with open('election.csv',"rb") as f2, open('tweet.csv',"wb") as o2:
    read2= csv.reader( f2 , delimiter=';' )
    write2= csv.writer( o2 , delimiter=';' )

    write2.writerow(['tweet_id','tweet_text','original_author','favorite_count','is_quote_status','is_retweet','retweet_count'])
    i = 1
    for r in read2:
        if r[1] != "text":
          write2.writerow((str(i),r[1], r[3],r[7],r[5],r[2],r[6]))
          i= i+1


with open('election.csv',"rb") as f3, open('postet.csv',"wb") as o3:
    read3= csv.reader( f3 , delimiter=';' )
    write3= csv.writer( o3 , delimiter=';' )

    write3.writerow(['tweet_id','screen_name','time'])
    i = 1
    for r in read3:
        if r[0] != "handle":
           write3.writerow((str(i),r[0], r[4]))
           i= i+1

with open('election.csv',"rb") as f_text, open('text.csv',"wb") as r_text:
    read_text= csv.reader( f_text , delimiter=';' )
    write_text= csv.writer( r_text , delimiter=';' )

    for r in read_text:
        if r[1] != "text":
           write_text.writerow([r[1]])


with open('text.csv', "rb") as f4, open ('enthaelt.csv', "wb") as o4:
  read4 = csv.reader( f4, delimiter=';')
  write4 = csv.writer( o4, delimiter=';') 
  
  write4.writerow(['tweet_id', 'hashtag_name']) 

  j = 1
  for r in read4:
    j = j+1
    for st in range(len(r)):
      s = ''.join(r)
      h = [i  for i in s.split() if i.startswith("#") ]
      for i in range(len(h)):
        if "https" in h[i] :
          continue
        else:
          h[i] = re.sub(r'[?|!|"|.|,|:|;|)|(|*|-|_]', r'', h[i])
          write4.writerow([str(j), h[i].lower()])
          

with open('enthaelt.csv',"rb") as f6, open('hash.csv',"wb") as o6:
    read6= csv.reader( f6 , delimiter=';' )
    write6= csv.writer( o6 , delimiter=';' )

    for r in read6:
      write6.writerow( [r[1]])



with open('hash.csv', "rb") as f5, open ('hashtags.csv', "wb") as o5:
  seen = set()
  for line in f5:
    if line in seen:
      continue
    else:
      seen.add(line)
      o5.write(line)
