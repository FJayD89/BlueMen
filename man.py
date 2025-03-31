from cardinal import Cardinal
from point import Point

class Man:
	points: list[Point]

	def __init__(self, points: list[Point]):
		self.points = points

	@staticmethod
	def from_tuples(points_list: list[tuple[int, int]]) -> "Man":
		return Man.from_map(map(lambda p: Point(p[0],p[1]), points_list))

	@staticmethod
	def from_map(map_points: map) -> "Man":
		return Man(list(map_points))

	def rotate(self, origin: Point):
		return Man.from_map(map(lambda p: p.rotate(origin), self.points))

	def move_by(self,diff: Point) -> "Man":
		return Man.from_map(map(lambda p: p + diff, self.points))

	def __repr__(self):
		return str(list(map(str, self.points)))

	def normalize(self):
		xmin = min(map(Point.get_x, self.points))
		ymin = min(map(Point.get_y, self.points))
		move = Point(xmin, ymin)
		return self.move_by(-move)

	def set(self, points: list[Point]):
		self.points = points

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