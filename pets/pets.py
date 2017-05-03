from animals import Animals


class Pets(Animals):
	counter = 0

	def __init__(self, name):
		self.name = name

		super(Pets, self).__init__()
		Pets.counter += 1
		return
