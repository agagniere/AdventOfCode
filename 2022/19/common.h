#include <ft_coroutine.h>
#include <ft_ctype.h>       /* isdigit */
#include <ft_prepro/enum.h> /* DECLARE_ENUM */

#include <stdbool.h>
#include <stdint.h> /* uint8_t */
#include <unistd.h> /* STDIN_FILENO */

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
