import re

def check_byr(s):
    y = int(s)
    return 1920 <= y and y <= 2002
def check_iyr(s):
    y = int(s)
    return 2010 <= y and y <= 2020
def check_eyr(s):
    y = int(s)
    return 2020 <= y and y <= 2030
def check_hgt(s):
    h, u = int(s[:-2]), s[-2:]
    return u in ['cm', 'in'] and (150 <= h and h <= 193) if  u == 'cm' else (59 <= h and h <= 76)

def check_hcl(s): return re.fullmatch('#[0-9a-f]{6}', s) != None
def check_ecl(s): return s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def check_pid(s): return re.fullmatch('\d{9}', s) != None
def check_cid(s): return True

check = {"byr":check_byr, "iyr":check_iyr, "eyr":check_eyr, "hgt":check_hgt, "hcl":check_hcl, "ecl":check_ecl, "pid":check_pid, "cid":check_cid}

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
