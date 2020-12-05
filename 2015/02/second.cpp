#include <iostream>
#include <vector>
#include <algorithm> // min_element
#include <numeric> // accumulate

int main(void)
{
	std::vector<int> dim;
	std::vector<int> faces;
	int64_t total_length = 0;

	for (int box = 0; box < 1000; box++)
	{
		do
		{
			dim.push_back(0);
			std::cin >> dim.back();
		} while (std::cin.peek() == 'x' && std::cin.ignore());

		for (size_t i = 0; i < dim.size(); i++)
			faces.push_back(dim[i] + dim[(i + 1) % dim.size()]);

		total_length += 2 * *std::min_element(faces.cbegin(), faces.cend());
		total_length += std::accumulate(dim.cbegin(), dim.cend(), 1, std::multiplies<int>());

		dim.clear();
		faces.clear();
	}
	std::cout << total_length << std::endl;
	return 0;
}
