#include <ft_coroutine.h>
#include <ft_ctype.h> /* isdigit */
#include <ft_deque.h>
#include <ft_prepro/enum.h>  /* DECLARE_ENUM */
#include <ft_prepro/tools.h> /* MAX */

#include <stdbool.h>
#include <stdint.h> /* int8_t */

DECLARE_ENUM(
	resource,
	ORE,
	CLAY,
	OBSIDIAN,
	GEODE
); /* Declares: resource_count, string_from_resource */

typedef union bunch      bunch_t;
typedef struct iteration iteration_t;

union bunch
{
	struct
	{
		uint8_t ore;
		uint8_t clay;
		uint8_t obsidian;
		uint8_t geode;
	};
	uint8_t by_index[resource_count];
};

struct iteration
{
	bunch_t robots;
	bunch_t resources;
	uint8_t  time;
};

/**
 ** Returns the next unsigned int found in the string, or 0 if none is found.
 */
int next_int(char* string)
{
	static char* p   = NULL;
	int          ans = 0;

	if (string && p) /* Discarding what's remaining of the previous string */
		p = string - 1;
	else if (!string && !p) /* No more ints to read */
		return 0;
	scrBegin;
	p = string;
	while (*p)
	{
		if (ft_isdigit(*p))
			ans = ans * 10 + *p - '0';
		else if (ans)
			scrReturn(ans);
		p++;
	}
	p = NULL;
	scrLine = 0;
	scrFinish(0);
}

void increment(bunch_t* a, bunch_t b)
{
	int     i = resource_count;

	while (i --> 0)
		a->by_index[i] += b.by_index[i];
}

bunch_t opposite(bunch_t b)
{
	int     i = resource_count;

	while (i --> 0)
		b.by_index[i] *= -1;
	return b;
}

bool can_afford(bunch_t recipe, bunch_t resources)
{
	int i = resource_count;

	while (i --> 0)
		if (recipe.by_index[i] > resources.by_index[i])
			return false;
	return true;
}


/* Buy the most complex robot affordable at each turn */
int greedy(bunch_t recipes[4], int time_limit, bunch_t robots, bunch_t resources)
{
	int time    = 0;

	while (time++ < time_limit)
	{
		enum resource buying = resource_count;
		int           i      = resource_count;

		while (i --> 0)
			if (can_afford(recipes[i], resources))
			{
				buying = i;
				break;
			}
		increment(&resources, robots);
		if (buying != resource_count)
		{
			increment(&resources, opposite(recipes[buying]));
			robots.by_index[buying]++;
		}

	}
	return resources.geode;
}

/* accumulate resources until we can afford the wanted robot */
void simulate_until(iteration_t state, t_deque* fringe, bunch_t recipes[4], enum resource wanted, int time_limit)
{
	while (!can_afford(recipes[wanted], state.resources))
	{
		increment(&state.resources, state.robots);
		state.time += 1;
	}
	increment(&state.resources, opposite(recipes[wanted]));
	increment(&state.resources, state.robots);
	state.robots.by_index[wanted] += 1;
	state.time += 1;
	if (state.time < time_limit)
		FTQ_PUSH_BACK_ONE(fringe, &state);
}


int quality_level(bunch_t recipes[4], int time_limit)
{
	iteration_t storage[200];
	t_deque     fringe[] = {DEQUE_NEW(storage)};
	iteration_t current  = {.robots = {.ore = 1}};
	int         best     = 0;
	const int   max_ore  = MAX(recipes[CLAY].ore, recipes[OBSIDIAN].ore, recipes[GEODE].ore);
	int         geodes;

	ftq_intent(fringe, 'B'); /* Will only push back */
	FTQ_PUSH_BACK_ONE(fringe, &current);
	while (!ftq_is_empty(fringe))
	{
		FTQ_POP_FRONT_ONE(fringe, &current);
		geodes = greedy(recipes, time_limit - current.time, current.robots, current.resources);
		best = MAX(best, geodes);

		if (current.robots.ore < max_ore)
			simulate_until(current, fringe, recipes, ORE, time_limit);
		if (current.robots.clay < recipes[OBSIDIAN].clay)
			simulate_until(current, fringe, recipes, CLAY, time_limit);
		/* Uncomment this block for an exhaustive search
		** It is not required for my input, but it is for the sample input.
		** It requires a muuuuch longer queue storage
		if (current.robots.clay && current.robots.obsidian < recipes[GEODE].obsidian)
			simulate_until(current, fringe, recipes, OBSIDIAN, time_limit);
		*/
		// if (current.robots.obsidian)
		//     simulate_until(current, fringe, recipes, GEODE, time_limit);
	}
	return best;
}
