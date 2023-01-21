import keys
import praw

reddit = praw.Reddit(
    client_id=keys.client_id,
    client_secret=keys.client_secret,
    user_agent=keys.user_agent,
)


def top_posts():
    return [i.title for i in reddit.subreddit('CryptoCurrency').hot(limit=10)]
