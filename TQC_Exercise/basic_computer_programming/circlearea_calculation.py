
import math

def calculate_perimeter(r, pi):
    return 2 * pi * r

def calculate_area(r, pi):
    return pi * r * r

def main():
    r = eval(input())
    pi = math.pi
    area = calculate_area(r, pi)
    perimeter = calculate_perimeter(r, pi)
    
    print(f"Radius = {r:.2f}\n")
    print(f"Perimeter = {perimeter:.2f}\n")
    print(f"Area = {area:.2f}\n")

if __name__ == "__main__":
    main()
    

