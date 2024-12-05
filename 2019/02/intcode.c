#include <ft_array.h>

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef NDEBUG
#	define DEBUG(A)
#else
#	define DEBUG(A) A
#endif

typedef uint64_t (*t_function)(uint64_t, uint64_t);

uint64_t add(uint64_t a, uint64_t b) { return a + b; }

uint64_t mul(uint64_t a, uint64_t b) { return a * b; }

static const t_function operations[10] = {[1] add, [2] mul};

int64_t intcode(uint64_t* program)
{
	uint64_t *p = program;

	while (*p != 99)
	{
		DEBUG(printf("%c ( %lu %lu ) -> %lu\n", "?+*"[p[0]], p[1], p[2], p[3]));
		DEBUG(if (*p > 2) return -1);
		program[p[3]] = operations[*p](program[p[1]], program[p[2]]);
		p += 4;
	}
	return *program;
}

size_t read_stdin(uint64_t** program)
{
	t_array  result        = NEW_ARRAY(uint64_t);
	char*    buffer        = NULL;
	size_t   buffer_length = 0;
	ssize_t  status;
	uint64_t n;

	while ((status = getdelim(&buffer, &buffer_length, ',', stdin)) > 0)
	{
		n = atoi(buffer);
		fta_append(&result, &n, 1);
	}
	free(buffer);
	*program = result.data;
	return result.size;
}

int main(int ac, char** av)
{
	uint64_t* program;
	size_t   length = read_stdin(&program);

	DEBUG(if (ac >= length) return 1);
	while (ac --> 1)
		program[ac] = atoi(av[ac]);
	printf("%li\n", intcode(program));
	free(program);
	return 0;
}
