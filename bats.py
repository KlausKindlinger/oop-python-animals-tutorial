from animals import Animals
from animals.awaketimeduration import AwakeTimeDuration

class Bats(Animals):
	counter = 0

	AWAKE_SOUND = 'Fiep'
	ANGRY_SOUND = 'FIEP'

	def __init__(self):
		super(Bats, self).__init__()

		Bats.counter += 1

		self.aweketime = AwakeTimeDuration(20, 8)

		return

