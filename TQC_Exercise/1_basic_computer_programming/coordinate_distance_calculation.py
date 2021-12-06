


def calculate_coordinatedistance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def main():
    x1 = eval(input("please input coordinate-x1: "))
    y1 = eval(input("please input coordinate-y1: "))
    x2 = eval(input("please input coordinate-x2: "))
    y2 = eval(input("please input coordinate-y2: "))
    result = calculate_coordinatedistance(x1, y1, x2, y2)
    print(f"( {x1} {y1} )")
    print(f"( {x2} {y2} )")
    print(f"Distance = {result:.4f}\n")
if __name__ == "__main__":
    main()