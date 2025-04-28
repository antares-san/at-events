from animals.animal import Animal

class Mammal(Animal):

    def __init__(self, file_name):
        super().__init__(file_name)
        # private member
        self.__animal_name = self.data["animal_name"]

    def __to_str__(self):
        return f"The {self.group_name} named {self.animal_name}. The {self.group_name}'s breed is {self.animal_type}"

    # Imlements the abstract move() method of the parent Animal class.
    def move(self):
        print(f"{self.animal_type} {self.animal_name} can running")

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