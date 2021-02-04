#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that return the number of subscribers from an Reddit API
    """
    header = {'User-Agent': 'Mozilla/5.0 Gecko/20100101 Firefox/84.0'}
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=header)
    subscribers = response.json().get("data").get("subscribers")
    if subscribers:
        return subscribers
    return 0
