"""
It's an implementation of a custom function of imageProcess.
"""


def set_delay(num):
    """Delay for a while"""
    time = 0
    while time < num:
        time += 1


def imageFunc(imagePath):
    """simulate image function"""
    if imagePath != "":
        set_delay(100000000)


def imageProcess(imagePath, callback=imageFunc):
    """simulate image processing"""
    print(f"{imagePath} processing...")
    callback(imagePath)
    print(f"{imagePath} finished...")
