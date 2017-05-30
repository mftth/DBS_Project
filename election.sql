createdb election
psql -d election -U postgres
CREATE TABLE "User"(screenname CHAR(30));
CREATE TABLE "Hashtag"(hashtagname CHAR(30));
CREATE TABLE "Tweet"(tweettext CHAR(140), tweetid INT, favouritecount INT, retweetcount INT, originalauthor CHAR(20), truncated BOOLEAN, isquotestatus BOOLEAN, sourceurl CHAR(100), isretweet BOOLEAN, inreplytoscreenname BOOLEAN);
alter table "User" add primary key (screenname);
alter table "Tweet" add primary key (tweetid);
alter table "Hashtag" add primary key (hashtagname);
