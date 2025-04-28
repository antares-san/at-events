from animals.mammal import Mammal
from animals.bird import Bird
from animals.animal import Animal
from animals.fish import Fish


config_path = "event_3/data"


dog = Mammal(f"{config_path}/dog.json")
dog.move()
print(dog)
dog.animal_name = "Kashtanka"
print(dog)


dove = Bird(f"{config_path}/dove.json")
dove.move()
print(dove)

perch = Fish(f"{config_path}/fish.json")
perch .move()
print(perch)
print(perch.is_river_fish)

# You can't create an instance of an abstract class
# animal = Animal(f"{config_path}/dove.json")



