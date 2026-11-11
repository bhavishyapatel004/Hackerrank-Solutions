# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
# Problem     Sum and Prod
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-11, 09:19 p.m.
# ──────────────────────────────────────────────────

import numpy

n,m=map(int,input().split())

a=numpy.array([input().split() for _ in range (n)],dtype=int)

result=numpy.sum(a,axis=0)

print(numpy.prod(result))
