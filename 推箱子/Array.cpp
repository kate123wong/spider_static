#include "Array.h"

void ArrayInit (void )
{
	memset(map, 0, sizeof(map));
	for (int i = 3, j = 5; i <= 10; i++)
	{
		map[i][j] = ROAD;
	}
}
