import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'linux:tBitBjqxOF8PgmdkJhWtCgx19amSqw:v1.0.0 (by /u/professor07)',
        'Accept': 'application/json'
    }
    params = {
        'limit': 10  # Fetching 10 posts
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print("None")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
