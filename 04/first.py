description = {
    "byr":"Birth Year",
    "iyr":"Issue Year",
    "eyr":"Expiration Year",
    "hgt":"Height",
    "hcl":"Hair Color",
    "ecl":"Eye Color",
    "pid":"Passport ID",
    "cid":"Country ID"
}

mandatory = set(description.keys())
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
        if set(current.keys()) >= mandatory:
            count += 1
        current.clear()
print(count)
