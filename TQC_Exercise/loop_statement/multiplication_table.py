"""
This a function to create multiplication_table.

To run the script::
    $ python multiplication_table.py
"""

def main():
    """main"""
    num = int(input())
    table = []*num
    for i in range(num):
        i+=1
        for j in range(num):
            j+=1
            print(f"{j:<2d}* {i:<2d}= {i*j:<4d}", end="")
        print("\n")

if __name__ == "__main__":
    main()