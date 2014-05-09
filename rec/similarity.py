from math import sqrt

"""
A method that returns the euclidean distance between person1 and person2.
"""
def sim_distance(prefs, person1, person2):
  shared_items = []
  for item in prefs[person1]:
    if item in prefs[person2]:
      shared_items.append(item)

  # If there are no shared items, then the distance is 0
  if len(shared_items) == 0: return 0

  sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in shared_items])
  return 1 / (1 + sqrt(sum_of_squares))
