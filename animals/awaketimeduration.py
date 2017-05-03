class AwakeTimeDuration(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def check_if_in_awake_time_duration(self, time):
		if self.is_dayactive():
			status = self._time_in_day_duration(time)
			return status
		else:
			status = self._time_in_night_duration(time)
			return status

	def _time_in_day_duration(self,time):
		if self.start <= time.time <= self.end:
			return True
		return False

	def _time_in_night_duration(self, time):
		if self.end < time.time < self.start:
			return False
		return True

	def is_nightactive(self):
		if self.start > self.end:
			return True
		else:
			return False

	def is_dayactive(self):
		return not self.is_nightactive()
