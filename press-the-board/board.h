#ifndef Board_h_
#define Board_h_

#include <vector>

class Board{
public:
	// Constructors
	Board(int b_size);
	Board(int b_size, const std::vector<std::vector<bool> > & init_board);

	// Modifiers
	bool press(int row, int col);

	// Other member functions
	bool isSolved() const;
	std::vector<std::vector<int> > solve();
	void printBoard() const;

private:
	int size;
	std::vector<std::vector<bool> > pieces;
};

#endif