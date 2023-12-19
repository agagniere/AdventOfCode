import re
from collections import namedtuple
from math import prod

from first import Part
from utils import lines

Condition = namedtuple('Condition', ['field', 'comparator', 'threshold', 'destination'])

def create_workflow(instructions):
    tests = []
    for instruction in instructions:
        if ':' in instruction:
            cond = re.match(r'(\w+)([<>])(\d+):(\w+)', instruction)
            tests.append(Condition(field = cond[1],
                                   comparator = cond[2],
                                   threshold = int(cond[3]),
                                   destination = cond[4]))
        else:
            return tests, instruction

def read_workflow(lines):
    result = {}
    for line in lines:
        if not line:
            break
        name, code = line.split('{')
        instructions = code[:-1].split(',')
        result[name] = create_workflow(instructions)
    return result

if __name__ == '__main__':

    workflows = read_workflow(lines())

    def explore(workflow, bounds):
        if workflow == 'R':
            return 0
        if workflow == 'A':
            return prod(len(field_range) for field_range in bounds)
        result = 0
        conditions, default = workflows[workflow]
        for condition in conditions:
            current_range = getattr(bounds, condition.field)
            if condition.comparator == '<':
                if current_range.stop <= condition.threshold:
                    return explore(condition.destination, bounds)
                elif condition.threshold <= current_range.start:
                    continue
                new_bounds = bounds._asdict()
                new_bounds[condition.field] = range(getattr(bounds, condition.field).start, condition.threshold)
                result += explore(condition.destination, Part(**new_bounds))
                new_bounds[condition.field] = range(condition.threshold, getattr(bounds, condition.field).stop)
                bounds = Part(**new_bounds)
            elif condition.comparator == '>':
                if current_range.start > condition.threshold:
                    return explore(condition.destination, bounds)
                elif condition.threshold >= current_range.stop - 1:
                    break
                new_bounds = bounds._asdict()
                new_bounds[condition.field] = range(condition.threshold + 1, getattr(bounds, condition.field).stop)
                result += explore(condition.destination, Part(**new_bounds))
                new_bounds[condition.field] = range(getattr(bounds, condition.field).start, condition.threshold + 1)
                bounds = Part(**new_bounds)
        return result + explore(default, bounds)

    print(explore('in', Part(*([range(1, 4001)] * 4))))
