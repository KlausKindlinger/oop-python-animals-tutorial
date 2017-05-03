from animals import Animals

class Sheeps(Animals):
	counter = 0

	AWAKE_SOUND = 'Mäh'
	ANGRY_SOUND = 'Blöök'

	def __init__(self):
		super(Sheeps, self).__init__()
		Sheeps.counter += 1
		return
