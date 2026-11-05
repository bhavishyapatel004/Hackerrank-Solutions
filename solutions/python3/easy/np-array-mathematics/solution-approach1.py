# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
# Problem     Array Mathematics
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-05, 09:36 p.m.
# ──────────────────────────────────────────────────

import numpy

n,m=map(int,input().split())
a=numpy.array([input().split() for _ in range (n)],dtype=int)
b=numpy.array([input().split() for _ in range (n)],dtype=int)

print (numpy.add(a,b))
print (numpy.subtract(a,b))
print (numpy.multiply(a,b))
print (numpy.floor_divide(a,b))
print (numpy.mod(a,b))
print (numpy.power(a,b))
