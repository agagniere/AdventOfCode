import sys

def sort_string(S):
    return ''.join(sorted(S))

def check_line(line):
    words = list(map(sort_string, line.split()))
    return len(words) == len(set(words))

print(sum(map(check_line, sys.stdin.readlines())))
