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

    # look up: method 1
    try:
        dept = name_dept["no_key"]  # throws exception when the key is not found
        print(f"{dept}")
    except KeyError as e:
        print(f"error: {e}")

    # look up: method 2
    if "no_key" in name_dept:  # inefficient because it queries the dict twice
        dept = name_dept["no_key"]
        print(f"{dept}")

    # look up: method 3 (recommended)
    dept = name_dept.get("alice", "no_key")  # provides the support for default value
    print(f"{dept}")

    # add items


if __name__ == '__main__':
    main()
