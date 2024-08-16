#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return the
titles of all hot posts for a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot posts for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): The list of hot post titles (used for recursion).
        after (str): The "after" token for pagination (used for recursion).

    Returns:
        list: A list of titles of all hot posts for the subreddit, or None if
        invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')

            if not posts:
                return hot_list if hot_list else None

            hot_list.extend([post['data']['title'] for post in posts])

            # If there is a next page, continue recursion with the after token
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception:
        return None
