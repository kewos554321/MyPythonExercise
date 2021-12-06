"""
This a function is for factorical calculation.
And ouput is a number.

To run the script::
    $ python loop_factorial_calculation.py
"""


def cal_factorial(num):
    """calculate the factorical number"""
    result = 1
    i = 1
    while i <= num:
        result *= i
        i += 1
    return result


def main():
    """main"""
    num = int(input())
    result = cal_factorial(num)
    print(result)


if __name__ == "__main__":
    main()
