import time


def set_delay(num):
    time = 0
    while time < num:
        time += 1


def imageFunc(imagePath):
    i = 0
    while True:
        time.sleep(2)
        print(imagePath)
        i += 1
        if i > 5:
            break
        yield
    print(f"{imagePath}'s imageFucn finished")

def imageProcess(imagePath, callback=imageFunc):
    print(f"{imagePath} Start...")
    yield callback(imagePath)
    print(f"{imagePath} Finished...")


if __name__ == '__main__':

    job1 = imageProcess("./img1.png")
    job2 = imageProcess("./img2.png")
    job3 = imageProcess("./img3.png")

    timer1 = next(job1)
    timer2 = next(job2)
    timer3 = next(job3)

    tasks = []
    tasks.append([job1, timer1])
    tasks.append([job2, timer2])
    tasks.append([job3, timer3])

    while tasks:
        for task in tasks:
            try:
                next(task[1])
            except StopIteration:
                try:
                    next(task[0])
                except StopIteration:
                    tasks.remove(task)
