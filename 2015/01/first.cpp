#include <iostream>

int main(void)
{
	char c;
	int64_t floor = 0;
	while (std::cin >> c)
		floor += (c == '(' ? 1 : -1);
	std::cout << floor << std::endl;
	return 0;
}
