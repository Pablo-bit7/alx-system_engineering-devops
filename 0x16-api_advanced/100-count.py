#!/usr/bin/python3
"""
100-count.py - Recursive Reddit API query for keyword counts in hot articles
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses titles of hot articles,
    and counts occurrences of given keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to search for.
        after (str): The "after" token for pagination (used for recursion).
        word_count (dict): A dictionary to store keyword counts.

    Returns:
        None: Prints the results as specified in the task requirements.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    try:
        # Send the GET request to Reddit API
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')

            # Initialize word counts on the first recursion
            if not word_count:
                word_count = {word.lower(): 0 for word in word_list}

            # Loop through posts and count keywords in the title
            for post in posts:
                title = post['data']['title'].lower().split()
                for word in word_count.keys():
                    word_count[word] += title.count(word)

            # Recursion: if there is a next page, continue with after token
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                # After all recursion, sort and print the results
                sorted_count = sorted(
                    word_count.items(),
                    key=lambda kv: (-kv[1], kv[0])
                )
                for word, count in sorted_count:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return None
    except Exception:
        return None
