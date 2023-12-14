[Statement](https://adventofcode.com/2023/day/14)

```console
$ time python second.py < sample.txt
Found a loop of length 7, starting from 3
The 1000000000th cycle is at step 3 of the loop
Therefore it is the same as the 6th cycle
64
CacheInfo(hits=290, misses=110, maxsize=None, currsize=110)

real   0m0,057s
user   0m0,048s
sys    0m0,012s

$ time python second.py < input.txt
Found a loop of length 17, starting from 151
The 1000000000th cycle is at step 9 of the loop
Therefore it is the same as the 160th cycle
...
CacheInfo(hits=62209, misses=4991, maxsize=None, currsize=4991)

real   0m0,140s
user   0m0,121s
sys    0m0,021s
```
