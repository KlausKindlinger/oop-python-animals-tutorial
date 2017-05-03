from cats import Cats
from sheeps import Sheeps
from dogs import Dogs
from parrots import Parrots
from bats import Bats

from mytime import MyTime

sepp = Cats('Sepp')
bruno = Cats('Bruno')
hondo = Dogs('Hondo')
fritz = Cats('Fritz')
minki = Cats('Minki')
sissi = Cats('Sissi')
polly = Parrots('Polly')


print(bruno.sound())
bruno.set_sleep()
print(bruno.sound())
shaun = Sheeps()
print(shaun.sound())
shaun.set_sleep()
print(shaun.sound())
cnt = Cats.count()
bruno.set_angry()
print(bruno.sound())
hondo.set_angry()
print(hondo.sound())
print(polly.sound())
polly.set_angry()
print(polly.sound())

dracula = Bats()

newpetlist = [sepp, dracula, shaun, bruno, hondo, fritz, minki, polly, shaun, polly]

print("===<0>===")

for pet in newpetlist:
	pet.set_awake()
	try:
		name = pet.name
		snd = pet.sound()
		print(snd)
	except AttributeError:
		pass

print("===<1>===")

for pet in newpetlist:
	pet.set_awake()
	if hasattr(pet, 'name'):
		snd = pet.sound()
		print(snd)

print("===<2>===")

from pets import Pets

my_time = MyTime()

for pet in newpetlist:
	pet.set_mood_from_time(my_time)
	if isinstance(pet, Pets):
		snd = pet.sound()
		print(snd)
	else:
		pass

print("===<3>===")

