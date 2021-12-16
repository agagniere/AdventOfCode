data = input()

def read_input():
    for c in data:
        v = int(c, base=16)
        for mask in [1 << p for p in range(4)[::-1]]:
            yield bool(v & mask)
next_bit = read_input()

def bits(n):
    v = 0
    for _, b in zip(range(n), next_bit):
        v <<= 1
        v += b
    return v

class Packet:
    def __init__(self, version):
        self.version = version
    def __str__(self):
        return f"(version {self.version})"

    @classmethod
    def parse_packet(cls):
        version = bits(3)
        type = bits(3)
        if type == 4:
            return Literal(version)
        else:
            return Operator(version)

class Literal(Packet):
    NOT_LAST = (1 << 4)
    DATA = 0xF

    def __init__(self, version):
        super().__init__(version)
        self.bytes = []
        while True:
            char = bits(5)
            self.bytes.append(char & Literal.DATA)
            if not char & Literal.NOT_LAST:
                break

    def sum(self):
        return self.version
    def __len__(self):
        return 6 + 5 * len(self.bytes)
    def __str__(self):
        return "Literal({}, {})".format(super().__str__(), self.bytes)

class Operator(Packet):
    BIT_LEN = 0
    PKG_LEN = 1

    def __init__(self, version):
        super().__init__(version)
        self.length_type_id = next(next_bit)
        self.length = bits(11) if self.length_type_id == Operator.PKG_LEN else bits(15)
        self.sub = []
        if self.length_type_id == Operator.PKG_LEN:
            for _ in range(self.length):
                self.sub.append(Packet.parse_packet())
        else:
            rem = self.length
            while rem > 0:
                self.sub.append(Packet.parse_packet())
                rem -= len(self.sub[-1])

    def sum(self):
        return self.version + sum([ s.sum() for s in self.sub ] )
    def __len__(self):
        return 7 + [15, 11][self.length_type_id] + (sum(map(len, self.sub)) if self.length_type_id == Operator.PKG_LEN else self.length)
    def __str__(self):
        return "Operator({}, {} {})".format(super().__str__(), self.length, ["bits", "packages"][self.length_type_id == Operator.PKG_LEN]) + "\n{\n\t" + '\n\t'.join(map(str, self.sub)) + "\n}\n"

print(Packet.parse_packet().sum())
