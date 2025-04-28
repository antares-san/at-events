from animals.animal import Animal

class Fish(Animal):

    def __init__(self, file_name):
        super().__init__(file_name)
        # private member
        self.__is_river_fish = self.data["is_river_fish"]

    # Imlements the abstract move() method of the parent Animal class.
    def move(self):
        print(f"{self.group_name} can swimming")

    # Setter
    @property
    def is_river_fish(self):
        return self.__is_river_fish