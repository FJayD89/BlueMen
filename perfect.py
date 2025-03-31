from itertools import product


def rotate(piece):
	return {(y, -x) for (x, y) in piece}


def flip(piece):
	return {(-x, y) for (x, y) in piece}


def generate_transformations(piece):
	"""Generate all 8 possible transformations of a piece (rotations and flips)."""
	transformations = set()
	current = piece
	for _ in range(4):  # 4 rotations
		current = rotate(current)
		transformations.add(frozenset(current))
		transformations.add(frozenset(flip(current)))
	return [set(trans) for trans in transformations]


def can_place(board, piece: set[tuple[int, int]], top_left: tuple[int, int]):
	"""Check if a piece can be placed at a given position (top-left corner)."""
	for (dx, dy) in piece:
		x = top_left[0] + dx
		y = top_left[1] + dy
		if not (0 <= x < len(board) and 0 <= y < len(board[0])) or board[x][y] != 0:
			return False
	return True


def place_piece(board, piece: tuple[int, int], top_left, piece_id):
	for (dx, dy) in piece:
		x = top_left[0] + dx
		y = top_left[1] + dy
		board[x][y] = piece_id


def remove_piece(board, piece, top_left):
	for (dx, dy) in piece:
		x = top_left[0] + dx
		y = top_left[1] + dy
		board[x][y] = 0


def solve_puzzle(board, pieces, piece_index=0, ret_all: bool = False):
	if piece_index == len(pieces):
		print("SOLVED!!!")
		# print_board(board)
		return True  # All pieces placed

	for symm in pieces[piece_index]:
		for x in range(len(board)):
			for y in range(len(board[0])):
				if can_place(board, symm, (x, y)):
					place_piece(board, symm, (x, y), piece_index + 1)
					if solve_puzzle(board, pieces, piece_index + 1):
						if not ret_all: return True
					remove_piece(board, symm, (x, y))

	return


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

	return frozenset(coords)


def to_grid(man: set):
	width = max(p[0] for p in man) + 1
	height = max(p[1] for p in man) + 1

	grid = [[' ' for i in range(width)] for j in range(height)]

	for (y, x) in product(range(height), range(width)):
		if (x, y) in man:
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
