#include "common.h"

#include <ft_prepro/tools.h> /* MAX */
#include <ft_printf.h>
#include <ft_deque.h>
#include <get_next_line.h>

#include <unistd.h> /* STDIN_FILENO */

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

typedef struct
{
	int8_t  time;
	bunch_t robots;
	bunch_t resources;
} iteration_t;

int quality_level(bunch_t recipes[4], int time_limit)
{
	iteration_t storage[100];
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
		ft_printf("%hhi: %hi -> %hi\n", current.time, current.robots.ore, current.resources.ore);
		if (current.robots.geode)
		{
			geodes = current.resources.geode + (time_limit - current.time) * current.robots.geode;
			if (geodes > best)
			{
				ft_printf("By waiting with %hi geode robots, we can get %i geodes.\n",
						  current.robots.geode, geodes);
				best = geodes;
			}
		}
		geodes = greedy(recipes, time_limit - current.time, current.robots, current.resources);
		if (geodes > best)
		{
			ft_printf("Greedy algo gets us %i\n", geodes);
			best = geodes;
		}

		if (current.robots.ore < max_ore)
		{
			iteration_t next = current;
			while (next.resources.ore < recipes[ORE].ore)
			{
				next.resources = add(next.resources, next.robots);
				next.time += 1;
				ft_printf("%hhi: %hi\n", next.time, next.resources.ore);
			}
			next.resources = add(next.resources, opposite(recipes[ORE]));
			next.resources = add(next.resources, next.robots);
			next.robots.ore += 1;
			next.time += 1;
			ft_printf("%hhi: %hi\n", next.time, next.resources.ore);

			next.resources = add(next.resources, next.robots);
			next.time += 1;
			FTQ_PUSH_BACK_ONE(fringe, &next);
		}

		/*
		current.time += 1;
		current.resources = add(current.resources, current.robots);
		if (current.time < time_limit)
			FTQ_PUSH_BACK_ONE(fringe, &current);
		*/
	}
	return best;
}

int main()
{
	int     blueprint_id            = 0;
	bunch_t recipes[resource_count] = {};
	char*   line                    = NULL;
	long    total                   = 0;

	while (get_next_line(STDIN_FILENO, &line) == 1)
	{
		blueprint_id            = next_int(line);
		recipes[ORE].ore        = next_int(NULL);
		recipes[CLAY].ore       = next_int(NULL);
		recipes[OBSIDIAN].ore   = next_int(NULL);
		recipes[OBSIDIAN].clay  = next_int(NULL);
		recipes[GEODE].ore      = next_int(NULL);
		recipes[GEODE].obsidian = next_int(NULL);
		free(line);
		/*ft_printf(
			"Blueprint %i:\n\t"
			"Each ore robot costs %i ore.\n\t"
			"Each clay robot costs %i ore.\n\t"
			"Each obsidian robot costs %i ore and %i clay.\n\t"
			"Each geode robot costs %i ore and %i obsidian.\n",
			blueprint_id,
			recipes[ORE].ore, recipes[CLAY].ore,
			recipes[OBSIDIAN].ore, recipes[OBSIDIAN].clay,
			recipes[GEODE].ore, recipes[GEODE].obsidian
			);*/
		int q = quality_level(recipes, 32);
		ft_printf("Blueprint %i: %i\n", blueprint_id, q);
		total += blueprint_id * q;
	}
	ft_printf("%li\n", total);
	return 0;
}
