set -e # Exit on fail
set -u # Exit if using an undefined variable
set -o pipefail # A pipe fails if one of its command fails
shopt -s extglob lastpipe # Persist hashmap values outside of loops

declare -A stars # Declare a hashmap

printf "| Day " ;
for folder in $("ls" -d */)
do
    printf "|[${folder%/}](https://adventofcode.com/${folder%/})"
done
echo "|"

printf "| --: " ;
for folder in $("ls" -d */)
do
    printf "| :--------: "
    stars[$folder]=0
done
echo "|"

for i in $(seq -w 25)
do
    printf "| $i  "
    for folder in $("ls" -d */)
    do
        printf "|"
        compgen -G "$folder$i/first*" >/dev/null && printf ":star": && stars[$folder]=$(( ${stars[$folder]} + 1 ))
        compgen -G "$folder$i/second*" > /dev/null && printf ":star:" && stars[$folder]=$(( ${stars[$folder]} + 1 ))
    done
    printf "\n"
done

counter=0
printf "| Total"
for folder in $("ls" -d */)
do
    printf " | %i" ${stars[$folder]}
	counter=$(( counter + ${stars[$folder]} ))
done
printf "\n\nTotal stars: %i\n" $counter
