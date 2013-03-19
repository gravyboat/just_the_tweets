#!/usr/bin/python3.2

import unittest
import os
import sys

sys.path.insert(0, '../')


testJsonData = {'follow_request_sent': None, 'profile_use_background_image': True, 'default_profile_image': False, 'id': 14159138, 'verified': False, 'profile_image_url_https': 'https://si0.twimg.com/profile_images/73450913/IMG_0202_normal.jpg', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'followers_count': 5223, 'profile_sidebar_border_color': 'C0DEED', 'id_str': '14159138', 'profile_background_color': 'C0DEED', 'listed_count': 346, 'status': {'lang': 'en', 'favorited': False, 'entities': {'user_mentions': [{'id': 15804774, 'indices': [13, 24], 'id_str': '15804774', 'screen_name': 'gvanrossum', 'name': 'Guido van Rossum'}], 'hashtags': [{'indices': [0, 6], 'text': 'pycon'}], 'urls': []}, 'contributors': None, 'truncated': False, 'text': '#pycon news: @gvanrossum giving a masterful technical talk on async io.  It is a plain spoken, clear exposition of the issues.', 'created_at': 'Sun Mar 17 16:35:32 +0000 2013', 'retweeted': False, 'in_reply_to_status_id_str': None, 'coordinates': None, 'in_reply_to_user_id_str': None, 'source': 'web', 'in_reply_to_status_id': None, 'in_reply_to_screen_name': None, 'id_str': '313327754735144960', 'place': None, 'retweet_count': 12, 'geo': None, 'id': 313327754735144960, 'in_reply_to_user_id': None}, 'profile_background_image_url_https': 'https://si0.twimg.com/images/themes/theme1/bg.png', 'utc_offset': -28800, 'statuses_count': 1308, 'description': 'Python core developer.\r\nFreelance programmer/consultant/trainer.\r\nHusband to Rachel.\r\nFather to Matthew.', 'friends_count': 158, 'location': 'Santa Clara, CA', 'profile_link_color': '0084B4', 'profile_image_url': 'http://a0.twimg.com/profile_images/73450913/IMG_0202_normal.jpg', 'following': None, 'geo_enabled': False, 'profile_background_image_url': 'http://a0.twimg.com/images/themes/theme1/bg.png', 'name': 'raymondh', 'lang': 'en', 'profile_background_tile': False, 'favourites_count': 5, 'screen_name': 'raymondh', 'notifications': None, 'url': 'http://rhettinger.wordpress.com', 'created_at': 'Sun Mar 16 20:12:52 +0000 2008', 'contributors_enabled': False, 'time_zone': 'Pacific Time (US & Canada)', 'protected': False, 'default_profile': True, 'is_translator': False}

class JustTheTweetsTestCase(unittest.TestCase):

    def setUp(self):
        self.JsonData = testJsonData

    def test_readTweets(self):
        from tweetScraper import tweetScraper
        tweetRead = tweetScraper()
        pulledTweet = tweetRead.pullTweet(self.JsonData)
        self.assertEqual(pulledTweet,
                         'raymondh: #pycon news: @gvanrossum giving a masterful technical talk on async io.  It is a plain spoken, clear exposition of the issues.', 'Strings do not match')


if __name__ == '__main__':
    unittest.main()
