# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
# Problem     Concatenate
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-02, 08:05 p.m.
# ──────────────────────────────────────────────────

import numpy

n,m,p=map(int,input().split())

arr1=numpy.array([input().split()for i in range(n)],int)
arr2=numpy.array([input().split()for i in range(m)],int)

print(numpy.concatenate((arr1,arr2),axis=0))
