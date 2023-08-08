#!/usr/bin/python3
"""Function that Queries Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = '0x16-api_advanced v1.0 (by /u/Droguemike)'
    headers = {'User-Agent': user_agent}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for index, post in enumerate(posts):
            title = post['data']['title']
            hot_list.append(title)

        if 'after' in data['data'] and data['data']['after'] is not None:
            after = data['data']['after']
            recurse(subreddit, hot_list=hot_list, after=after)

    else:
        return None
    return hot_list
