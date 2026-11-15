# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
# Problem     Mean, Var, and Std
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-15, 11:31 p.m.
# ──────────────────────────────────────────────────

import numpy

n,m=map(int,input().split())

me=numpy.array([input().split() for _ in range(n)],dtype=int)

print(numpy.mean(me,axis=1))
print(numpy.var(me,axis=0))
print(round(numpy.std(me), 11))

