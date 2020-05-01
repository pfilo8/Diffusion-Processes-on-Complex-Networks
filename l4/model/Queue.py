class Queue:
    """ Klasa reprezentująca kolejkę."""

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
        return self.items[-1]
