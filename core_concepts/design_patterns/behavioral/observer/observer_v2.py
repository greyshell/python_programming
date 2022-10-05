#!/usr/bin/env python3


class SubscriberOne:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        return print(f"received message from {self.name}: {message} ")


class SubscriberTwo:

    def __init__(self, name):
        self.name = name

    def receive(self, message):
        return print(f"received message from {self.name}: {message} ")


class Publisher:
    def __init__(self):
        self.subscribers = dict()  # key: subscriber, value: callback function object

    def register(self, who, callback=None):  # callback can be any function object but have same signature
        if callback is None:
            callback = who.update  # update() is a default call back method
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispatch(self, message):
        for callback in self.subscribers.values():
            callback(message)


if __name__ == "__main__":
    pub2 = Publisher()
    bob = SubscriberOne("Bob")
    alice = SubscriberTwo("Alice")

    pub2.register(bob)
    pub2.register(alice, alice.receive)

    pub2.dispatch("this is lunch time")

    pub2.unregister(bob)
    pub2.dispatch("this is dinner time")  # bob will not get the notification
