class Point2D:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	def move(self, dx, dy):
		self.x = self.x + dx
		self.y = self.y + dy

	def __str__(self) -> str:
		return f'Point2D(x: {self.x}, y: {self.y})'

	def __call__(self, x, y, *args, **kwds):
		print(f'args: {args}')
		print(f'keyword args: {kwds}')

		if 'foo' in kwds:
			v = kwds['foo']
			print(f'foo: {v}')
		
		self.move(1, 1)
		print(self)


p1 = Point2D(1, 1)
p1(2, 3, 3, 'foo', key='value', foo='kar')
