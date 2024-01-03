from utils import lines
from enum import IntEnum, auto
from collections import defaultdict, namedtuple, deque
from math import prod

Pulse = namedtuple('Pulse', ['is_high', 'sender', 'recipient'])

#class Pulse(PulseBase):
#    def __str__(self):
#        return f'{self.sender} -{("low", "high")[self.is_high]}-> {self.recipient}'

class Module:

    def add_input(self, _):
        pass

class FlipFlop(Module):

    def __init__(self):
        self.is_on = False

    def receive(self, pulse: Pulse) -> None | bool:
        if pulse.is_high:
            return None
        self.is_on = not self.is_on
        return self.is_on

class Conjunction(Module):

    def __init__(self):
        self.memory = {}

    def add_input(self, name: str):
        self.memory[name] = False

    def receive(self, pulse: Pulse) -> bool:
        self.memory[pulse.sender] = pulse.is_high
        return not all(self.memory.values())

class Broadcast(Module):

    def receive(self, pulse: Pulse) -> bool:
        return pulse.is_high

class Output(Module):

    def receive(self, pulse: Pulse) -> None:
        pass


def parse(lines: list[str]) -> (dict[str, Module], dict[str, list[str]]):
    by_name = defaultdict(Output)
    topo = defaultdict(list)
    for line in lines:
        source, destinations = line.split(' -> ')
        name = ''.join(filter(str.isalpha, source))
        by_name[name] = {'%': FlipFlop, '&': Conjunction, 'b': Broadcast}[source[0]]()
        topo[name] += destinations.split(', ')
    for name, destinations in topo.items():
        for dest in destinations:
            by_name[dest].add_input(name)
    return by_name, topo

def press_button(modules: dict[str, Module], topology: dict[str, list[str]], times: int):
    count = defaultdict(int)
    for _ in range(times):
        fringe = deque([Pulse(is_high = False,
                              sender = 'button',
                              recipient = 'broadcaster')])
        while fringe:
            current = fringe.popleft()
            count[current.is_high] += 1
            to_send = modules[current.recipient].receive(current)
            if to_send is not None:
                fringe += [Pulse(sender=current.recipient,
                                 recipient = dest,
                                 is_high = to_send)
                           for dest in topology[current.recipient]]
        #print('-' * 40, end = '\n\n')
    print(f'Low : {count[False]:4}\nHigh: {count[True]:4}')
    return prod(count.values())

if __name__ == '__main__':
    print(press_button(*parse(lines()), 1000))
