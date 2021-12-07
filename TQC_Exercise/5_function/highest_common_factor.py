"""
This is a function for highest common factor.

To run the script::
    $ python highest_common_factor.py
"""


def compute(valx, valy):
    """
    input x and y value form user
    ouput their highest common factor
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