class AwakeTimeDuration(object):
	""" This class is the duration during a day, where an animal
	     is awake
	"""
	
	def __init__(self, start, end):
		""" Constructor
		@param self: pointer to myself
		@param start: hour when the animal awakes
		@param end: hour when the animal falls asleep
		Note: An animal is nightactive if it awakes later on a day than it falls asleep
		"""
		self.start = start
		self.end = end

	def check_if_in_awake_time_duration(self, time):
		""" Check if the parameter time is within the awake time of this duration.
		@param self: pointer to myself
		@param time: The time to check
		"""
		if self.is_dayactive():
			status = self._time_in_day_duration(time)
			return status
		else:
			status = self._time_in_night_duration(time)
			return status

	def _time_in_day_duration(self,time):
		""" Is a given time in my awake timespan for day-active animals?
		@param self: pointer to myself
		@param time: The time to check
		"""
		if self.start <= time.time <= self.end:
			return True
		return False

	def _time_in_night_duration(self, time):
		""" Is a given time in my awake timespan for night-active animals?
		@param self: pointer to myself
		@param time: The time to check
		"""	
		if self.end < time.time < self.start:
			return False
		return True

	def is_nightactive(self):
		""" Is this a night-active duration?
		@param self: pointer to myself
		"""
		if self.start > self.end:
			return True
		else:
			return False

	def is_dayactive(self):
		""" Is this a day-active duration?
		@param self: pointer to myself
		"""
		return not self.is_nightactive()
