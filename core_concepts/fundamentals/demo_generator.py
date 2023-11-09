#!/usr/bin/env python3

import re
import sys


def fetch_squares(max_root):
    squares = list()
    for x in range(max_root):
        squares.append(x ** 2)
    return squares


def gen_squares(max_num):
    for num in range(0, max_num):
        yield num ** 2


def gen_token(text):
    start = 0
    end = text.find(" ", start)
    while end > 0:
        token = text[start: end]
        # stop producing token when encounters EOF
        if token == "EOF":
            return
        yield token
        start = end + 1
        end = text.find(" ", start)

    yield text[start:]


def words_in_text(path):
    with open(path) as handle:
        for line in handle:
            line = line.rstrip("\n")  # longest line in the file determine the memory footprint
            for word in line.split():  # bug: line.split() -> does not return a generator obj
                yield word


def words_in_text_improved(path):
    BUFFER_SIZE = 2 ** 20

    def read():
        return handle.read(BUFFER_SIZE)

    def normalize(chunk):
        return chunk.lower().rstrip(',!.\n')

    with open(path) as handle:
        buffer = read()
        start, end = 0, -1
        while True:
            for match in re.finditer(r'[ \t\n+]', buffer):  # blankspace, tab, new line
                end = match.start()
                yield normalize(buffer[start: end])
                start = match.end()
            new_buffer = read()
            if new_buffer == '':
                break  # end of file

            buffer = buffer[end + 1:] + new_buffer
            start, end = 0, -1

    word = normalize(buffer[start:])
    if word != '':
        yield word


def file_hash(path):
    with open(path) as handle:
        print(next(handle))
        print(next(handle))


if __name__ == '__main__':
    MAX = 5

    for num in fetch_squares(MAX):  # bug: what if fetch_squares() returns a list that does not fit into the memory
        print(num, end=" ")

    print("")
    for num in gen_squares(MAX):
        print(num, end=" ")

    for num in gen_squares(MAX):
        print(num, end=" ")

    body = "int main() { return 0; }"
    for token in gen_token(body):
        print(token)

    file = '../poem-simple.txt'

    print("printing all words:", end="\n")
    for word in words_in_text(file):
        print(word)

    print("")
    print("printing all words:", end="\n")
    for word in words_in_text_improved(file):
        print(word)

    file_hash(file)
