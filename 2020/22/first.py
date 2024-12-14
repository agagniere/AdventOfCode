import sys
from collections import deque

def parse(lines):
    return list(map(int, lines.split('\n')[1:]))

def score(deck):
    return sum(c * (i+1) for i, c in enumerate(reversed(deck)))

if __name__ == '__main__':
    A, B = map(deque, map(parse, sys.stdin.read().strip().split('\n\n')))
    while A and B:
        play = A.popleft(), B.popleft()
        decks[play[1] > play[0]] += sorted(play, reverse=True)
    print("Winner: Player", 1 if decks[0] else 2)
    print(sum(map(score, decks)))
