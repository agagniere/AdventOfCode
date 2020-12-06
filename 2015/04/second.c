#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <openssl/md5.h>

int main(int ac, char** av)
{
	char     str[50];
	uint8_t  hash[MD5_DIGEST_LENGTH];
	size_t   prefix;
	size_t   n;

    if (ac < 2)
	{
        printf("Usage: %s <stem>\n", *av);
        return 1;
    }
	memset(str, 0, sizeof(str));
	strncpy(str, av[1], 49);
	prefix = strlen(str);
	n = 0;
    while (++n)
	{
        snprintf(str + prefix, 49 - prefix, "%lu", n);
        MD5(str, strlen(str), hash);
		if (!*hash && !hash[1] && !hash[2])
		{
			printf("%02x%02x %02x%02x %lu\n", hash[0], hash[1], hash[2], hash[3], n);
			break;
		}
    }

    return 0;
}
