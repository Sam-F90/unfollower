A script which uses the Twitter API and the python api library Tweepy to unfollow users that you have muted on Twitter.

I find this script is usedful if you are trying to grow your follower base by following users(and then muting them) in hopes that they will follow back.

At the end of the week you can run the script and it will automatically unfollow all those who never followed back. 




A log.txt file will be kept of every user you unfollowed and at what time, as well as their following-follower count.

The script will also send a dm to the user from the user's twitter account listing all the accounts unfollowed for easy access.


INSTRUCTIONS:
1. request an api account from twitter with access to reading/writing/direct messaging
2. save the keys given from twitter in your environment variables as
  \`TWITTER_KEYS = consumer_key,consumer_secret,access_token_key,access_token_secret`
3. install required modules using pipenv
4. run using `python unfollower.py`
