#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    return the hot list using recursive function
    """
    try:
        response = requests.get(
            'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
                subreddit, after), headers={
                    'User-Agent': 'Mozilla/5.0 Gecko/20100101 Firefox/84.0'})
        response_json = response.json()
        list_dicts = response_json.get('data').get('children')
        after = response_json.get('data').get('after')
        for i in range(len(list_dicts)):
            hot_list.append(list_dicts[i].get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except:
        return None
