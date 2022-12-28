import keys
import praw

reddit = praw.Reddit(
    client_id=keys.client_id,
    client_secret=keys.client_secret,
    user_agent=keys.user_agent,
)

hot_posts = reddit.subreddit('CryptoCurrency').hot(limit=10)
for post in hot_posts:
    print(post.title)
