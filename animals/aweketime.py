class Aweketime(object):
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def has(self,time):
		if self.start <= time.time <= self.end:
			return True
		if self.start > self.end:
			if self.start <= time.time:
				return True
			if time.time <= self.end:
				return True
		return False