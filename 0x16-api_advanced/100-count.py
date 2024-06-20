#!/usr/bin/python3
"""Module to query the Reddit API and count given keywords in the titles of hot articles recursively."""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """Counts occurrences of keywords in hot article titles of a subreddit."""
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0.0 (by /u/yourusername)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after, 'limit': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        after = data.get("after", None)
        children = data.get("children", [])

        for child in children:
            title = child.get("data", {}).get("title", "").lower().split()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] = counts.get(word_lower, 0) + title.count(word_lower)
        
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")

    except requests.RequestException:
        return

if __name__ == "__main__":
    pass
