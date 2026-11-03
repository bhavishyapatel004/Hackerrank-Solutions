# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
# Problem     Zeros and Ones
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-03, 09:37 p.m.
# ──────────────────────────────────────────────────

import numpy as np

n=tuple(map(int,input().split()))

print(np.zeros(n,dtype=int))
print(np.ones(n,dtype=int))



