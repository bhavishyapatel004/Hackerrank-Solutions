# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
# Problem     Shape and Reshape
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-02, 07:46 p.m.
# ──────────────────────────────────────────────────

import numpy

my_array=numpy.array(input().split(),int)
my_array= numpy.reshape(my_array,(3,3))

print(my_array)

