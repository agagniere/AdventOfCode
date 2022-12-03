#include <stdio.h>

static int match(char a, char b)
{
	return (a == b ? a - '0' : 0);
}

int main()
{
	char     buf[9000];
	unsigned result = 0;
	unsigned len;
	unsigned i = 0;

	scanf("%[0-9]", buf);
	while (buf[i])
		i++;
	len = i;
	while (i --> 0)
		result += match(buf[i], buf[(i + len/2) % len]);
	printf("%i\n", result);
	return 0;
}
