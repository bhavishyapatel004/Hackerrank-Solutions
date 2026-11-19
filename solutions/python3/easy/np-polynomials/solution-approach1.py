# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
# Problem     Polynomials
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-19, 06:45 p.m.
# ──────────────────────────────────────────────────

import numpy

p=list(map(float,input().split()))
x=float(input())

print(numpy.polyval(p,x))
