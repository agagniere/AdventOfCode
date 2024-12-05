#include <libft/ft_array.h> // t_array

#include <stdint.h> // int64_t
#include <stdio.h> // printf
#include <stdlib.h> // EXIT_SUCCESS
#include <stdbool.h> // bool true false
#include <string.h> // strcmp
#include <inttypes.h> // PRI*

#ifdef NDEBUG
#	define DEBUG(A)
#else
#	define DEBUG(A) A
#endif

enum Instruction {
	Add = 1,
	Multiply,
	Input,
	Output,
	JumpIfTrue,
	JumpIfFalse,
	LessThan,
	Equals,
	Stop = 99
};

/**
 * Interpret @p program as intcode
 * @param input: values used by the input opcode, used as a stack (reverse order)
 */
int64_t intcode(int64_t* program, t_array* input)
{
	int64_t *p = program;

	while (true)
	{
		bool mode1 = (*p /   100) % 2;
		bool mode2 = (*p /  1000) % 2;
		enum Instruction instruction = *p % 100;

		switch (instruction)
		{
		case Add:
			program[p[3]] = (mode1 ? p[1] : program[p[1]]) + (mode2 ? p[2] : program[p[2]]);
			p += 4;
			break;
		case Multiply:
			program[p[3]] = (mode1 ? p[1] : program[p[1]]) * (mode2 ? p[2] : program[p[2]]);
			p += 4;
			break;
		case Input:
			DEBUG(if (input->size == 0) {fprintf(stderr, "Out of input\n"); return -1;});
			program[p[1]] = *(int64_t*)ARRAY_LAST(input);
			DEBUG(printf("Read: %" PRIi64 "\n", program[p[1]]));
			fta_popback(input, 1);
			p += 2;
			break;
		case Output:
			printf("%" PRIi64 "\n", mode1 ? p[1] : program[p[1]]);
			p += 2;
			break;
		case JumpIfTrue:
			if (mode1 ? p[1] : program[p[1]])
				p = program + (mode2 ? p[2] : program[p[2]]);
			else
				p += 3;
			break;
		case JumpIfFalse:
			if (!(mode1 ? p[1] : program[p[1]]))
				p = program + (mode2 ? p[2] : program[p[2]]);
			else
				p += 3;
			break;
		case LessThan:
			program[p[3]] = (mode1 ? p[1] : program[p[1]]) < (mode2 ? p[2] : program[p[2]]);
			p += 4;
			break;
		case Equals:
			program[p[3]] = (mode1 ? p[1] : program[p[1]]) == (mode2 ? p[2] : program[p[2]]);
			p += 4;
			break;
		case Stop:
			return *program;
		default:
			fprintf(stderr, "Unsupported instruction: %u\n", instruction);
			return -1;
		}
	}
	return *program;
}

size_t read_stdin(int64_t** program)
{
	t_array  result        = NEW_ARRAY(int64_t);
	char*    buffer        = NULL;
	size_t   buffer_length = 0;
	ssize_t  status;
	int64_t n;

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
	int64_t* program;
	t_array  input = NEW_ARRAY(int64_t);
	int64_t  n;

	read_stdin(&program);
	fta_reserve(&input, ac);
	while (ac --> 1)
	{
		n = atoi(av[ac]);
		fta_append(&input, &n, 1);
	}
	intcode(program, &input);
	free(program);
	fta_clear(&input);
	return EXIT_SUCCESS;
}
