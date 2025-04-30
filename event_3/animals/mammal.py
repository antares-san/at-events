from animals.animal import Animal

class Mammal(Animal):

    def __init__(self,  group_name):
        super().__init__(group_name)
        # private member
        self.__animal_name = "noname"


    def __to_str__(self):
        return f"The {self.group_name} named {self.animal_name}"

    # Imlements the abstract move() method of the parent Animal class.
    def move(self):
        print(f"{self.group_name} {self.animal_name} can running")

    # Getter
    @property
    def animal_name(self):
        return self.__animal_name
    
    # Setter 
    @animal_name.setter
    def animal_name(self, value):
        self.__animal_name = value
    
    def __str__(self):
        return self.__to_str__()

    def __repr__(self):
        return self.__to_str__()