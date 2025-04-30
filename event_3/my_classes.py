from animals.mammal import Mammal
from animals.bird import Bird
from animals.animal import Animal
from animals.fish import Fish



dog = Mammal("Dog")
dog.move()
print(dog)
dog.animal_name = "Kashtanka"
print(dog)


dove = Bird("Dove")
dove.move()
print(dove)

perch = Fish("Perch")
perch .move()
print(perch)
print(perch.is_river_fish)

print("Animal count:", Animal.counter)




