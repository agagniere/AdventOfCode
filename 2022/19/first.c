#include "common.h"

#include <ft_printf.h>
#include <get_next_line.h>

#include <unistd.h> /* STDIN_FILENO */

int main(void)
{
	int     blueprint_id            = 0;
	bunch_t recipes[resource_count] = {};
	char*   line                    = NULL;
	long    total                   = 0;
	int     quality;

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
		/*
		ft_printf(
			"Blueprint %i:\n\t"
			"Each ore robot costs %i ore.\n\t"
			"Each clay robot costs %i ore.\n\t"
			"Each obsidian robot costs %i ore and %i clay.\n\t"
			"Each geode robot costs %i ore and %i obsidian.\n",
			blueprint_id,
			recipes[ORE].ore, recipes[CLAY].ore,
			recipes[OBSIDIAN].ore, recipes[OBSIDIAN].clay,
			recipes[GEODE].ore, recipes[GEODE].obsidian);
		*/
		quality = quality_level(recipes, 24);
		ft_printf("Blueprint %i: %i\n", blueprint_id, quality);
		total += blueprint_id * quality;
	}
	ft_printf("%li\n", total);
	return 0;
}
