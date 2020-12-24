import sys


class Constraint:
    def __init__(self, pairs):
        self.ranges = [range(int(lower), int(upper) + 1) for lower, upper in pairs]

    def __contains__(self, item):
        return True in [item in r for r in self.ranges]


def parse_ticket(string: str):
    return [int(field) for field in string.split(',')]


def is_ticket_valid(constraints):
    def inner(ticket):
        for field in ticket:
            if True not in [field in constraint for constraint in constraints]:
                return False
        return True
    return inner


def is_matching(x, tickets, constraint):
    for ticket in tickets:
        if not ticket[x] in constraint:
            return False
    return True


if __name__ == '__main__':
    with open('input.txt') as my_input_file:
        lines = my_input_file.read().splitlines()
        constraints = [Constraint([interval.split('-') for interval in line.split(': ')[1].split(' or ')]) for line in lines[:20]]
        mine = parse_ticket(lines[22])
        valid_tickets = list(filter(is_ticket_valid(constraints), map(parse_ticket, lines[25:]))) + [mine]
        is_matching_precomputed = [set([i for i in range(len(constraints)) if is_matching(col, valid_tickets, constraints[i])]) for col in range(len(constraints))]

        print(len(valid_tickets))

        count = 0
        def backtrack(mapping):
            global count
            count += 1
            col = len(mapping)
            if col == len(constraints):
                return mapping
            for i, constraint in enumerate(constraints):
                if i in is_matching_precomputed[col] and i not in mapping:
                    res = backtrack(mapping + [i])
                    if res:
                        return res
            return None

        mapping = backtrack([])
        print(count)
        inverse = {col:i for i, col in enumerate(mapping)}
        print(mapping)
        result = 1
        for i in range(6):
            result *= mine[inverse[i]]
        print(result)
