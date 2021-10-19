def receive_and_print():
    print('starting')
    while True:
        payload = yield
        print(f"RECEIVED: {payload}")


if __name__ == '__main__':
    gen_receiver = receive_and_print()
    next(gen_receiver)  # prime the co-routine, suspend the run
    gen_receiver.send("hello")
    gen_receiver.send("guys")
    gen_receiver.close()
