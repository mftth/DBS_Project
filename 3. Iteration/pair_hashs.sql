SELECT E.hashtag_name, F.hashtag_name
FROM "ENTHAELT" E, "ENTHAELT" F
WHERE E.tweet_id = F.tweet_id
