import praw
from textblob import TextBlob
import math


reddit = praw.Reddit(client_id='uifJuvRl06uxTg',
                     client_secret='Bf4eHDQhORvpJBw7syIvzat8gyA',
                     user_agent='subSentiment')

# opens file with subreddit names
with open('sb.txt') as f:

    for line in f:
        subreddit = reddit.subreddit(line.strip())

        #subreddit.submissions() has been removed from the API
        #sub_submissions = subreddit.submissions(day_start, day_end)
        sub_submissions = subreddit.search("coronavirus", time_filter = 'day')
        
        sub_sentiment = 0
        num_comments = 0

        for submission in sub_submissions:
            if not submission.stickied:
                submission.comments.replace_more(limit=0)
                for comment in submission.comments.list():
                        blob = TextBlob(comment.body)

                        #adds comment sentiment to overall sentiment for subreddit
                        comment_sentiment = blob.sentiment.polarity
                        sub_sentiment += comment_sentiment
                        num_comments += 1

                        #prints comment and polarity
                        #print(str(comment.body.encode('utf-8')) + ': ' + str(blob.sentiment.polarity))

        print('/r/' + str(subreddit.display_name))
        try:
            print('Ratio: ' + str(math.floor(sub_sentiment/num_comments*100)) + '\n')
        except:
            print('No comment sentiment.' + '\n')
            ZeroDivisionError

# add key:value subredditname:sentiment to dict
# order dictionary by sentiment value
# output dictionary key + ' sentiment: ' + sentiment value


