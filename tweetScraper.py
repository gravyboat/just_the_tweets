#!/usr/bin/python3.2

import urllib.request
import json
import argparse

class tweetScraper(object):

    def queryTwitterUserDatabase(self, twitterDatabase= 'twitterUsers.db')
    def createJsonData(self, twitterHandle):
        self.twitterHandle = twitterHandle

        twitterUserUrl = 'https://api.twitter.com/1/users/show.json?screen_name={0}&include_entities=true'.format(self.twitterHandle)
        jsonTweetData = urllib.request.urlopen(twitterUserUrl)
        readTweetData = jsonTweetData.readall().decode('utf-8')
        formattedJsonTweet = json.loads(readTweetData)
        return(formattedJsonTweet)

    def pullTweet(self, tweetJson):
        self.tweetJson = tweetJson

        return(self.tweetJson['screen_name'] + ': ' + self.tweetJson['status']['text'])


parser = argparse.ArgumentParser(description='Choose how a user wishes to interact.')
parser.add_argument('-u', '--user', dest='twitterUser', type=str, help='Choose which Twitter user you would like to query.')
args = parser.parse_args()
if args.twitterUser:
    twitterHandle = args.twitterUser

if __name__ == '__main__':
    tweetScrape = tweetScraper()
    twitterJson = tweetScrape.createJsonData(twitterHandle)
    print(tweetScrape.pullTweet(twitterJson))
