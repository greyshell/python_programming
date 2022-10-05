#!/usr/bin/env python3

class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        return print(f"received message from {self.name}: {message} ")


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)  # If the element passed to remove() doesn't exist, KeyError exception is thrown.

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)  # drawback: all subscriber need to have update method


if __name__ == "__main__":
    pub = Publisher()
    bob = Subscriber("Bob")
    alice = Subscriber("Alice")
    tom = Subscriber("Tom")

    pub.register(bob)
    pub.register(alice)
    pub.register(tom)

    pub.dispatch("this is lunch time")

    pub.unregister(tom)
    pub.unregister(alice)
    pub.dispatch("this is dinner time")  # alice will not get the message
