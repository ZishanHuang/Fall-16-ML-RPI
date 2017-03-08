# N-puzzle

An extension of the 8-puzzle, 15-puzzle game to an n-puzzle game.

Sample 8-puzzle game:

        Start               Solved
    +---+---+---+       +---+---+---+
    | 3 | 1 | 2 |       |   | 1 | 2 |
    +---+---+---+       +---+---+---+
    |   | 4 | 5 |  ==>  | 3 | 4 | 5 |
    +---+---+---+       +---+---+---+
    | 6 | 7 | 8 |       | 6 | 7 | 8 |
    +---+---+---+       +---+---+---+

## How to run the game
###Useful Files

- board.py: contains the Board class
- game.py: main function for running the game

###Instructions
To play a random board of size 3, enter the following command:

```
$ python game.py
```

Command line arguments can be added to specify the board size, defining the board or not, and which algorithm used to solve the game.

	USAGE:
	-s,  --size <size>          set the size of board (default to 3)
	-d,  --define               user define the board or not
	-fn, --function <function>  set the function used to solve the game (default to 'human')

###Examples

1. Creating a random board of size 4: ```$ python game.py -s 4```

2. Enter values for a board of size 3 and solve it with astar: ```$ python game.py -d -fn astar```

3. Use bfs to solve a random board of size 5: ```$ python game.py --size 5 -fn bfs```

## Implementing

### What to do?

Implement the BFS and Astar algorithms which return a lists of actions.

Note that not all puzzles are solvable. Why?

Implement your isSolvable() function (otherwise your BFS/Astar might not terminate).

Look for the `""" ENTER YOUT CODE HERE """` in game.py.

### Useful Functions in the Board class

- `getSize()` returns the board size

- `getMaxNum()` returns the max number in the board (size^2 - 1)

- `getNum(i, j)` returns the number in board position (i,j)

- `getBoardAsGrid()` returns a 2D list of numbers

- `getBoardAsList()` returns a 1D list of numbers

- `getEmpty()` returns the position of the empty spot (position of 0)

- `isLegal(action)` returns True/False

- `move(action)` returns the new board that moved the empty tile left/right/up/down (original board not changed)

- `wins()` returns True/False

- `printBoard()` prints the board in ASCII art