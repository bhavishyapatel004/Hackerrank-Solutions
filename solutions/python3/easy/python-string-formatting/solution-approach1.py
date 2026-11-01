# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-01, 07:36 p.m.
# ──────────────────────────────────────────────────

def print_formatted(number):
    width= len (bin(number)[2:])

    for i in range(1,number + 1):
        decimal=str(i)
        octal=oct(i)[2:]
        hexadecimal=hex(i)[2:].upper()
        binary=bin(i)[2:]
    
        print(decimal.rjust(width),
              octal.rjust(width),
              hexadecimal.rjust(width),
              binary.rjust(width))
