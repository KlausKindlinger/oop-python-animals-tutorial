class Aweketime(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def has(self):
		da = self.dayactive()
		na = self.nightactive()
		if da or na == True:
			return True
		else:
			return False

#	def timeset(self, time):
#		if self.start <= time.time <= self.end:
#			return True
#		else:
#			return False

	def dayactive(self,time):
		if self.start <= time.time <= self.end:
			return True
		else:
			return False


	def nightactive(self,time):
		if self.start > self.end:
			if self.start <= time.time:
				return True
			if time.time <= self.end:
				return True
		else:
			return False