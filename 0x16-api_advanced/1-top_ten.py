#!/usr/bin/python3
""" Funtion to print hot posts on a given Reddit subreddit	"""
 import requests
 
 
 def top_ten(subreddit):
     """ Print the titles of the 10 hottest posts ona given subreddit  """
     url = "https://www.reddit.com/r//{}/about.json".format(subreddit)
     headers = {
             "user-agent": "linux 0x16. api.advanced:v1.0.0 (by /u/bdov_)"
             }
     params = {
             "limit": 10
             }
     response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
     if response.status_code == 404:
         print("None")
         return
     results = response.json().get("title")) for c in results.get("children")
