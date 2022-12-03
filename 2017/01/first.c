#include <stdio.h>

static int match(char a, char b)
{
	return (a == b ? a - '0' : 0);
}

int main()
{
	char     buf[9000];
	char*    p      = buf;
	unsigned result = 0;

	scanf("%[0-9]", buf);
	while (*++p)
		result += match(*p, p[-1]);
	result += match(p[-1], *buf);
	printf("%i\n", result);
	return 0;
}
