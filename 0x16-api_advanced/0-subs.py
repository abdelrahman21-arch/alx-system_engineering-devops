#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import json


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /u/Neat_Poet_3024)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        results = response.json().get("data")
        if results is None:
            return (0)
        return results.get("subscribers")
    except json.decoder.JSONDecodeError:
        print("Failed to decode JSON data from response")
        return 0
