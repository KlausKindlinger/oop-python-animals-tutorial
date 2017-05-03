class AnimalSounds(object):
	def __init__(self, sound):
		self.sound = sound

	def __str__(self):
		return self.sound

class AnimalMoods(object):
	AWAKE = 'Awake'
	SLEEPING = 'Sleeping'

	def __init__(self, mood):
		self.mood = mood

	def __str__(self):
		return self.mood

	def __repr__(self):
		return self.__str__()

class AnimalMoodSounds(object):

	def __init__(self,mood,sound):
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
		self.moodsounds.update({key:moodsound})

	def get_sound(self,mood):
		key = str(mood)
		moodsound = self.moodsounds[key]
		snd = moodsound.sound
		return snd

class Animals(object):
	counter = 0

	def __init__(self):
		self.mood = AnimalMoods(AnimalMoods.AWAKE)

		self.moodsounds = AnimalMoodSoundsCollection()
		moodsound = AnimalMoodSounds(AnimalMoods.SLEEPING, 'zzzz')
		self.moodsounds.add_moodsound(moodsound)
		Animals.counter += 1

	def sound(self):
		snd = self.moodsounds.get_sound(self.mood)
		return snd

	def set_sleep(self):
		self.mood = AnimalMoods(AnimalMoods.SLEEPING)

	def set_awake(self):
		self.mood = AnimalMoods(AnimalMoods.AWAKE)

	@classmethod
	def count(cls):
		return cls.counter

class Cats(Animals):
	counter = 0
	def __init__(self):
		super(Cats,self).__init__()
		moodsound = AnimalMoodSounds(AnimalMoods.AWAKE, 'Miau')
		self.moodsounds.add_moodsound(moodsound)
		Cats.counter += 1
		return


class Sheeps(Animals):
	counter = 0
	def __init__(self):
		super(Sheeps,self).__init__()
		moodsound = AnimalMoodSounds(AnimalMoods.AWAKE, 'Mäh')
		self.moodsounds.add_moodsound(moodsound)
		Sheeps.counter += 1
		return







bruno = Cats()

print(bruno.sound())
bruno.set_sleep()
print(bruno.sound())

fritz = Cats()
minki = Cats()


shaun = Sheeps()
print (shaun.sound())
shaun.set_sleep()
print (shaun.sound())

cnt = Cats.count()
print (Cats.count(), Sheeps.count(), Animals.count())
