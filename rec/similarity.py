from math import sqrt

def sim_distance(prefs, person1, person2):
  shared_items = {}
  for item in prefs[person1]:
    if item in prefs[person2]:
      shared_items[item] = 1

  if len(shared_items) == 0: return 0

  sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in shared_items])
  return 1 / (1 + sqrt(sum_of_squares))
