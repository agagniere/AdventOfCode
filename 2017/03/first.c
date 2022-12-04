#include <stdlib.h>
#include <stdio.h>

int main(int ac, char** av)
{
	int N, root, layer, upper;

	if (ac < 2)
		return 0;
	N = atoi(av[1]);
	root = 1;
	while ((upper = root * root) < N)
		root += 2;
	root -= 1;
	while (upper - root > N)
		upper -= root;
	layer = root / 2;
	printf("%u\n", layer + abs(upper - layer - N));
	return 0;
}
