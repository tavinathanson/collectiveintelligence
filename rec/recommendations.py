from data import *
from similarity import *

"""
Returns the top n closest people in similarity to the argument person, mapped to
their similarity scores.
"""
def top_matches(prefs, person, n = 5, sim = sim_pearson):
    # Create a map of people to scores by calling similarity on all other people
    scores = [(sim(prefs, person, other), other) for other in prefs if other != person]

    # Sort (by key) in decreasing order, and return the top n
    scores.sort()
    scores.reverse()
    return scores[0:n]
