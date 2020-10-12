# !/usr/bin/env python3

# author: greyshell
# description: play with dict


def main():
    """
    - TBD
    :return:
    """
    # create a empty dict
    a = {}
    d = dict()

    # initialise
    name_dept = {
        "alice": "cse",
        "bob": "ee",
        "carol": "it"
    }

    print(f"{name_dept}")  # ordered structure

    # look up: method 1
    try:
        dept = name_dept["no_key"]  # throws exception when the key is not found
        print(f"{dept}")
    except KeyError as e:
        print(f"error: {e}")

    # look up: method 2
    if "key" in name_dept:  # inefficient because it queries the dict twice
        dept = name_dept["no_key"]
        print(f"{dept}")

    # look up: method 3 (recommended)
    dept = name_dept.get("alice", "no_key")  # provides the support for default value
    print(f"{dept}")

    # get all keys
    print(f"{name_dept.keys()}")  # retuens a object
    # get all values
    print(f"{name_dept.values()}")  # returns a object
    # get key and values in tuple format
    print(f"{name_dept.items()}")  # returns a list, each entry is tuple

    # print the dict: method 1
    for key, value in name_dept.items():  # unpacks the tuples
        print(f"{key}: {value}")

    # print the dict: method 2
    for key in name_dept:  # __iter__() => iterates over the keys, similar to name_dept.keys()
        print(f"{key}: {name_dept[key]}")


if __name__ == '__main__':
    main()
