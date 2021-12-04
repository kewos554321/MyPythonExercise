"""
This a function to do continuous addition.

To run the script::
    $ python integer_continuous_addition.py
"""

def main():
    """main"""
    val1 = int(input())
    val2 = int(input())
    result = 0
    for i in range(val1, val2+1):
        result+=i
    print(result)

if __name__ == "__main__":
    main()
