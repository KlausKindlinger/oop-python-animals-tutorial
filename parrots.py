import random

from animals import AWAKE
from pets import Pets


class Parrots(Pets):
	AWAKE_SOUND = 'undefined'
	ANGRY_SOUND = 'So nicht!'

	def __init__(self, name):
		super(Parrots, self).__init__(name)
		Parrots.counter += 1
		self.awake_sounds = ['Cracker', ' GruGru', 'Lustig']
		return

	def sound(self):
		my_animal_mood = self.mood
		my_mood = my_animal_mood.mood
		if my_mood == AWAKE:
			rv = random.choice(self.awake_sounds)
		else:
			rv = super(Parrots, self).sound()

		return rv
