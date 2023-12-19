[Statement](https://adventofcode.com/2023/day/17)

```console
$ time python first.py < sample.txt
Cells          :     144
Node visited   :     571
Left in fringe :      76
OOO  OOOO
  OOOO  O
        OOO
          O
          OO
           O
           O
           OO
            O
            O
           OO
           O
           OO
102

real  0m0,075s
user  0m0,062s
sys   0m0,015s

$ time python second.py < sample.txt
Cells          :     144
Node visited   :     115
Left in fringe :     229
OOOOOOOOO
        O
        O
        O
        OOOOO
            O
            O
            O
            O
            O
            O
            O
            O
94

real  0m0,065s
user  0m0,054s
sys   0m0,015s
```

```console
$ time python first.py < input.txt
Cells          :   19600
Node visited   :   75628
Left in fringe :    1259

real  0m3,086s
user  0m3,004s
sys   0m0,080s

$ time python second.py < input.txt
Cells          :   19600
Node visited   :   75406
Left in fringe :    3963

real  0m7,088s
user  0m7,011s
sys   0m0,068s
```
