#include "queens.h"

int main()
{
	//while(true){
		board b = board_new();
		generate_random_board(b, 8);
		print_board_state(b);
		printf("Heuristic: %i\n", get_board_heuristic(b));
		printf("\n");
		getchar();
	//}
    return 0;
}

