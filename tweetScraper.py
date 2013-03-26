#!/usr/bin/python3.2

import urllib.request
import json
import argparse

class tweetScraper(object):

    def queryTwitterUserDatabase(self, twitterDatabase = 'twitterUsers.db'):
        pass

    def createJsonData(self, twitterHandles):
        self.twitterHandles = twitterHandles
        jsonList = []

        for handle in self.twitterHandles:
            twitterUserUrl = 'https://api.twitter.com/1/users/show.json?screen_name={0}&include_entities=true'.format(handle)
            jsonTweetData = urllib.request.urlopen(twitterUserUrl)
            readTweetData = jsonTweetData.readall().decode('utf-8')
            formattedJsonTweet = json.loads(readTweetData)
            jsonList.append(formattedJsonTweet)

        return(jsonList)

    def pullTweet(self, jsonTweetList):
        self.jsonTweetList = jsonTweetList
        tweetList = []

        for jsonTweet in self.jsonTweetList:
            tweetList.append(jsonTweet['screen_name'] + ': ' + jsonTweet['status']['text'])
        return(tweetList)


parser = argparse.ArgumentParser(description='Choose how a user wishes to interact.')
parser.add_argument('-u', '--user', dest='twitterUser', type=str, help='Choose which Twitter user you would like to query.')
args = parser.parse_args()
if args.twitterUser:
    twitterHandle = [args.twitterUser]

if __name__ == '__main__':
    tweetScrape = tweetScraper()
    handleId = ['gvanrossum', 'raymondh']
    twitterJson = tweetScrape.createJsonData(twitterHandle)
    print(tweetScrape.pullTweet(twitterJson))
