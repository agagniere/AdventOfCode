#include "common.h"

#include <stdio.h>

int main()
{
	uint8_t  pipe[4000] = {[0] 0x7f};
	unsigned Y          = 0;
	unsigned turn       = 0;
	unsigned count      = 0;
	rock_t   R;
	unsigned y;

	while (count < 2022)
	{
		R = rocks[count % 5];
		y = Y + 3;
		while (y > Y)
			shift_rock(&R, pattern[turn++ % p_max], pipe + y-- + 1);
		while (true)
		{
			shift_rock(&R, pattern[turn++ % p_max], pipe + y + 1);
			if ((R.shape[0] & pipe[y]) || (R.height > 1 && (R.shape[1] & pipe[y + 1])))
			{
				for (unsigned in_range(i, R.height))
					pipe[y + i + 1] |= R.shape[i];
				Y = PP_MAX(Y, y + R.height);
				break;
			}
			y--;
		}
		count++;
	}
	printf("%u\n", Y);
}
