from .animalmoods import AnimalMoods


class AnimalSounds(object):
	def __init__(self, sound):
		self.sound = sound

	def __str__(self):
		return self.sound


class AnimalMoodSounds(object):
	def __init__(self, mood, sound):
		self.mood = AnimalMoods(mood)
		self.sound = AnimalSounds(sound)
		return

	def key(self):
		key = str(self.mood)
		return key


class AnimalMoodSoundsCollection(object):
	def __init__(self):
		self.moodsounds = {}

	def add_moodsound(self, moodsound):
		key = moodsound.key()
		self.moodsounds.update({key: moodsound})

	def get_sound(self, mood):
		key = str(mood)
		moodsound = self.moodsounds[key]
		snd = moodsound.sound
		return snd
