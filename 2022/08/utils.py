from math import prod
import sys

def store_forest():
    return [list(map(int, line.strip())) for line in sys.stdin.readlines()]

def columns(forest :list):
    return [[row[i] for row in forest] for i in range(len(forest[0]))]

def visible_trees(forest :list, reverse :bool):
    result = set()
    prev_heights = [-1 for _ in forest[0]]
    for y, row in list(enumerate(forest))[::-1 if reverse else 1]:
        current = -1
        for x, tree in list(enumerate(row))[::-1 if reverse else 1]:
            if tree > prev_heights[x]:
                result.add( (x, y) )
                prev_heights[x] = tree
            if tree > current:
                result.add( (x, y) )
                current = tree
    return result

def scenic_score(x, y, row, column):
    def single(p, line):
        current = line[p]
        score = 0
        while p > 0:
            p -= 1
            score += 1
            if line[p] >= current:
                break
        return score
    def reverse(p, line):
        return single(len(line) - p - 1, line[::-1])
    return prod([single(x, row), single(y, column), reverse(x, row), reverse(y, column)])
