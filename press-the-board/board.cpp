#include <iostream>
#include <cstdlib>
#include "board.h"

Board::Board(int b_size){
	size = b_size;
	// randomly generate a board of size b_size
	srand((unsigned)time(0));
	for(int i=0; i<size; i++){
		pieces.push_back(std::vector<bool>());
		for(int j=0; j<size; j++){
			pieces[i].push_back(rand() % 2 == 0);
		}
	}
	printBoard();
}

Board::Board(int b_size, const std::vector<std::vector<bool> > & init_board){
	size = b_size;
	// set the pieces of the board to be the same as init_board
	for(int i=0; i<size; i++){
		pieces.push_back(std::vector<bool>(init_board[i]));
	}
	printBoard();
}

// Modifiers
bool Board::press(int row, int col){
	if(row < 0 or row > size - 1 or col < 0 or col > size - 1){
		return false;
	}
	// invert the pressed position
	pieces[row][col] = !pieces[row][col];
	// invert the piece on the top of the pressed position if possible
	if(row - 1 >= 0){
		pieces[row-1][col] = !pieces[row-1][col];
	}
	// invert the piece on the bottom of the pressed position if possible
	if(row + 1 < size){
		pieces[row+1][col] = !pieces[row+1][col];
	}
	// invert the piece on the left of the pressed position if possible
	if(col - 1 >= 0){
		pieces[row][col-1] = !pieces[row][col-1];
	}
	// invert the piece on the right of the pressed position if possible
	if(col + 1 < size){
		pieces[row][col+1] = !pieces[row][col+1];
	}
	/*
	// invert the up, down, left, right pieces of the position pressed and itself
	for(int i=-1; i<=1; i++){
		if(row + i < 0 or row + i > size - 1) continue;
		for(int j=-1; j<=1; j++){
			if(col + j < 0 or col + j > size - 1) continue;
			pieces[row+i][col+j] = !pieces[row+i][col+j];
		}
	}
	*/
	printBoard();
	return true;
}

// Other member functions
bool Board::isSolved() const{
	for(int i=0; i<size; i++){
		for(int j=0; j<size; j++){
			if(!pieces[i][j]){
				return false;
			}
		}
	}
	return true;
}

std::vector<std::vector<int> > Board::solve(){
	std::vector<std::vector<int> > steps;
	return steps;
}

void Board::printBoard() const{
	std::cout << "----------------------------------" << std::endl;
	std::cout << "Board size: "<< size << std::endl;	
	std::cout << "Board:" << std::endl;
	for(int i=0; i<size; i++){
		for(int j=0; j<size; j++){
			std::cout << pieces[i][j] << "   ";
		}
		std::cout << std::endl;
	}
}