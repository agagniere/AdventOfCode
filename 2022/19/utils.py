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
        fringe = deque([(0,
                         add_dict(defaultdict(int), {ORE:1}),
                         defaultdict(int))])
        best = 0
        max_ore = max(r.costs[ORE] for r in self.recipes[1:])
        seen = set()
        count = 0
        while fringe:
            elapsed, robots, resources = fringe.popleft()
            count += 1
            best = max(best, resources[GEODE] + (elapsed - max_minutes) * robots[GEODE])
            #print(f'After {elapsed} minutes, {dict(resources)}, with robots {dict(robots)}: {best}')
            for recipe in self.recipes:
                if robots[recipe.resource] >= max_robots or (recipe.resource == ORE and robots[recipe.resource] >= max_ore):
                    continue
                can_wait = True
                for res, count in recipe.costs.items():
                    if robots[res] < 1:
                        can_wait = False
                        break
                if can_wait:
                    next_elapsed = elapsed + 1
                    next_resources = resources.copy()
                    while not recipe.can_afford_with(next_resources):
                        next_resources = add_dict(next_resources, robots)
                        next_elapsed += 1
                    next_robots = add_dict(robots, {recipe.resource: 1})
                    next_resources = sub_dict(next_resources, recipe.costs)
                    next_resources = add_dict(next_resources, robots)
                    if next_elapsed < max_minutes:
                        fringe.append( (next_elapsed, next_robots, next_resources) )
        print(f'{len(seen):10}, {count:10}')
        return best

def lines():
    while True:
        try:
            yield input()
        except:
            break

def parse(iterable) -> list:
    return list(map(Blueprint.parse, iterable))
