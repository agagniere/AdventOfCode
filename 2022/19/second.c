#include "common.h"

#include <ft_printf.h>
#include <get_next_line.h>

#include <unistd.h> /* STDIN_FILENO */

int main()
{
	int     blueprint_id            = 0;
	bunch_t recipes[resource_count] = {};
	char*   line                    = NULL;
	long    total                   = 1;
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
		quality = quality_level(recipes, 32);
		ft_printf("Blueprint %i: %i\n", blueprint_id, quality);
		total *= quality;
		if (blueprint_id == 3)
			break ;
	}
	ft_printf("%li\n", total);
	return 0;
}
