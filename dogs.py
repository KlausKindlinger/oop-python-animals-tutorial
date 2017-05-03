from pets.pets import Pets

class Dogs(Pets):
	counter = 0

	AWAKE_SOUND = 'WauWau'
	ANGRY_SOUND = 'Grrrrr'

	def __init__(self, name):
		super(Dogs, self).__init__(name)
		Dogs.counter += 1
		return
