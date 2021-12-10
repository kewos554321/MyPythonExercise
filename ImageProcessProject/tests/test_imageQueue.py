import time
from test_Array import *

def set_delay(num):
    time = 0
    while time < num:
        time += 1

def imageFunc(imagePath):
    i = 0
    while True:
        time.sleep(2)
        i += 1
        print(f"Run {imagePath} {i}")
        if i > 5:
            break
        # yield
    print(f"{imagePath}'s imageFucn finished")

def imageProcess(imagePath, callback=imageFunc):
    print(f"{imagePath} Start...")
    # yield callback(imagePath)
    callback(imagePath)
    print(f"{imagePath} Finished...")


class imageQueue(object):
    def __init__(self):
        self.queue = Array()

    def isEmpty(self):
        return self.queue._isEmpty()

    def addToQueue(self, imagePath):
        self.queue._insertAt(imagePath, self.queue.length)
        imageProcess(imagePath)
        self.removeFromQueue(imagePath)
        yield 

    def removeFromQueue(self, imagePath):
        ind = self.queue._findInd(imagePath)
        if ind != -1:
            self.queue._removeFrom(ind)
        yield

def main():
    tasks = imageQueue()
    t1 = tasks.addToQueue("./img1.png")
    t2 = tasks.addToQueue("./img2.png")
    t3 = tasks.removeFromQueue("./img2.png")

    traggers = [t1, t2, t3]
    for i in traggers:
        next(i)

if __name__ == "__main__":
    main()
