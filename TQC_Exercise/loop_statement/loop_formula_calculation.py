"""
This a function is for formula calculation.
input is a grater than 1 number and ouput is a number, too.
The formula is 11+2+12+3+…+1n−1+n


To run the script::
    $ python loop_formula_calculation.py
"""


def cal_formula(num):
    """calculate the formula"""
    result = 0
    i = 2
    while i <= num:
        val = 1/((i-1)**0.5 + i**0.5)
        result += val
        i += 1
    return result


def main():
    """main"""
    num = int(input())
    result = cal_formula(num)
    print(f"{result:.4f}")


if __name__ == "__main__":
    main()
