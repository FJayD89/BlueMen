from itertools import product

from man import Man
from point import Point

class Board:
	width: int
	height: int
	men: list[tuple[Man, Point]]

	def __init__(self, width: int, height: int, men: list[tuple[Man, Point]]):
		self.men = men
		self.height = height
		self.width = width

	def get_potentials(self, man: Man):
		bound = man.get_border()
		positions = list(map(Point.from_tuple,
		                     product(range(self.width - bound.x), range(self.height - bound.y))))
		return positions

	def overlaps(self, man: Man, pos: Point):
		return sum(other.overlap(man, pos - opos) for (other, opos) in self.men)

	def get_positions(self, man: Man):
		srt = sorted(self.get_potentials(man), key=lambda p: self.overlaps(man, p))
		minval = self.overlaps(man, srt[0])
		best = []
