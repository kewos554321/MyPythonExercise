"""
It's an implementation of a custom function of image queue.
"""
from myArray import *
from ImageProcess import *


class ImageQueue(object):
    def __init__(self):
        self.queue = myArray()

    def isEmpty(self):
        """Identify whether queue is empty."""
        return self.queue._isEmpty()

    def addToQueue(self, imagePath):
        """Add job to queue"""
        self.queue._insertAt(imagePath, self.queue.length)
        print(f"{imagePath} add to job queue.")
        imageProcess(imagePath)
        self.removeFromQueue(imagePath)
        yield

    def removeFromQueue(self, imagePath):
        """remove job to queue"""
        ind = self.queue._findInd(imagePath)
        if ind != -1:
            self.queue._removeFrom(ind)
        print(f"{imagePath} is removed")
        yield

def main():
    """main"""
    tasks = ImageQueue()
    t1 = tasks.addToQueue("./img1.png")
    t2 = tasks.addToQueue("./img2.png")
    t3 = tasks.removeFromQueue("./img2.png")

    triggers = [t1, t2, t3]
    for i in triggers:
        next(i)

if __name__ == "__main__":
    main()