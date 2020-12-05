#include <iostream>

int main(void)
{
	int64_t floor = 0;
	unsigned index = 0;
	char c;

	while (floor >= 0)
	{
		std::cin >> c;
		floor += (c == '(' ? 1 : -1);
		index++;
	}
	std::cout << index << std::endl;
	return 0;
}
