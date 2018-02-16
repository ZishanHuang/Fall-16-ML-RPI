# Pressing the board

To open a locked treasure box, there is a puzzle that needs to be solved. A square board with size n has pieces on it showing either 0 or 1. When a piece on the board is pressed, the pressed piece itself, the piece above it, the piece below it, the piece on its left and the piece on its right will all be inverted. All the pieces of a square board of size n mush be 1 to open the box.

For example, the board below has a size of 3. When the position (1, 1) is pressed:

	0   0   0         0   1   0
	0   0   0   ==>   1   1   1
	0   0   1         0   1   1

When the position (0, 2) is pressed:

	0   1   0         0   0   1
	1   1   1   ==>   1   1   0
	0   1   1         0   1   1

The following is an example of a solved board:

	1   1   1
	1   1   1
	1   1   1

