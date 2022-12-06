def day6(length :int):
    def inner(line :str):
        for i in range(length, len(line)):
            if len(set(line[max(0, i - length):i])) == length:
                return i
    return inner
