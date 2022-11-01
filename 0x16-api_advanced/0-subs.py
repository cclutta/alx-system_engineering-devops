#!/usr/bin/python3
"""
    function that queries the Reddit API and returns
    the number of subscribers for a given subreddit.
"""
import requests

headers = {"User-Agent": "ubuntu:compaq"}


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    else:
        return 0
