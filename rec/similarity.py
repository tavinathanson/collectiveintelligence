from math import sqrt

"""
Returns the euclidean distance between person1 and person2.
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

"""
Returns the Pearson correlation between person1 and person2.
"""
def sim_pearson(prefs, person1, person2):
  shared_items = []
  for item in prefs[person1]:
    if item in prefs[person2]:
      shared_items.append(item)

  n = len(shared_items)

  # If there are no shared items, then the correlation is 0
  if n == 0: return 0

  # Add up the preferences
  sum1 = sum([prefs[person1][item] for item in shared_items])
  sum2 = sum([prefs[person2][item] for item in shared_items])

  # Sum up the squares
  sum1_squared = sum([pow(prefs[person1][item], 2) for item in shared_items])
  sum2_squared = sum([pow(prefs[person2][item], 2) for item in shared_items])

  # Sum up the products
  product_sum = sum([prefs[person1][item] * prefs[person2][item] for item in shared_items])

  # Calculate Pearson
  num = product_sum - ((sum1 * sum2) / n)
  denom = sqrt((sum1_squared - (pow(sum1, 2) / n)) * (sum2_squared - (pow(sum2, 2) / n)))
  if denom == 0: return 0
  return num / denom
