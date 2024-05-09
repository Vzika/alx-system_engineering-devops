#!/usr/bin/python3
"""0-subs

Run ./0-main.py programming or ./0-main.py this_is_a_fake_subreddit for testing
"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent header to avoid getting blocked
    headers = {'User-Agent': 'CustomBot/1.0'}
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']
            
            # Return the number of subscribers
            return subscribers
        else:
            # Return 0 if the subreddit is invalid or there is an error
            return 0
    except Exception as e:
        # Handle any exceptions (e.g., network errors) and return 0
        print(f"An error occurred: {e}")
        return 0

