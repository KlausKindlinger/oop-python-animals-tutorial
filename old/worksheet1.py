from cats import Cats
from sheeps import Sheeps
from dogs import Dogs
from parrots import Parrots

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

newpetlist = [sepp, shaun, bruno, hondo, fritz, minki, polly, shaun, polly]

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
for pet in newpetlist:
	pet.set_awake()
	if isinstance(pet, Pets):
		snd = pet.sound()
		print(snd)
	else:
		pass
