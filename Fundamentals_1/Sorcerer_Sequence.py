import math
first_terms = [input() for i in range(int(input()))]

def sorcerer_sequence(first_term):
    sequence = [first_term]
    next_term = first_term
    while next_term > 1:
        if (next_term % 2 == 0):
            next_term = math.floor(next_term ** (1 / 2))
        else:
            next_term = math.floor(next_term ** (3 / 2))
        sequence.append(next_term)
    return sequence


for i in first_terms:
    print(*sorcerer_sequence(int(i)))

#     https://mycode.prepbytes.com/problems/fundamentals/JUGGLER
