#pragma once
#include <stdlib.h>
#include <stdio.h>

typedef struct q_t {int x, y, conflicts; }queen_t, *queen;
typedef struct b_t {int len, alloc; queen v; }board_t, *board;

board board_new();
board board_copy(board b);
void board_free(board b);
void board_append(board b, queen q);
void generate_random_board(board b, int n);
void print_board_state(board b);
int get_board_heuristic(board b);