COPY "public"."ENTHAELT" FROM '/tmp/enthaelt.csv' DELIMITER ';' CSV ENCODING 'WIN1252';
COPY "public"."HASHTAG" FROM '/tmp/hashtags.csv' DELIMITER ';' CSV ENCODING 'WIN1252';
COPY "public"."POSTET" FROM '/tmp/postet.csv' DELIMITER ';' CSV ENCODING 'WIN1252';
COPY "public"."TWEET" FROM '/tmp/tweet.csv' DELIMITER ';' CSV ENCODING 'WIN1252';
COPY "public"."USER" FROM '/tmp/user.csv' DELIMITER ';' CSV ENCODING 'WIN1252';

