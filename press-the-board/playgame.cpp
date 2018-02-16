#include <vector>
#include <iostream>
#include "board.h"

int main()
{
	Board board1(3);
	board1.press(1, 1);
	board1.press(0, 2);
	board1.press(12, 1);
}