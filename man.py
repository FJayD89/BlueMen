from typing import Iterable

from cardinal import Cardinal
from point import Point

class Man:
	points: frozenset[Point]

	def __init__(self, points: Iterable[Point]):
		self.points = frozenset(points)

	def rotate(self, origin: Point = Point.o()):
		return Man(p.rotate(origin) for p in self.points)

	def move_by(self,diff: Point) -> "Man":
		return Man(p + diff for p in self.points)

	def __repr__(self):
		return str(list(map(str, self.points)))

	def normalize(self):
		xmin = min(p.x for p in self.points)
		ymin = min(p.y for p in self.points)
		move = Point(xmin, ymin)
		return self.move_by(-move)

	def set(self, points: Iterable[Point]):
		self.points = frozenset(points)

	def get_border(self) -> Point:
		norm = self.normalize()
		xmax = max(map(Point.get_x, norm.points))
		ymax = max(map(Point.get_y, norm.points))
		return Point(xmax, ymax)

	def overlap(self, other: "Man", pos: Point):
		overlap_count = 0
		for a in self.normalize().points:
			for b in other.normalize().move_by(pos).points:
				if a == b:
					overlap_count += 1

		return overlap_count

	def facing(self, direction: Cardinal):
		match direction:
			case Cardinal.UP:
				return self
			case Cardinal.RIGHT:
				return self.rotate(Point.o())
			case Cardinal.DOWN:
				return self.rotate(Point.o()).rotate(Point.o())
			case Cardinal.LEFT:
				return self.rotate(Point.o()).rotate(Point.o()).rotate(Point.o())
			case _:
				raise Exception("WTF HOW")

	def __iter__(self):
		return iter(self.points)

	def flip(self):
		return Man(p.flip() for p in self.points)