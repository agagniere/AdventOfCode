#include <ft_coroutine.h>
#include <ft_ctype.h> /* isdigit */
#include <ft_deque.h>
#include <ft_prepro/enum.h>  /* DECLARE_ENUM */
#include <ft_prepro/tools.h> /* MAX */

#include <stdbool.h>
#include <stdint.h> /* int*_t */

typedef union bunch bunch_t;

union bunch
{
	struct
	{
		int16_t ore;
		int16_t clay;
		int16_t obsidian;
		int16_t geode;
	};
	int16_t by_index[4];
};

DECLARE_ENUM(
	resource,
	ORE,
	CLAY,
	OBSIDIAN,
	GEODE
);

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

bunch_t add(bunch_t a, bunch_t b)
{
	bunch_t s;
	int     i = resource_count;

	while (i --> 0)
		s.by_index[i] = a.by_index[i] + b.by_index[i];
	return s;
}

bunch_t opposite(bunch_t b)
{
	bunch_t o;
	int     i = resource_count;

	while (i --> 0)
		o.by_index[i] = -b.by_index[i];
	return o;
}

bool can_afford(bunch_t recipe, bunch_t resources)
{
	int i = resource_count;

	while (i --> 0)
		if (recipe.by_index[i] > resources.by_index[i])
			return false;
	return true;
}

/*
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
		resources = add(resources, robots);
		if (buying != resource_count)
		{
			resources = add(resources, opposite(recipes[buying]));
			robots.by_index[buying]++;
		}

		ft_printf("%2i [%2i %2i %2i %2i] [%2i %2i %2i %2i]\n", time,
				  robots.ore, robots.clay, robots.obsidian, robots.geode,
                  resources.ore, resources.clay, resources.obsidian, resources.geode);

	}
	return resources.geode;
}
*/

typedef struct
{
	int8_t  time;
	bunch_t robots;
	bunch_t resources;
} iteration_t;

int quality_level(bunch_t recipes[4], int time_limit)
{
	iteration_t storage[300000];
	t_deque     fringe[] = {DEQUE_NEW(storage)};
	iteration_t current  = { .robots = { .ore = 1 } };
	int         best     = 0;
	int         max_ore  = MAX(recipes[CLAY].ore, recipes[OBSIDIAN].ore, recipes[GEODE].ore);
	int         geodes;

	ftq_intent(fringe, 'B'); /* Will only push back */
	FTQ_PUSH_BACK_ONE(fringe, &current);
	while (!ftq_is_empty(fringe))
	{
		FTQ_POP_FRONT_ONE(fringe, &current);
		/*
		ft_printf("%hhi: (%hi, %hi) -> (%hi, %hi)\n",
				  current.time,
				  current.robots.ore, current.robots.clay,

				  current.resources.ore, current.resources.clay);
		*/
		if (current.robots.geode)
		{
			geodes = current.resources.geode + (time_limit - current.time) * current.robots.geode;
			if (geodes > best)
			{
				/*ft_printf("By waiting with %hi geode robots, we can get %i geodes.\n",
				  current.robots.geode, geodes);*/
				best = geodes;
			}
		}

		if (current.robots.ore < max_ore)
		{
			iteration_t next = current;
			while (next.resources.ore < recipes[ORE].ore)
			{
				next.resources = add(next.resources, next.robots);
				next.time += 1;
			}
			next.resources = add(next.resources, opposite(recipes[ORE]));
			next.resources = add(next.resources, next.robots);
			next.robots.ore += 1;
			next.time += 1;
			if (next.time < time_limit)
				FTQ_PUSH_BACK_ONE(fringe, &next);
		}

		if (current.robots.clay < recipes[OBSIDIAN].clay)
		{
			iteration_t next = current;
			while (next.resources.ore < recipes[CLAY].ore)
			{
				next.resources = add(next.resources, next.robots);
				next.time += 1;
			}
			next.resources = add(next.resources, opposite(recipes[CLAY]));
			next.resources = add(next.resources, next.robots);
			next.robots.clay += 1;
			next.time += 1;
			if (next.time < time_limit)
				FTQ_PUSH_BACK_ONE(fringe, &next);
		}

		if (current.robots.clay && current.robots.obsidian < recipes[GEODE].obsidian)
		{
			iteration_t next = current;
			while (next.resources.ore < recipes[OBSIDIAN].ore
				   || next.resources.clay < recipes[OBSIDIAN].clay)
			{
				next.resources = add(next.resources, next.robots);
				next.time += 1;
			}
			next.resources = add(next.resources, opposite(recipes[OBSIDIAN]));
			next.resources = add(next.resources, next.robots);
			next.robots.obsidian += 1;
			next.time += 1;
			if (next.time < time_limit)
				FTQ_PUSH_BACK_ONE(fringe, &next);
		}

		if (current.robots.obsidian)
		{
			iteration_t next = current;
			while (next.resources.ore < recipes[GEODE].ore
				   || next.resources.obsidian < recipes[GEODE].obsidian)
			{
				next.resources = add(next.resources, next.robots);
				next.time += 1;
			}
			next.resources = add(next.resources, opposite(recipes[GEODE]));
			next.resources = add(next.resources, next.robots);
			next.robots.geode += 1;
			next.time += 1;
			if (next.time < time_limit)
				FTQ_PUSH_BACK_ONE(fringe, &next);
		}
	}
	return best;
}
