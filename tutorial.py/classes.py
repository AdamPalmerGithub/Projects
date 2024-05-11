class Animal:
    def __init__(self, sound) -> None:
        self.sound = sound

        def make_sound(self):
            return f"The {type(self).__name__} goes {self.sound}"
        

class Lion(Animal):
    pass


class Canary(Animal):
    pass


class Goldfish(Animal):
    pass


lion = Lion("rawr")
bird = Canary("tweet")
fish = Goldfish("Blub")

print(lion.make_sound())
print(bird.make_sound())
print(fish.make_sound())
