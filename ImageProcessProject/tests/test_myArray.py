"""
a test for queue(FIFO)
"""
import sys

class Array(object):
    def __init__(self):
        self.arr = []
        self.length = 0

    def _isEmpty(self):
        return self.length == 0

    def _insertAt(self, elem, ind):
        if self._isEmpty():
            self.arr = self.arr + [None]
            self.arr[ind] = elem
        else:
            self.arr = self.arr + [None]
            i = self.length
            while i >= ind:
                self.arr[i] = self.arr[i-1]
                i -= 1
            self.arr[ind] = elem
        self.length += 1

    def _removeFrom(self, ind):
        if self._isEmpty():
            return 0
        del self.arr[ind]
        self.length -= 1

    def _show(self, ind):
        print(self.arr[ind])

    def _findInd(self, elem):
        ind = self.length - 1
        while True:
            if ind == -1:
                return ind
            elif self.arr[ind] == elem:
                return ind
            ind -= 1


if __name__ == "__main__":
    A = Array()
    A.insertAt(12, 0)
    A.insertAt(23, 1)
    A.insertAt(34, 2)
    A.insertAt(45, 3)
    print(f"now this arr = {A.arr}")
    print(f"now this arr's length = {A.length}")
    print("--------")

    A.insertAt(56, 1)
    print(f"after insert and now this arr = {A.arr}")
    print(f"after insert and now this arr's length = {A.length}")
    A.show(1)
    print("--------")

    A.removeFrom(2)
    print(f"after remove and now this arr = {A.arr}")
    print(f"after remove and now this arr's length = {A.length}")
    A.show(1)
    print("--------")
    
    print(A.isEmpty())
    A.removeFrom(0)
    A.removeFrom(0)
    A.removeFrom(0)
    A.removeFrom(0)
    print(A.isEmpty())

