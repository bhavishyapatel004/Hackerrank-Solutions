# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Problem     Check Strict Superset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-02, 07:23 p.m.
# ──────────────────────────────────────────────────

A=set(map(int,input().split()))
n=int(input())

result=True

for i in range(n):
    B=set(map(int,input().split()))
    
    if not A > B:
        result=False
        break
print(result)
