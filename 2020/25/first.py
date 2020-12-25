class EndPoint:
    INITIAL = 7
    MAX = 20201227

    def __init__(self, public_key):
        self.publicKey = public_key
        self.secret = 0
        value = 1
        while value != public_key:
            self.secret += 1
            value = (value * EndPoint.INITIAL) % EndPoint.MAX
        print("Found a secret loop of", self.secret)

    def handshake(self, other_key):
        value = 1
        for _ in range(self.secret):
            value = (value * other_key) % EndPoint.MAX
        return value


sample_card = EndPoint(5764801)
sample_door = EndPoint(17807724)
print(sample_card.handshake(sample_door.publicKey))
print(sample_door.handshake(sample_card.publicKey))

card = EndPoint(18499292)
door = EndPoint(8790390)
print(card.handshake(door.publicKey))
print(door.handshake(card.publicKey))
