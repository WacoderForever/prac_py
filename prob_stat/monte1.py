import numpy as np
#   using default number generator
rng = np.random.default_rng()

def random_in_square():
#Returns a random position in the square [-1,1)x[-1,1).
    return rng.uniform(low=[-1,-1],high=[1,1])

def is_in_circle(x):
    return np.dot(x,x) < 1

def simulate_number_of_hits(N):
## Simulates number of hits in case of N trials in the pebble game."""
    number_hits = 0
    for i in range(N):
        position = random_in_square()
        if is_in_circle(position):
            number_hits += 1
    return number_hits

trials = 4000
hits = simulate_number_of_hits(trials)
print(hits , "hits, estimate of pi =", 4 * hits / trials )