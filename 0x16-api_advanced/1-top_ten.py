#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    return the first 10 hot posts listed
    """
    header = {'User-Agent': 'Mozilla/5.0 Gecko/20100101 Firefox/84.0'}
    try:
        response = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=header)
        hot_dict = response.json().get('data').get('children')
        # list of dictionaries
        limit = 0
        for dicts in hot_dict:
            if limit == 10:
                break
            print(dicts.get('data').get('title'))
            limit += 1
    except:
        print('None')
