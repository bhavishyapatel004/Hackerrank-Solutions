# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Problem     Capitalize!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-02, 07:08 p.m.
# ──────────────────────────────────────────────────


def solve(s):
    result = ' '.join(
        word[0].upper() + word[1:] if word else ''
        for word in s.split(' ')
    )
    return result





