def dis(self):
    for attr, value in self.__dict__.items():
        print(f"{attr}: {value}")

Pet = type('Pet', (), {'dis': dis})


my_pet = Pet()
my_pet.name = 'Tom'
my_pet.age = 3


my_pet.dis()
