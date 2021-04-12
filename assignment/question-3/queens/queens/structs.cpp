#include "structs.h"

board board_new() {
	return (board)calloc(1, sizeof(board_t));
}

board board_copy(board b1) {
	board b2 = board_new();
	for (int i = 0; i < b1->len; i++) {
		board_append(b2, &b1->v[i]);
	}
	return b2;
}

void board_free(board b) {
	free(b->v);
	free(b);
}

void board_append(board b, queen q) {
	if (b->len >= b->alloc) {
		b->alloc *= 2;
		if (!b->alloc)b->alloc = 4;
		b->v = (queen)realloc(b->v, sizeof(queen_t)*b->alloc);
	}
	b->v[b->len++] = *q;
}

void generate_random_board(board b, int n) {
	queen_t temp;
	for (int x = 0;x < n;x++) {
		temp = { x,rand() % n,0 };
		board_append(b, &temp);
	}
}

void print_board_state(board b) {
	for (int y = 0;y < b->len; y++) {
		for (int x = 0; x < b->len;x++) {
			if (b->v[x].y == y)printf("Q");
			else printf("E");
		}
		printf("\n");
	}
}

int get_board_heuristic(board b) {
	int h = 0;
	for (int i = 0;i < b->len;i++) {
		for (int j = i; j < b->len;j++) {
			if (b->v[i].x == b->v[j].x) h++;
			if (b->v[i].y == b->v[j].y) h++;
			if ((b->v[i].x - b->v[j].y) == (b->v[i].y - b->v[j].x)) h++;
		}
	}
	return h;
}