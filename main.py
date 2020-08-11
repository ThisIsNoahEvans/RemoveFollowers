import tweepy

screenname = str(input('Enter the username of the account you want to remove the followers of: '))

print('The consumer key must be of a Twitter developer account and the access key must be of the account you want to remove the followers of (they can be of the same account if you wish to remove the followers of your developer account).')
consumerKey = str(input('Enter your consumer key: '))
consumerSecret = str(input('Enter your consumer secret key: '))
accessKey = str(input('Enter your access key: '))
accessSecret = str(input('Enter your access secret key: '))

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


ids = []

print('Starting to remove followers. You\'ll see their Twitter user ID printed out when they have been blocked and unblocked.')
for page in tweepy.Cursor(api.followers_ids, screen_name=screenname).pages():
    ids.extend(page)

for user in ids:
    try:
        api.create_block(user)
        print('Blocked', user)
    except:
        print('There was an error blocking the user with ID', user)
        continue
    api.destroy_block(user)
    print('Unblocked', user)

print('Your followers should have been removed!')

