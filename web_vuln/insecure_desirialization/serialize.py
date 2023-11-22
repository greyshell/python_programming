#!/usr/bin/env python3

import pickle
import pickletools


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def summary(self):
        """provides the summay of the object"""
        return f"{self.name} is {self.age} years old"


if __name__ == '__main__':
    # create a user obj
    user = User("Joker", 40)
    stream_of_bytes = pickle.dumps(user)
    print(f"bytes: {stream_of_bytes}")

    # write the state of the user obj into a file
    file_path = 'user.pkl'
    with open(file_path, 'wb') as f:
        pickle.dump(user, f)

    # inspect the byte stream
    print(f"{pickletools.dis(stream_of_bytes)}")
