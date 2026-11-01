# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Problem     Designer Door Mat
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-01, 07:11 p.m.
# ──────────────────────────────────────────────────

n,m=map(int,input().split())

#upper part
for i in range (1,n,2):
    pattern=".|."*i
    print(pattern.center(m,'-'))
    
#middle part
print("WELCOME".center(m,'-'))

#lower part
for i in range (n-2,0,-2):
    pattern=".|."*i
    print(pattern.center(m,'-'))
