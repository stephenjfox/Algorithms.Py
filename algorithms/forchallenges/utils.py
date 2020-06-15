"""
Tools used for handling test input from standard-in, in a coding challenge
  environment like HackerRank or Google CodeJam.

* For a CodeJam 2019+ or a HackerRank-like environment, you would just copy-paste this code in.
* For something like CodeJam legacy, you're working locally anyway.
"""

from typing import List

def read_many_numerical() -> List[float]:
    return [float(x) for x in input().split()]

def read_inputs():
    n = int(input())
    values = read_many_numerical()

    return n, values
