import sys
from collections import deque
from first import parse, score

Player1 = 0
Player2 = 1

def myhash(A, B):
    return tuple(A + ['|'] + B)

def recursive_combat(A, B):
    seen = set()
    while A and B:
        if myhash(A, B) in seen:
            return Player1, None
        seen.add(myhash(A, B))
        a, b = A.pop(0), B.pop(0)
        if len(A) >= a and len(B) >= b:
            round_winner, _ = recursive_combat(A[:a], B[:b])
        else:
            round_winner = b > a
        if round_winner == Player1:
            A += [a, b]
        else:
            B += [b, a]
    return Player1 if A else Player2, A if A else B

A,B = map(parse, sys.stdin.read().strip().split('\n\n'))
winner, deck = recursive_combat(A, B)

print("Winner: Player", winner + 1)
print(score(deck))
