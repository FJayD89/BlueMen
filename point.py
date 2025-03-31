class Point:
	x: int
	y: int

	def __init__(self, x, y):
		self.x = x
		self.y = y

	@staticmethod
	def from_tuple(t: tuple[int, int]):
		return Point(t[0], t[1])

	def rotate(self, origin: "Point") -> "Point":
		"""
		Clockwise 90 deg rotation around the origin
		:param origin:
		:return:
		"""
		diff = self.get_diff(origin)
		return Point(diff.y, -diff.x)

	def get_diff(self, other: "Point"):
		return Point(self.x - other.x, self.y - other.y)

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __repr__(self):
		return f"({self.x},{self.y})"


	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def set_point(self, point: "Point") -> None:
		self.x = point.x
		self.y = point.y

	def set_xy(self, x:int, y:int) -> None:
		self.x = x
		self.y = y

	def __neg__(self):
		return Point(-self.x, -self.y)

	def __eq__(self, other: "Point"):
		return self.x == other.x and self.y == other.y

	@staticmethod
	def o():
		return Point(0,0)
