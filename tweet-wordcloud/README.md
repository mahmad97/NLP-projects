# tweet-wordcloud

User inputs a keyword and this program searches for tweets with that keyword using the Twitter v2 API.
Pulls 10,000 recent tweets, removes stopwords from them and then generates a wordcloud to show the most common words surrounding the keyword.

Need standard access to the Twitter v2 API for this to work. Add the Bearer Token (App-only) in the auth line and it should work.