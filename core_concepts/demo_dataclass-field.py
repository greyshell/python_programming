#!/usr/bin/env python3


from dataclasses import dataclass, field


@dataclass(frozen=True)
class Subscriber:
    name: str

    def update(self, message):
        return print(f"received message from {self.name}: {message} ")


@dataclass
class Publisher:
    # subscribers: list = field(default_factory=list)
    subscribers: set = field(default_factory=set)

    def register(self, who):
        # self.subscribers.append(who)
        self.subscribers.add(who)

    def unregister(self, who):
        # self.subscribers.remove(who)
        self.subscribers.discard(who)

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
    pub.dispatch("this is dinner time")
