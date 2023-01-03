#include "common.h"

#include <ft_prepro/tools.h> /* MAX */
#include <ft_printf.h>
#include <get_next_line.h>

#include <unistd.h> /* STDIN_FILENO */

int quality_level(bunch_t recipes[4])
{
	int     time      = 0;
	bunch_t robots    = {.ore = 1};
	bunch_t resources = {};
	int     max_ore   = MAX(recipes[CLAY].ore, recipes[OBSIDIAN].ore, recipes[GEODE].ore);

	/*ft_printf("mn [  Robots   ] [ Resources ]\n");*/
	while (time++ < 24)
	{
		enum resource buying = resource_count;
		int           i      = resource_count;

		if (robots.ore < max_ore)
		{
			if (resources.ore >= recipes[ORE].ore)
				buying = ORE;
		}
		else
			while (i --> 0)
				if (can_afford(recipes[i], resources))
				{
					buying = i;
					break;
				}
		resources = add(resources, robots);
		if (buying != resource_count)
		{
			/*ft_printf("New %s robot is ready\n", string_from_resource[buying]);*/
			resources = add(resources, opposite(recipes[buying]));
			robots.by_index[buying]++;
		}
		/*ft_printf("%2i [%2i %2i %2i %2i] [%2i %2i %2i %2i]\n", time,
				  robots.ore, robots.clay, robots.obsidian, robots.geode,
				  resources.ore, resources.clay, resources.obsidian, resources.geode);*/
	}
	return resources.geode;
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
		int q = quality_level(recipes);
		ft_printf("%i\n", q);
		total += blueprint_id * q;
	}
	ft_printf("%li\n", total);
	return 0;
}
