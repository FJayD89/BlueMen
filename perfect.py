from itertools import product

from man import Man
from point import Point


def generate_transformations(piece: Man):
	"""Generate all 8 possible transformations of a piece (rotations and flips)."""
	transformations = set()
	rotations = [
		piece,
		piece.rotate(),
		piece.rotate().rotate(),
		piece.rotate().rotate().rotate()
	]
	for rot in rotations:  # 4 rotations
		transformations.add(rot)
		transformations.add(rot.flip())
	return transformations


def can_place(board, piece: Man, top_left: Point):
	"""Check if a piece can be placed at a given position (top-left corner)."""
	for p in piece:
		x,y = p + top_left
		if not (0 <= x < len(board) and 0 <= y < len(board[0])) or board[x][y] != 0:
			return False
	return True


def place_piece(board, piece: Man, top_left, piece_id):
	for p in piece:
		x,y = p + top_left
		board[x][y] = piece_id


def remove_piece(board, piece, top_left):
	for p in piece:
		x,y = p + top_left
		board[x][y] = 0


def solve_puzzle(board, pieces, piece_index=0, ret_all: bool = False):
	if piece_index == len(pieces):
		print("SOLVED!!!")
		# print_board(board)
		return True  # All pieces placed

	for symm in pieces[piece_index]:
		points = (Point(x,y) for x in range(len(board)) for y in range(len(board[0])))
		for p in points:
			if can_place(board, symm, p):
				place_piece(board, symm, p, piece_index + 1)
				if solve_puzzle(board, pieces, piece_index + 1):
					if not ret_all: return True
				remove_piece(board, symm, p)

	return False


def print_board(board):
	for row in board:
		print(' '.join(str(cell) for cell in row))


def from_grid(grid: list[list[int]]):
	height = len(grid)
	width = len(grid[0])
	coords = set()

	for (y, x) in product(range(height), range(width)):
		if grid[y][x] == 1:
			coords.add((x, y))

	return Man(Point(x,y) for x,y in coords)


def to_grid(man: Man):
	width = max(p.x for p in man) + 1
	height = max(p.y for p in man) + 1

	grid = [[' ' for i in range(width)] for j in range(height)]

	for (y, x) in product(range(height), range(width)):
		if Point(x, y) in man:
			grid[y][x] = 'X'

	grid = [" ".join(map(str, line)) for line in grid]
	grid = "\n".join(grid)
	return grid


def choose_n(arr, n: int) -> list[set]:
	# return all unordered n-combinations from a list
	if n == 0:
		return [set()]
	if not arr:
		return []

	rest_with = choose_n(arr[1:], n - 1)
	without = choose_n(arr[1:], n)

	head = arr[0]

	with_first = [set.union(s.copy(), {head}) for s in rest_with]

	return with_first + without
