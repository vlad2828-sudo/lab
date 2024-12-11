class Bird:
    def fly(self):
        raise NotImplementedError("Метод має бути реалізований у підкласі")

# Підкласи
class Sparrow(Bird):
    def fly(self):
        print("Горобець летить")

class Penguin(Bird):
    def fly(self):
        print("Пінгвіни не літають")  # Це порушує LSP

# тестування
def make_bird_fly(bird: Bird):
    bird.fly()


sparrow = Sparrow()
make_bird_fly(sparrow)  # "меток"
