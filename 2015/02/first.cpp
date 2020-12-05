#include <iostream>
#include <vector>
#include <algorithm> // min_element
#include <numeric> // accumulate

int main(void)
{
	std::vector<int> dim;
	std::vector<int> faces;
	int64_t total_surface = 0;

	for (int box = 0; box < 1000; box++)
	{
		do
		{
			dim.push_back(0);
			std::cin >> dim.back();
		} while (std::cin.peek() == 'x' && std::cin.ignore());

		for (int i = 0; i < dim.size(); i++)
			faces.push_back(dim[i] * dim[(i + 1) % dim.size()]);

		total_surface += *std::min_element(faces.cbegin(), faces.cend());
		total_surface += 2 * std::accumulate(faces.cbegin(), faces.cend(), 0);

		dim.clear();
		faces.clear();
	}
	std::cout << total_surface << std::endl;
	return 0;
}
