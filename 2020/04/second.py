import re

check = {
    "byr":(lambda s:int(s) in range(1920, 2003)),
    "iyr":(lambda s:int(s) in range(2010, 2021)),
    "eyr":(lambda s:int(s) in range(2020, 2031)),
    "hgt":(lambda s:int(s[:-2]) in {'cm':range(150,194), 'in':range(59,77)}[s[-2:]]),
    "hcl":(lambda s:re.fullmatch('#[0-9a-f]{6}', s) != None),
    "ecl":(lambda s:s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    "pid":(lambda s:re.fullmatch('\d{9}', s) != None),
    "cid":(lambda s:True)
}

mandatory = set(check.keys())
mandatory.remove('cid')

current = {}
count = 0
for i in range(953):
    line = input()
    if line:
        for pair in line.split():
            key, val = pair.split(':')
            current[key] = val
    if not line or i == 952:
        try:
            if set(current.keys()) >= mandatory and not False in [check[k](v) for k,v in current.items()]:
                count += 1
        except:
            pass
        current.clear()
print(count)
