grep "add y w" -A1 input.txt --color=never | grep -P "\d+" -o --color=never > a.txt
grep "eql x w" -B1 input.txt --color=never | grep -P "[-]?\d+" -o --color=never > b.txt
paste a.txt b.txt -d ' '
rm a.txt b.txt
