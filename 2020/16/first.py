class Constraint:
    def __init__(self, pairs):
        self.ranges = [range(int(lower), int(upper) + 1) for lower, upper in pairs]

    def __contains__(self, item):
        return True in [item in r for r in self.ranges]


if __name__ == '__main__':
    with open('input.txt') as my_input_file:
        lines = my_input_file.read().splitlines()
        constraints = []
        for line in lines[:20]:
            key, value = line.split(': ')
            constraints += [Constraint([interval.split('-') for interval in value.split(' or ')])]
        result = 0
        for line in lines[25:]:
            for v in map(int, line.split(',')):
                if True not in [v in constraint for constraint in constraints]:
                    result += v
        print("Errors sum :", result)
