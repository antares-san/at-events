from animals.animal import Animal

class Fish(Animal):

    def __init__(self, group_name):
        super().__init__(group_name)
        # private member
        self.__is_river_fish = False

    # Imlements the abstract move() method of the parent Animal class.
    def move(self):
        print(f"{self.group_name} can swimming")

    # Getter
    @property
    def is_river_fish(self):
        return self.__is_river_fish
    
    # Setter
    @is_river_fish.setter
    def is_river_fish(self, value):
        self.__is_river_fish = value