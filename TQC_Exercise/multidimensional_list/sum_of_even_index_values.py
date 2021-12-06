"""
This a function to sum even values.

To run the script::
    $ python sum_of_even_index_values.py
"""


def sum_even_values(vals):
    """sum even values"""
    total = 0
    for i in vals:
        total += i
    return total


def main():
    """main"""
    ind = 0
    vals = []
    even_vals = []
    while ind < 12:
        val = int(input())
        vals.append(val)
        if not val % 2:
            even_vals.append(val)
        ind += 1
    total = sum_even_values(even_vals)
    for i in range(0, len(vals), 3):
        print(f"{vals[i]:>3d}{vals[i+1]:>3d}{vals[i+2]:>3d}\n")
    print(f"{total:>3d}\n")


if __name__ == "__main__":
    main()
