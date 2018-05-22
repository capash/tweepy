# tweepy
The repository contains:
1. python code to extract the twitter data for the hashtags - #NewYork, #LosAngeles, #SanFrancisco
2. Output.txt containing the JSON data for last 10 days
3. Config file containing the secrets
4. Final output Excl file with the field - user_handle | If post is retweet | Retweet count | Favourites | Hashtag used

Points to Ponder :

There are three levels of nesting and I could get to 2 levels for the "entities" field which has the "hashtags" details.
The data manipulation is done using pandas library.
