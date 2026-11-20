# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
# Problem     Linear Algebra
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-20, 10:55 p.m.
# ──────────────────────────────────────────────────

import numpy

n=int(input())
arr=numpy.array([input().split() for _ in range(n)],dtype=float)

print(round(numpy.linalg.det(arr),2))
