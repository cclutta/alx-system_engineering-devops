#!/usr/bin/python3
"""
    function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.
"""
import requests

headers = {"User-Agent": "ubuntu:compaq"}


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        for children in res.json().get("data").get("children"):
            print(children.get("data").get("title"))
    else:
        print(None)
