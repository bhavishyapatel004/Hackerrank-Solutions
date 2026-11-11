# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# Problem     Min and Max
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-11, 09:27 p.m.
# ──────────────────────────────────────────────────

import numpy

n,m=map(int,input().split())

arr=numpy.array([input().split() for _ in range(n)],dtype=int)

minn=numpy.min(arr,axis=1)

maxx=numpy.max(minn)

print(maxx)


