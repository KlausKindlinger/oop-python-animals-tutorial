from .animalmoods import AnimalMoods
from .animalsounds import AnimalMoodSounds, AnimalMoodSoundsCollection
from .animalmoods import AWAKE, SLEEPING, ANGRY
from .awaketimeduration import AwakeTimeDuration


class Animals(object):
	counter = 0

	SLEEPING_SOUND = 'zzzz'

	def __init__(self):
		self.mood = AnimalMoods(AWAKE)

		self.moodsounds = AnimalMoodSoundsCollection()
		moodsound = AnimalMoodSounds(SLEEPING, self.SLEEPING_SOUND)
		self.moodsounds.add_moodsound(moodsound)
		moodsound = AnimalMoodSounds(AWAKE, self.AWAKE_SOUND)
		self.moodsounds.add_moodsound(moodsound)
		moodsound = AnimalMoodSounds(ANGRY, self.ANGRY_SOUND)
		self.moodsounds.add_moodsound(moodsound)

		self.aweketime = AwakeTimeDuration(8, 20)

		Animals.counter += 1

	def awake_time(self, start, end):
		self.aweketime = AwakeTimeDuration(start, end)
		return

	def sound(self):
		snd = self.moodsounds.get_sound(self.mood)
		return snd

	def set_sleep(self):
		self.mood = AnimalMoods(SLEEPING)

	def set_awake(self):
		self.mood = AnimalMoods(AWAKE)

	def set_angry(self):
		self.mood = AnimalMoods(ANGRY)

	def set_mood_from_time(self, time):
		if self.aweketime.check_if_in_awake_time_duration(time):
			self.set_awake()
		else:
			self.set_sleep()

	@classmethod
	def count(cls):
		return cls.counter
