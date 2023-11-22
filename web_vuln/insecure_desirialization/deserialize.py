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
    # load the file
    file_path = 'user.pkl'
    with open(file_path, 'rb') as f:
        user = pickle.load(f)

    print(f"{user}")
    print(f"{user.summary()}")
