import random


class AnimalSounds(object):
	def __init__(self, sound):
		self.sound = sound

	def __str__(self):
		return self.sound


class AnimalMoods(object):
	AWAKE = 'Awake'
	SLEEPING = 'Sleeping'
	ANGRY = 'Angry'

	def __init__(self, mood):
		self.mood = mood

	def __str__(self):
		return self.mood

	def __repr__(self):
		return self.__str__()


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


class Animals(object):
	counter = 0

	SLEEPING_SOUND = 'zzzz'

	def __init__(self):
		self.mood = AnimalMoods(AnimalMoods.AWAKE)

		self.moodsounds = AnimalMoodSoundsCollection()
		moodsound = AnimalMoodSounds(AnimalMoods.SLEEPING, self.SLEEPING_SOUND)
		self.moodsounds.add_moodsound(moodsound)
		moodsound = AnimalMoodSounds(AnimalMoods.AWAKE, self.AWAKE_SOUND)
		self.moodsounds.add_moodsound(moodsound)
		moodsound = AnimalMoodSounds(AnimalMoods.ANGRY, self.ANGRY_SOUND)
		self.moodsounds.add_moodsound(moodsound)

		Animals.counter += 1

	def sound(self):
		snd = self.moodsounds.get_sound(self.mood)
		return snd

	def set_sleep(self):
		self.mood = AnimalMoods(AnimalMoods.SLEEPING)

	def set_awake(self):
		self.mood = AnimalMoods(AnimalMoods.AWAKE)

	def set_angry(self):
		self.mood = AnimalMoods(AnimalMoods.ANGRY)

	@classmethod
	def count(cls):
		return cls.counter


class Pets(Animals):
	counter = 0

	def __init__(self, name):
		self.name = name

		super(Pets, self).__init__()
		Pets.counter += 1
		return


class Cats(Pets):
	counter = 0

	AWAKE_SOUND = 'Miau'
	ANGRY_SOUND = 'Chhhhh'

	def __init__(self, name):
		super(Cats, self).__init__(name)
		Cats.counter += 1
		return


class Dogs(Pets):
	counter = 0

	AWAKE_SOUND = 'WauWau'
	ANGRY_SOUND = 'Grrrrr'

	def __init__(self, name):
		super(Dogs, self).__init__(name)
		Dogs.counter += 1
		return


class Sheeps(Animals):
	counter = 0

	AWAKE_SOUND = 'Mäh'
	ANGRY_SOUND = 'Blöök'

	def __init__(self):
		super(Sheeps, self).__init__()
		Sheeps.counter += 1
		return


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
		if my_mood == AnimalMoods.AWAKE:
			rv = random.choice(self.awake_sounds)
		else:
			rv = super(Parrots, self).sound()
		return rv


bruno = Cats('Bruno')

print(bruno.sound())
bruno.set_sleep()
print(bruno.sound())

fritz = Cats('Fritz')
minki = Cats('Minki')

shaun = Sheeps()
print(shaun.sound())
shaun.set_sleep()
print(shaun.sound())

cnt = Cats.count()
print(Cats.count(), Dogs.count(), Pets.count(), Animals.count())

bruno.set_angry()
print(bruno.sound())
hondo = Dogs('Hondo')
hondo.set_angry()
print(hondo.sound())
sissi = Cats('Sissi')

polly = Parrots('Polly')
print(polly.sound())
print(polly.sound())
polly.set_angry()
print(polly.sound())
