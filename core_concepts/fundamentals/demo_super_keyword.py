class Dog:
    sound = "woof"

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.sound}"


class BigDog(Dog):
    sound = "abc"

    def speak(self):
        return super().sound.upper()
        # return super().speak().upper()


if __name__ == "__main__":
    d = Dog('jacky')
    print(d.speak())

    c = BigDog('tommy')
    print(c.speak())
