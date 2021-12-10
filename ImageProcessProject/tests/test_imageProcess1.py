import threading

def set_delay(num):
    time = 0
    while time < num:
        time += 1


def imageFunc(imagePath):
    set_delay(100000000)
    print(f'{imagePath} finished')


def workInBackground(imagePath):
    threading.Thread(target=imageFunc, args=(imagePath,)).start()


def imageProcess(imagePath, callback=workInBackground):
    callback(imagePath)


if __name__ == '__main__':
    imagePath = "./img1.png"
    imageProcess(imagePath)
    imagePath = "./img2.png"
    imageProcess(imagePath)
    imagePath = "./img3.png"
    imageProcess(imagePath)
    print(f"adding background {imagePath}")
    for i in range(10):
        print(i)