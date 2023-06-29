import snscrape.modules.twitter as st
import pandas as pd

query = 'etilang lang:id until:2023-06-30 since:2022-01-01'
tweets = []
limits = 1000

for tweet in st.TwitterSearchScraper(query).get_items():

    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# export
filename = 'tweets.csv'
df.to_csv(filename, index=False)

print(f"Dataframe exported to {filename} successfuly")
