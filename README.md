# Twitter-dataset-generator

The purpose of this project is to create a dataset with tweets of certain twitter users. This dataset can be used for machine learning and similar projects. To overcome the 3200 tweets limit an existing dataset (https://www.reddit.com/r/datasets/comments/6fniik/over_one_million_tweets_collected_from_us/) is used and the most recent 3200 tweets are joinded to it. All accounts are taken from US politicians. To modify the account list take a look at the file accounts.

## Usage

Enter your Twitter API credentials into Downleaded/tweet_dumper.py. Then just run the script generateDataset.sh. You might also want to modify the accounts file. The number accounts in the final dataset is set in joinResults.py.
