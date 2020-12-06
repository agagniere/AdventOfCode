grep -P '([a-z][a-z]).*\1' input.txt | grep -P '([a-z])[a-z]\1' | wc -l
