sed -E 's|mul (\S) (\S)|\1 *= \2;|' |
    sed -E 's|add (\S) (\S+)|\1 += \2;|' |
    sed -E 's|div (\S) (\S+)|\1 /= \2;|' |
    sed -E 's|mod (\S) (\S+)|\1 %= \2;|' |
    sed -E 's|eql (\S) (\S+)|\1 = \1 == \2;|' |
    sed -E 's|inp (\S)|\1 = input[];|'
