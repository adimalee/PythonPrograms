# Name: Aditya Maleeswaran
# Assignment Name: Homework 1
# File Name: WordLadderProblemInformedSearch.py

from heapq import heappush, heappop
from string import ascii_lowercase as chars

class WordNeighbors(object):

  def __init__(self, words):
    self.words = words
    self.M = dict()                 # Neighbor words

  def variants(self, wd, words):
    wasl = list(wd)                 # Change word to a list
    for i, c in enumerate(wasl):
      for oc in chars:
        if c == oc: continue        # Skip if they are the same character
        wasl[i] = oc                # Replace the character
        ow = ''.join(wasl)
        if ow in words:             # Check if it is a valid word
          yield ow
      wasl[i] = c

  def __getitem__(self, wd):
    if wd not in self.M:
      self.M[wd] = dict.fromkeys(self.variants(wd, self.words), 1)
    return self.M[wd]

# heuristic function is the difference letters of 2 words.
  def heuristic(self, u, v):
    return sum(a!=b for a, b in zip(u, v))

  def ladder(self, s, t, h=None):
    if h is None:
      def h(v):
        return self.heuristic(v, t)

    _, P = a_star(self, s, t, h)
    if P is None:
      return [s, None, t]

    u, p = t, []
    while u is not None:
      p.append(u)
      u = P[u]

    p.reverse()
    return p

inf = float('inf')
global counter # How many words examined to find a path.

def a_star(graph, start, target, heuristic):
  counter = 0
  parents, queue = {}, [(heuristic(start), None, start)]
  while queue:
    counter += 1
    distance, parent, candidate = heappop(queue)
    if candidate in parents: continue
    parents[candidate] = parent
    if candidate == target:
      return distance - heuristic(target), parents
    for neighbor in graph[candidate]:
      weight = graph[candidate][neighbor] - heuristic(candidate) + heuristic(neighbor)
      heappush(queue, (distance + weight, candidate, neighbor))
  return inf, None

if __name__ == '__main__':
    wds = set(line.strip().lower() for line in open("Words.txt"))   # Enter dictionary filename
    G = WordNeighbors(wds)
    print G.ladder('fool', 'sage')      # Enter inputs with parameters startword and finishword

