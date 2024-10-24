import pickle
import pickletools


class Test:
    """
    fix: try to save the state of an object using pickle where some
    properties of that object will not be serialized
    for example: open file descriptor
    """

    # fix the above code
    def __init__(self, file_path="test.txt"):
        # Used later in __reduce__
        self._file_path = file_path
        # An open file in write mode
        self.fd = open(self._file_path, 'wb')

    def __reduce__(self):
        # we return a tuple of class_name to call,
        # and optional parameters to pass when re-creating
        return self.__class__, (self._file_path,)


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
