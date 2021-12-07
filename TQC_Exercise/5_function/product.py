"""
This is a function for product of two values.

To run the script::
    $ python product.py
"""


def compute(valx, valy):
    """
    input x and y value form user
    ouput their multiplication
    """
    return valx * valy


def main():
    """main"""
    valx = int(input())
    valy = int(input())
    result = compute(valx, valy)
    print(result)


if __name__ == "__main__":
    main()
