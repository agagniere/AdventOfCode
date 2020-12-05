#include <bitset.h>

#include <unistd.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>

# define SIZE 16057

/* Returns the number of element set in the set */
size_t BITSET_size(const t_bitset* set)
{
	size_t count = 0;
	const t_bitset* end = set + SIZE;
	t_bitset  word;

	while (set < end)
	{
		if (*set)
		{
			word = *set;
			while (word)
			{
				count += word & 1;
				word >>= 1;
			}
		}
		++set;
	}
	return count;
}

void BITSET_set(t_bitset* set, size_t index)
{
	index %= SIZE << 6;
	BITSET_SET(set, index);
}

uint32_t hash(uint16_t x, uint16_t y)
{
	return (x << 16) + y;
	//printf("Hashing %hu, %hu : %x %x\n", x, y, hash, hash % (SIZE << 6));
	//return hash;
}

int main(void)
{
	t_bitset set[SIZE];
	uint16_t x = 0;
	uint16_t y = 0;
	uint16_t rx = 0;
	uint16_t ry = 0;
	char     c;
	int      turn = 0;

	memset(set, 0, sizeof(set));
	BITSET_set(set, hash(x,y));
	while (read(0, &c, 1) == 1 && c >= ' ')
	{
		if (++turn % 2)
		{
			switch (c)
			{
			case '>': ++x; break;
			case '<': --x; break;
			case '^': ++y; break;
			case 'v': --y;
			}
			BITSET_set(set, hash(x,y));
		}
		else
		{
			switch (c)
			{
			case '>': ++rx; break;
			case '<': --rx; break;
			case '^': ++ry; break;
			case 'v': --ry;
			}
			BITSET_set(set, hash(rx,ry));
		}
	}
	printf("%lu\n", BITSET_size(set));
	return 0;
}
