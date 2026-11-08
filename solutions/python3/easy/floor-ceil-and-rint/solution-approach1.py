# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true
# Problem     Floor, Ceil and Rint
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 11:06 p.m.
# ──────────────────────────────────────────────────

import numpy
numpy.set_printoptions(legacy='1.13')

arr=numpy.array(input().split(),dtype=float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
