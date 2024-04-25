class MinMaxStack:
    def __init__(self):
        self.min_max_stack = []  # maintain the state of min and max
        self.stack = []

    def peek(self):
        # time O(1), space O(1)
        return self.stack[-1]

    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, number):
        new_min_max = {
            "min": number,
            "max": number
        }
        if len(self.min_max_stack) > 0:  # if the stack in not empty
            top_elm = self.min_max_stack[-1]
            new_min_max["min"] = min(number, top_elm["min"])
            new_min_max["max"] = max(number, top_elm["max"])

        self.min_max_stack.append(new_min_max)
        self.stack.append(number)

    def get_min(self):
        # peek the top element
        top_elm = self.min_max_stack[-1]
        return top_elm["min"]

    def get_max(self):
        top_elm = self.min_max_stack[-1]
        return top_elm["max"]

