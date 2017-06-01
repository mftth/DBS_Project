create table "ENTHAELT"(tweet_id INT, hashtag_name CHAR(30));
create table "HASHTAG"(hashtag_name CHAR(30));
create table"POSTET"(tweet_id INT, screen_name CHAR(30), time CHAR(25));
create table "TWEET"(tweet_id INT, tweet_text CHAR(300), original_author CHAR(20), favourite_count INT, in_reply_to_screen_name CHAR(20), is_quote_status BOOLEAN, is_retweet BOOLEAN, retweet_count INT, truncated BOOLEAN, source_url CHAR(100));
create table "USER"(screen_name CHAR(30));
alter table "USER" add primary key (screen_name);
alter table "TWEET" add primary key (tweet_id);
alter table "HASHTAG" add primary key (hashtag_name);
alter table "ENTHAELT" add primary key (tweet_id, hashtag_name);
alter table "POSTET" add primary key (tweet_id);

alter table "TWEET" DROP COLUMN in_reply_to_screen_name, DROP COLUMN truncated, DROP COLUMN source_url;
