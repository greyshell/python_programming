#!/usr/bin/env python3
# multi channel enhancement

from dataclasses import dataclass, field


class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        return print(f"received message from {self.name}: {message} ")


class Publisher:
    def __init__(self, channels):
        self.channels = {channel: dict() for channel in channels}

    def register(self, channel, who, callback=None):  # callback can be any function or method
        if callback is None:
            callback = who.update  # update() is a default call back method
        subscribers = self.channels[channel]
        subscribers[who] = callback

    def unregister(self, channel, who):
        subscribers = self.channels[channel]
        del subscribers[who]

    def dispatch(self, channel, message):
        subscribers = self.channels[channel]
        for callback in subscribers.values():
            callback(message)


if __name__ == '__main__':
    pub = Publisher(['lunch', 'dinner'])

    bob = Subscriber("Bob")
    alice = Subscriber("Alice")
    tom = Subscriber("Tom")

    pub.register('lunch', bob)
    pub.register('dinner', alice)
    pub.register('lunch', tom)
    pub.register('dinner', tom)

    pub.dispatch('lunch', 'this is lunch time')

    pub.unregister('lunch', tom)
    pub.dispatch('dinner', 'this is dinner time')

    pub.dispatch('lunch', 'this is lunch time')
