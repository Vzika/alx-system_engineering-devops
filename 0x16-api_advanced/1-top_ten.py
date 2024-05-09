import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'CustomBot/1.0'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                print("Titles of the first 10 hot posts in r/{}:".format(subreddit))
                for post in data['data']['children']:
                    print(post['data']['title'])
            else:
                print("None")
        else:
            print("None")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("None")
