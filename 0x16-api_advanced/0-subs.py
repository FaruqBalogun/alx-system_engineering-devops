params = {}
"""Fuction to query subscibers on a given Reddit subreddit.""""
import requests


def number_of_subscibers(subreddit):
        """Return the number of subscribers on a given subreddit."""
        url = "https://www.reddit.com/r//{}/about.json".format(subreddit)
        header = {
                "User-Agent": "linux:0xid.api.advanced:v1.0.0(by /u/bdov_)"
        }
        response  = requests.get(url, headers=headers, allow_redirection=False)
        if response.status_code == 404:
                return 0
        results = response.json().get("data")
        return results.get("subscribers")