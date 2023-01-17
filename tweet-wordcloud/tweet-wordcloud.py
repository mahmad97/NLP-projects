import tweepy
import re
import emoji
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Define the client using Bearer Token from twitter API v2 and connect to it
client = tweepy.Client('ADD BEARER TOKEN HERE')

# Get user input for the keyword
keyword = input('Enter the tweet search keyword: ')

# Define whitelist for characters we want in out wordcloud
whitelist = set('abcdefghijklmnopqrstuvwxyz \n')

# Get stopwords from stopwords.txt
f = open('stopwords.txt', 'r')
stopwords = f.read()
f.close()
stopwords = ''.join(filter(whitelist.__contains__, stopwords)).split()
stopwords.append('rt') # 'RT' shows up on all retweets and is too common

# Define frequency dict
wordFreq = {}

# Function to extract words from the tweets after filtering
def addTweetTokensToDict(tweetText):
  words = re.sub(r'http\S+', '', tweetText)
  words = emoji.replace_emoji(words, replace=' ')
  words = words.lower()
  words = ''.join(filter(whitelist.__contains__, words)).split()

  for word in words:
    if word not in stopwords:
      if word in wordFreq:
        wordFreq[word] = wordFreq[word] + 1
      else:
        wordFreq[word] = 1

# Make 100 calls to get 100 tweets each in a loop
nextToken = None
tweetsPerRequest = 100
for i in range(100):
  response = client.search_recent_tweets(query = f'{keyword} lang:en', max_results = tweetsPerRequest, next_token = nextToken)
  
  for tweet in response.data:
    addTweetTokensToDict(tweet.text)

  nextToken = response.meta['next_token']
  print('tweets pulled: ' + str((i + 1) * tweetsPerRequest))

# Generate wordcloud
wordcloud = WordCloud(background_color='white').generate_from_frequencies(wordFreq)

# Display wordcloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Output the wordcloud to jpg
wordcloud.to_file('wordcloud.jpg')
