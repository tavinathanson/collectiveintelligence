from pydelicious import get_popular, get_userposts, get_urlposts
import time

"""
Gets 5 of the most popular links, and then creates empty dictionaries for each
user who posted one of those links.
"""
def initialize_user_dict(tag, count = 5):
  user_dict = {}
  for p1 in get_popular(tag = tag)[0:count]:
    for p2 in get_urlposts(p1['url']):
      user = p2['user']
      user_dict[user] = {}
  return user_dict

"""
Fill each element of the user dictionary with that user's links, giving
each link a "rating" of 1.0.
"""
def fill_items(user_dict):
  all_items = {}

  for user in user_dict:
    # Try 3 times to get the user's links
    for i in range(3):
      try:
        posts = get_userposts(user)
        break
      except:
        print "Failed user " + user + ", retrying"
        time.sleep(4)

    # Now that we have the user's links, add each link to the user's map of links and the total map
    for post in posts:
      url = post['url']
      user_dict[user][url] = 1.0
      all_items[url] = 1

  # For each rating set in user_dict (one per user), add 0 ratings for all the missing items
  for ratings in user_dict.values():
    for item in all_items:
      if item not in ratings:
        ratings[item] = 0.0
