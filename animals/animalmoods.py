AWAKE = 'Awake'
SLEEPING = 'Sleeping'
ANGRY = 'Angry'

class AnimalMoods(object):

	def __init__(self, mood):
		self.mood = mood

	def __str__(self):
		return self.mood

	def __repr__(self):
		return self.__str__()
