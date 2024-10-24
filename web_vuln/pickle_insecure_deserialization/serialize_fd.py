import pickle
import pickletools


class Test:
    """
    try to save the state of an object using pickle where some
    properties of that object will not be serialized
    for example: open file descriptor
    """
    def __init__(self, file_path="test.txt"):
        self.fd = open(file_path, 'wb')


if __name__ == '__main__':
    my_test = Test()
    # Now, watch what happens when we try to pickle this object:

    stream_of_bytes = pickle.dumps(my_test)

    print(f"bytes: {stream_of_bytes}")

    # write the state of the user obj into a file
    file_path = 'my_test.pkl'
    with open(file_path, 'wb') as f:
        pickle.dump(my_test, f)

    print(f"{pickletools.dis(stream_of_bytes)}")
