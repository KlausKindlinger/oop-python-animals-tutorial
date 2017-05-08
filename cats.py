from pets import Pets
from animals.awaketimeduration import AwakeTimeDuration


class Cats(Pets):
	counter = 0

	AWAKE_SOUND = 'Miau'
	ANGRY_SOUND = 'Chhhhh'

	def __init__(self, name):
		super(Cats, self).__init__(name)
		Cats.counter += 1

		self.aweketime = AwakeTimeDuration(6, 20)
		return
