# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
# Problem     Dot and Cross
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-16, 03:05 p.m.
# ──────────────────────────────────────────────────

import numpy

n=int(input())

A=numpy.array([input().split() for _ in range(n)],dtype=int)
B=numpy.array([input().split() for _ in range(n)],dtype=int)

print(numpy.dot(A,B))


