# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true
# Problem     Eye and Identity
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-04, 09:55 p.m.
# ──────────────────────────────────────────────────

import numpy as np
np.set_printoptions(legacy='1.13')

n,m=map(int,input().split())

print(np.eye(n,m))


