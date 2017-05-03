class Animal(object):
	def __init__(self):
		self.status = 'Awake'

	def sound(self):
		if self.status == 'Awake':
			return self.sleepy_sound()
		else:
			return self.awake_sound()

	def set_sleep(self):
		self.status = 'Sleeping'

	def set_awake(self):
		self.status = 'Awake'

	def sleepy_sound(self):
		return "zzzz"

	def awake_sound(self):
		return "Miau"


class Cat(Animal):
	pass

class Sheep(Animal):

	def awake_sound(self):
		return "Mäh"






bruno = Cat()

print(bruno.sound())
bruno.set_sleep()
print(bruno.sound())

shaun = Sheep()
print (shaun.sound())
shaun.set_sleep()
print (shaun.sound())