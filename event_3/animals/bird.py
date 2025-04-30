from animals.animal import Animal


class Bird(Animal):

    def __init__(self, group_name):
        super().__init__(group_name)
        # private member
        self.__can_fly = True

    # Imlements the abstract move() method of the parent Animal class.
    def move(self):
        print(f"{self.group_name} can flying")


    # Setter
    @property
    def can_fly(self):
        return self.__can_fly
    
    def __str__(self):
        return f"It's a {self.group_name}"
