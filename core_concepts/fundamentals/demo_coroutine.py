# author: greyshell

def gen_squares(max_root):
    squares = list()
    for x in range(max_root):
        squares.append(x ** 2)
    return squares


def gen_squares_improved(max_root):
    for num in range(0, max_root):
        yield num ** 2


def receive_and_print():
    print('STARTING')
    while True:
        payload = yield
        print(f"RECEIVED: {payload}")


def receive_and_print_v2():
    print('STARTING')
    try:
        while True:
            payload = yield
            print(f"RECEIVED: {payload}")
    except GeneratorExit:
        # clean up action is needed before closing the generator object
        print("CLOSING")


def receive_and_print_v3():
    """common pattern / best practice: finally block is used for clean up"""
    print('STARTING')
    try:
        while True:
            payload = yield
            print(f"RECEIVED: {payload}")
    # here we are not catching the exception
    finally:
        # but clean up action is needed before closing the generator object
        print("CLOSING")


def receive_and_print_v4():
    """throw an exception into the coroutine"""
    print('STARTING')
    while True:
        try:
            payload = yield
        except ValueError:
            # clean up action is needed before closing the generator object
            payload = "[INVALID]"
        print(f"RECEIVED: {payload}")


if __name__ == '__main__':
    # recap the generator concept
    # when a function has the "yield statement" or "yield expression" then we can call it as generator function
    # generator funciton returns generator object
    print("")
    MAX = 3

    out = gen_squares(MAX)  # starts from 0 to MAX
    print(type(out))

    # gen_squares() is a normal function
    # transfer of data -> one way: data is sent from gen_squares() to the for loop (ignore calling 1st time with arg)
    # transfer / flow of control: one way
    for num in gen_squares(MAX):
        print(num, end=" ")
    # drawback of this approach: if the returned list does not fit into the memory

    # improved code using generator
    print()
    out = gen_squares_improved(MAX)
    print(type(out))
    # fetching each items
    print(out.__next__())
    print(out.__next__())
    print(out.__next__())
    # print(out.__next__())  # throw an exception as nothing to fetch

    # transfer  of control -> two way: seems like two threads are cooperating and transfering controls to each other
    # flow of control -> bouncing between the generator function and the for loop
    # transfer of data -> one way: data is only sent from gen_squares_improved() to the for loop
    for num in gen_squares_improved(MAX):  # for intern called the __next__() and put the val in num
        print(num, end=" ")

    # coroutine concept -> it is a special generator function having yield expression
    # like normal function, it can send the data back to the consumer function / caller
    # however, consumer function / caller can also send the data back into the coroutine
    # transfer of data and transfer of control -> both ways

    print()
    gen_receiver = receive_and_print()
    # one time process to start the execution of the generator function body. this is called "prime the coroutine"
    next(gen_receiver)
    gen_receiver.send("hey")
    gen_receiver.send("yay")
    gen_receiver.close()  # send the signal to exit the generator
    print("done")

    # exit the generator and catch the exception
    gen_receiver = receive_and_print_v2()
    # one time process to start the execution of the generator function body. this is called "prime the coroutine"
    next(gen_receiver)
    gen_receiver.send("hey")
    gen_receiver.send("yay")
    # send the signal to exit the generator -> raise exception = GeneratorExit
    gen_receiver.close()  # jump to the end of the function if try / except is not defined

    print()
    gen_receiver_v2 = receive_and_print_v3()
    next(gen_receiver_v2)  # prime the co-routine due to lazy evaluation
    gen_receiver_v2.send("hey")
    gen_receiver_v2.send("yay")
    # send the signal to exit the generator,
    gen_receiver_v2.close()  # jump to the end of the function if try / except is not defined

    print()
    # in normal situation, a function / coroutine can raise exception that the caller must handle it.
    # however, due to bidirectional nature, caller can throw an exception into the coroutine
    gen_receiver_v3 = receive_and_print_v4()
    next(gen_receiver_v3)  # prime the co-routine due to lazy evaluation
    gen_receiver_v3.send("hey")
    gen_receiver_v3.send("yay")
    # send the signal to exit the generator,
    gen_receiver_v3.throw(ValueError)  # argument is exception type
