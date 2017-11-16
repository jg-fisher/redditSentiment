from bs4 import BeautifulSoup
import requests

url = requests.get('https://redditmetrics.com/top')

soup = BeautifulSoup(url.text, 'html.parser')



with open('sb.txt', 'w') as f:
    for subreddit in soup.find_all('a'):
        try:
            if '/r' in subreddit.string:
                f.write(subreddit.string[3:] + '\n')
        except:
            TypeError

