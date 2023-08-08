#!/usr/bin/python3
"""Function that Queries Reddit API"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    user_agent = '0x16-api_advanced v1.0 (by /u/Droguemike)'
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        print("None")
        return

    data = response.json()
    posts = data['data']['children']
    for index, post in enumerate(posts):
        print(f"{post['data']['title']}")
