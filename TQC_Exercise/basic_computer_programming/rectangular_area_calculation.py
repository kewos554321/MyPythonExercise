
def calculate_perimeter(h, w):
    return (w + h) * 2

def calculate_area(h, w):
    return h * w

def main():
    h = eval(input())
    w = eval(input())
    area = calculate_area(h, w)
    perimeter = calculate_perimeter(h, w)
    print(f"Height = {h:.2f}\n")
    print(f"Width = {w:.2f}\n")
    print(f"Perimeter = {perimeter:.2f}\n")
    print(f"Area = {area:.2f}\n")

if __name__ == "__main__":
    main()