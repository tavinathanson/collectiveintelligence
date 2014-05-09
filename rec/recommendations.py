from data import *
from similarity import *

"""
Returns the top n closest people in similarity to the argument person, mapped to
their similarity scores.
"""
def top_matches(prefs, person, n = 5, sim = sim_pearson):
    # Create a map of people to scores by calling similarity on all other people
    scores = [(sim(prefs, person, other), other) for other in prefs if other != person]
    scores.sort() # Sort by key
    scores.reverse()
    return scores[0:n]

"""
Returns all recommended movies (movies that person hasn't seen), sorted by
recommendation score (where critics with higher similarity have more weight in
determining the final score).
"""
def get_recommendations(prefs, person, sim = sim_pearson):
    totals = {}
    sim_sums = {}

    # Look at each critic
    for other in prefs:
      if other == person: continue # Skip same person
      sim_score = sim(prefs, person, other)
      if sim_score <= 0: continue # Skip 0 scores

      # Look at each of the critic's items, and multiply his rating by his similarity (e.g. weight)
      for item in prefs[other]:
        if item not in prefs[person] or prefs[person][item] == 0:
          totals.setdefault(item, 0)
          totals[item] += prefs[other][item] * sim_score
          sim_sums.setdefault(item, 0)
          sim_sums[item] += sim_score

    # Look at the item => total mapping, and turn that into a normalized total => item mapping
    rankings = [((total / sim_sums[item]), item) for item, total in totals.items()]
    rankings.sort() # Sort by key
    rankings.reverse()
    return rankings

"""
Flip item and person around in the prefs table.
"""
def transform_prefs(prefs):
  result = {}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item, {})

      # Flip item and person
      result[item][person] = prefs[person][item]
  return result
