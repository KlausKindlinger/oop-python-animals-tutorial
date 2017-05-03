class AnimalSounds(object):
	def __init__(self, sound):
		self.sound = sound

	def __str__(self):
		return self.sound

class AnimalMoods(object):
	def __init__(self, mood):
		self.mood = mood

	def __str__(self):
		return self.mood

	def __repr__(self):
		return self.__str__()

class AnimalMoodSounds(object):
	def __init__(self):
		self.moodsounds = {}

	def add_moodsound(self, mood, sound):
		key = str(mood)
		self.moodsounds.update({key:sound})

	def get_sound(self,mood):
		snd = self.moodsounds[mood]
		return snd

class Animals(object):
	def __init__(self):
		self.status = 'Awake'
		self.moodsounds = AnimalMoodSounds()
		mood = AnimalMoods('Sleeping')
		sound = AnimalSounds('zzzz')
		self.moodsounds.add_moodsound(mood, sound)

	def sound(self):
		snd = self.moodsounds.get_sound(self.status)
		return snd

	def set_sleep(self):
		self.status = 'Sleeping'

	def set_awake(self):
		self.status = 'Awake'


class Cats(Animals):
	def __init__(self):
		super(Cats,self).__init__()
		mood = AnimalMoods('Awake')
		sound = AnimalSounds('Miau')
		self.moodsounds.add_moodsound(mood, sound)
		return


class Sheeps(Animals):
	def __init__(self):
		super(Sheeps,self).__init__()
		mood = AnimalMoods('Awake')
		sound = AnimalSounds('Mäh')
		self.moodsounds.add_moodsound(mood, sound)
		return







bruno = Cats()

print(bruno.sound())
bruno.set_sleep()
print(bruno.sound())

shaun = Sheeps()
print (shaun.sound())
shaun.set_sleep()
print (shaun.sound())