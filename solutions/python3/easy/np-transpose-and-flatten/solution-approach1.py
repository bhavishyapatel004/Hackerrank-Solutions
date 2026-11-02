# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
# Problem     Transpose and Flatten
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-02, 07:58 p.m.
# ──────────────────────────────────────────────────

import numpy

n, m = map(int, input().split())

arr = numpy.array([input().split() for i in range(n)], int)

print(numpy.transpose(arr))
print(arr.flatten())
