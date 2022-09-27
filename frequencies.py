"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    itemsCount = [str(i) for i in items]
    keys = list(set(items))
    for key in keys:
        frequencies[str(key)] = itemsCount.count(str(key))
    return frequencies

#print(frequencies([100, 'Hello', '100', '100', 100]))


