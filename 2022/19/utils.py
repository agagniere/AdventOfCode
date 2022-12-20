from collections import deque, defaultdict

ORE      = 'ore'
CLAY     = 'clay'
OBSIDIAN = 'obsidian'
GEODE    = 'geode'

def add_dict(a, b):
    result = a.copy()
    for k,v in b.items():
        result[k] = v + result.get(k, 0)
    return result

def sub_dict(a, b):
    result = a.copy()
    for k,v in b.items():
        result[k] = result.get(k, 0) - v
    return result

class Recipe:
    def __init__(self, resource: str, costs: dict):
        self.resource = resource
        self.costs = costs

    def __str__(self):
        costs = ' and '.join(f'{c} {r}' for r, c in self.costs.items())
        return f'Each {self.resource} robot costs {costs}.'

    @classmethod
    def parse(cls, s: str):
        desc, cost = s.split(' costs ')
        return cls(desc.split()[1], {h.split()[1]: int(h.split()[0]) for h in cost.split(' and ')})

    def can_afford_with(self, have: dict):
        for res, count in self.costs.items():
            if count > have[res]:
                return False
        return True

class Blueprint:
    def __init__(self, index, recipes):
        self.index = int(index)
        self.recipes = list(recipes)

    def __str__(self):
        return '\n'.join([f'Blueprint {self.index}:'] + [f'\t{r}' for r in self.recipes])

    @classmethod
    def parse(cls, s: str):
        key, value = s.split(':')
        return cls(key.split()[1], map(Recipe.parse, value.split('.')[:-1]))

    def quality_level(self, max_minutes: int, max_robots: int) -> int:
        fringe = deque([(1,
                         add_dict(defaultdict(int), {ORE:1}),
                         add_dict(defaultdict(int), {ORE:1}))])
        best = 0
        max_ore = max(r.costs[ORE] for r in self.recipes)
        seen = 0
        while fringe:
            elapsed, robots, resources = fringe.popleft()
            seen += 1
            #print(f'After {elapsed} minutes, {dict(resources)}, with robots {dict(robots)}')
            if elapsed == max_minutes:
                #print(f'Finished with {dict(resources)}')
                best = max(best, resources[GEODE])
            else:
                if resources[ORE] < max_ore:
                    fringe += [(elapsed + 1,
                                robots,
                                add_dict(resources, robots))]
                for recipe in self.recipes:
                    if recipe.can_afford_with(resources) and robots[recipe.resource] < max_robots:
                        fringe += [(elapsed + 1,
                                    add_dict(robots, {recipe.resource: 1}),
                                    sub_dict(add_dict(resources, robots), recipe.costs))]
        print(seen)
        return best

def lines():
    while True:
        try:
            yield input()
        except:
            break

def parse(iterable) -> list:
    return list(map(Blueprint.parse, iterable))
