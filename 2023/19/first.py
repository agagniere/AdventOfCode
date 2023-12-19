import re
from collections import namedtuple

from utils import lines

Part = namedtuple('Part', 'x m a s')

def create_condition(field: str, comparator: str, threshold: int, destination: str):
    comparison = {'<': threshold.__gt__,
                  '>': threshold.__lt__}[comparator]

    def test(part: Part) -> str | None:
        if comparison(getattr(part, field)):
            return destination
        return None

    return test

def create_workflow(instructions):
    default = None
    tests = []
    for instruction in instructions:
        if ':' in instruction:
            cond = re.match(r'(\w+)([<>])(\d+):(\w+)', instruction)
            tests.append(create_condition(cond[1], cond[2], int(cond[3]), cond[4]))
        else:
            default = instruction

    def workflow(part: Part):
        for test in tests:
            dest = test(part)
            if dest:
                return dest
        return default

    return workflow

def read_workflow(lines):
    result = {}
    for line in lines:
        if not line:
            break
        name, code = line.split('{')
        instructions = code[:-1].split(',')
        result[name] = create_workflow(instructions)
    return result

def read_parts(lines):
    for line in lines:
        as_dict = {}
        for field in line[1:-1].split(','):
            name, value = field.split('=')
            as_dict[name] = int(value)
        yield Part(**as_dict)

if __name__ == '__main__':

    workflows = read_workflow(lines())

    accepted = []
    workflows['R'] = lambda p: None
    workflows['A'] = lambda p: accepted.append(part)
    for part in read_parts(lines()):
        current = 'in'
        while current:
            current = workflows[current](part)
    print(f'There are {len(accepted)} accepted parts')
    print(sum(sum(a._asdict().values()) for a in accepted))
