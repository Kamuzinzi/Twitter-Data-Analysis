import unittest
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join("../Twitter-Data-Analysis/")))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below
sampletweetsjsonfile = "sample/sampletweets.json"   #put here the path to where you placed the file e.g. ./sampletweets.json. 
_, tweet_list = read_json(sampletweetsjsonfile)

columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place",
    "place_coord_boundaries",
]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        tweet_df = self.df.get_tweet_df()
        return tweet_df

    def test_find_statuses_count(self):
        self.assertEqual(
            # self.df.find_statuses_count(), <provide a list of the first five status counts>
            self.df.find_statuses_count(), [8097, 5831, 1627, 1627, 48483]
        )

    def test_find_full_text(self):
        # text = <provide a list of the first five full texts>

        text = [
"RT @i_ameztoy: Extra random image (I):\n\nLets focus in one very specific zone of the western coast -&gt; Longjing District, Taichung #City, #Ta\u2026",
"RT @IndoPac_Info: #China's media explains the military reasons for each area of the drills in the #Taiwan Strait\n\nRead the labels in the pi\u2026",
"China even cut off communication, they don't anwer phonecalls from the US. But here clown @ZelenskyyUa enters the stage to ask #XiJinping to change Putin's mind.", 
"Putin to #XiJinping : I told you my friend, Taiwan will be a vassal state, including nukes, much like the Ukrainian model. I warned you... But it took Pelosi to open China's eyes.",
"RT @benedictrogers: We must not let this happen.\n\nWe must be ready.\n\nWe must defend #Taiwan\n\nhttps://t.co/z4Rv925jhI",]
# "RT @TGTM_Official: What kind of country can connive such extremely offensive remarks on the street?\n\n#Taiwan #TsaiIngwen\n#TheGreatTranslati\u2026"]
        self.assertEqual(self.df.find_full_text(), text)

    def test_find_sentiments(self):
        self.assertEqual(
            self.df.find_sentiments(self.df.find_full_text()),
            ([-0.125, -0.1, 0, 0.1, 0.2],[0.190625, 0.1, 0.0, 0.35, 0.5])

            # (
            #     <provide a list of the first five sentiment values>,
            #     <provide a list of the first five polarity values>,
            # ),
        )


    def test_find_screen_name(self):
        # name = <provide a list of the first five screen names>
        name = ["i_ameztoy", 'ZIisq', 'Fin21Free', 'Fin21Free', 'GraceCh15554845']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        # f_count = <provide a list of the first five follower counts>
        f_count = [20497, 65, 85, 85, 207]

        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        # friends_count = <provide a list of the first five friend's counts>
        friends_count = [2621, 272, 392, 392, 54]

        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
    # <provide a list of the first five is_sensitive values>)
        self.assertEqual(self.df.is_sensitive(), [None,None,None,None,False])


    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), 
        # [ {'text': 'City', 'indices': [132, 137]},
        # {'text': 'China', 'indices': [18, 24]},
        # {'text': 'Taiwan', 'indices': [98, 105]},
        # {'text': 'XiJinping', 'indices': [127, 137]},
        # {'text': 'XiJinping', 'indices': [9, 19]} ])

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )



if __name__ == "__main__":
    unittest.main()

