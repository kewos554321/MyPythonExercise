import sys
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

Node(1).get_data()
sys.exit()
Node.get_data()
Node.get_next()
Node.set_data(2)
Node.set_next(3)
Node.set_next(4)
