#!/usr/bin/python3
"""Module to query the Reddit API and return all hot posts titles recursively for a given subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts for a given subreddit recursively."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0.0 (by /u/yourusername)'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            hot_list.extend([post.get("data", {}).get("title", None) for post in children])
            after = data.get("after", None)
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None

if __name__ == '__main__':
    pass
