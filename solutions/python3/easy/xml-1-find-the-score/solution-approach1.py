# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true
# Problem     XML 1 - Find the Score
# Difficulty  Easy
# Subdomain   XML
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-22, 09:05 p.m.
# ──────────────────────────────────────────────────



import xml.etree.ElementTree as etree

def get_attr_number(node):
    total=len(node.attrib)
    
    for child in node:
        total+=get_attr_number(child)
        
    return total

