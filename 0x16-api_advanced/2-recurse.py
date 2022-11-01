#!/usr/bin/python3
"""
    recursive function that queries the Reddit API and prints the
    titles of all hot articles for a given subreddit.
"""
import requests

headers = {"User-Agent": "ubuntu:compaq"}


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json?after={}"\
          .format(subreddit, after)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        for children in res.json().get("data").get("children"):
            hot_list.append(children.get("data").get("title"))

        after = res.json().get("data").get("after")
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)

    else:
        return None
