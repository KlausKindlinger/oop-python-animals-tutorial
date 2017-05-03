class AwakeTimeDuration(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def check_if_in_awake_time_duration(self, time):
		""" Checks if an animal or pet is day- or nightactive"""
		da = self.dayactive(time)
		na = self.nightactive(time)
		if da == True:
			return True
		elif na == True:
			return True
		else:
			return False

	def dayactive(self, time):
		if self.start <= time.time <= self.end:
			return True
		else:
			return False

	def nightactive(self):
		if self.is_nightactive() == True:
			return True
		else:
			return False

	def is_nightactive(self,):
		if self.start > self.end:
			return True
		else:
			return False

	def is_dayactive(self,time):
		if self.start <= time.time <= self.end:
			return True
		else:
			return False
