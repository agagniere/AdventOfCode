#include "common.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef ITERATIONS
#	define ITERATIONS 2022
#endif

uint64_t check_for_cycle(uint64_t* stopped_rocks, uint64_t tower_height)
{
	static uint64_t prev_H      = 0;
	static uint64_t prev_C      = 0;
	static uint64_t prev_diff_H = 0;
	static uint64_t prev_diff_C = 0;
	uint64_t        diff_H      = tower_height - prev_H;
	uint64_t        diff_C      = *stopped_rocks - prev_C;

	if (diff_H == prev_diff_H && diff_C == prev_diff_C)
	{
		uint64_t cycles = (ITERATIONS - *stopped_rocks) / diff_C;

		printf("Found a cycle after %llu rocks : the tower grows %llu units every %llu rocks\n",
		       *stopped_rocks, diff_H, diff_C);
		*stopped_rocks += cycles * diff_C;
		printf("Skipping %llu cycles to %llu rocks\n", cycles, *stopped_rocks);
		return cycles * diff_H;
	}
	prev_diff_H = diff_H;
	prev_diff_C = diff_C;
	prev_H      = tower_height;
	prev_C      = *stopped_rocks;
	return 0;
}

static const unsigned keep = 300;

unsigned discard(uint8_t* tower, unsigned* height, unsigned capacity)
{
	const unsigned to_discard = *height - keep;

	memmove(tower, tower + to_discard, keep);
	memset(tower + keep, 0, capacity - keep);
	*height = keep;
	return to_discard;
}

/*
** La belle au bois dormant a ferme les ecoutilles
** Elle hiberne
** La reveillez pas, laissez-la
*/
#define SIZE 2043

int main()
{
	uint8_t  pipe[SIZE] = {[0] 0x7f};
	uint64_t step       = 0;
	uint64_t count      = 0;
	uint64_t archived   = 0;
	unsigned Y          = 0;
	unsigned y;
	rock_t   R;

	while (count < ITERATIONS)
	{
		R = rocks[count % 5];
		y = Y + 3;
		while (y > Y)
		{
			if (count && step % (5 * p_max) == 0)
				archived += check_for_cycle(&count, archived + Y);
			shift_rock(&R, pattern[step++ % p_max], pipe + y-- + 1);
		}
		while (true)
		{
			if (count && step % (5 * p_max) == 0)
				archived += check_for_cycle(&count, archived + Y);
			shift_rock(&R, pattern[step++ % p_max], pipe + y + 1);
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
		if (Y > SIZE - 10)
			archived += discard(pipe + 1, &Y, SIZE - 1);
	}
	printf("%llu\n", Y + archived);
	return 0;
}
