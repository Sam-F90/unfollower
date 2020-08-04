import tweepy
import datetime
import os

# get keys from evironment variable "TWITTER_KEYS"
TWITTER_API_KEYS = (os.environ.get("TWITTER_KEYS").split(","))

consumer_key,consumer_secret,access_token_key,access_token_secret = TWITTER_API_KEYS

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

# establish api
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# verify
try:
    api.verify_credentials()
except:
    print("Error during authentication")
    exit()



# get my id
me = api.me()

# get list of friends (id)
friends = api.friends_ids(me.id)

# get list of followers (id)
follower_ids = []
for follower in tweepy.Cursor(api.followers, me.screen_name).items(api.me().friends_count):
    follower_ids.append(follower.id)

# get list of muted friends (id)
muted_friends = api.mutes_ids()

# create list of users who are muted and do not follow you
to_unfollow = []
for friend in friends:
    if friend not in follower_ids and friend in muted_friends:
        to_unfollow.append(friend)




# create log to record data and string to send to DM
log = [datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")]
dm = [datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")]

# unfollow useres in to_unfollow[] and record them in log[] and dm[]
for user in to_unfollow:
    # unfollowed = api.destroy_friendship(user)
    unfollowed = api.get_user(user)
    log.append('unfollowed ' + unfollowed.screen_name + " [" +str(unfollowed.friends_count) + "," + str(unfollowed.followers_count)  + "]")
    dm.append("@" + unfollowed.screen_name)

# write info to log
with open("unfollow_log.txt","a") as fp:
    for line in log:
        fp.write(line + "\n")
    fp.write("\n")

api.send_direct_message(api.me().id,"\n".join(dm))
print("finished")