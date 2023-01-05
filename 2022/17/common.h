#pragma once

#include "prepro_tools.h"

#include <stdbool.h>
#include <stdint.h>

typedef struct rock rock_t;

struct rock
{
	uint8_t height;
	uint8_t shape[4];
};

const rock_t rocks[5] = {
	{ .height = 1, .shape = {
			[0]LINE(1, 1, 1, 1)
		} },
	{ .height = 3, .shape = {
			[2]LINE(0, 1, 0),
			[1]LINE(1, 1, 1),
			[0]LINE(0, 1, 0)
		} },
	{ .height = 3, .shape = {
			[2]LINE(0, 0, 1),
			[1]LINE(0, 0, 1),
			[0]LINE(1, 1, 1)
		} },
	{ .height = 4, .shape = {
			[3]LINE(1),
			[2]LINE(1),
			[1]LINE(1),
			[0]LINE(1)
		} },
	{ .height = 2, .shape = {
			[1]LINE(1, 1),
			[0]LINE(1, 1)
		} }
};

#ifdef NDEBUG
#	include "input.c"
#else
const char pattern[] = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>";
#endif

const unsigned p_max = C_ARRAY_LENGTH(pattern) - 1;

inline bool shift_rock(rock_t* R, char way, const uint8_t* pipe)
{
	const uint8_t mask = (way == '>' ? 1 : 1 << 6);
	unsigned      y    = R->height;

	while (y --> 0)
		if (R->shape[y] & mask)
			return false;
	y = R->height;
	while (y --> 0)
		switch (way)
		{
		case '>':
			if ((R->shape[y] >> 1) & pipe[y])
				return false;
			break;
		case '<':
			if ((R->shape[y] << 1) & pipe[y])
				return false;
			break;
		}
	y = R->height;
	while (y --> 0)
		switch (way)
		{
		case '>': R->shape[y] >>= 1; break;
		case '<': R->shape[y] <<= 1; break;
		}
	return true;
}

#include <stdio.h>

inline void print_pile(const uint8_t* pipe, unsigned Y)
{
	unsigned h = Y + 1;
	while (h --> 0)
		printf("%c%c%c%c%c%c%c\n",
		       (pipe[h] & (1 << 6) ? 'O' : ' '),
		       (pipe[h] & (1 << 5) ? 'O' : ' '),
		       (pipe[h] & (1 << 4) ? 'O' : ' '),
		       (pipe[h] & (1 << 3) ? 'O' : ' '),
		       (pipe[h] & (1 << 2) ? 'O' : ' '),
		       (pipe[h] & (1 << 1) ? 'O' : ' '),
		       (pipe[h] & (1 << 0) ? 'O' : ' '));
}
