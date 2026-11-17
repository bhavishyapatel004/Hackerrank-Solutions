# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
# Problem     Inner and Outer
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-17, 11:09 p.m.
# ──────────────────────────────────────────────────

import numpy



A=numpy.array(input().split(),dtype=int)
B=numpy.array(input().split(),dtype=int)

print(numpy.inner(A,B))
print(numpy.outer(A,B))
