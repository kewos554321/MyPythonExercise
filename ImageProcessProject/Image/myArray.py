"""
It's an implementation of a custom class of Array.
a test for queue(FIFO)
"""


class myArray(object):
    def __init__(self):
        self.arr = []
        self.length = 0

    def _isEmpty(self):
        """Identify whether arr is empty."""
        return self.length == 0

    def _insertAt(self, elem, ind):
        """
        Insert an element at a specific location.
        Move the behind elements backward.
        """
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
        """
        Remove an element at a specific location.
        Move the behind elements forward.
        """
        if self._isEmpty():
            return 0
        del self.arr[ind]
        self.length -= 1

    def _show(self, ind):
        """Print an element at a specific location."""
        print(self.arr[ind])

    def _findInd(self, elem):
        ind = self.length - 1
        while True:
            if ind == -1:
                return ind
            elif self.arr[ind] == elem:
                return ind
            ind -= 1
