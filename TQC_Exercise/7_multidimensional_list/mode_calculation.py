"""
This is a function to calculate the mode in the sample.
Hint: Assume that there is only one mode in the sample.

To run the script::
    $ python mode_calculateion.py
"""


def cal_mode(vals):
    """calculate mode value"""
    elements = set(vals)
    mode_count = 0
    mode_val = 0
    for i in elements:
        count = vals.count(i)
        if count > mode_count:
            mode_val = i
            mode_count = count
    return (mode_val, mode_count)


def main():
    """main"""
    vals = []
    for _ in range(10):
        val = int(input())
        vals.append(val)
    mode_val, mode_count = cal_mode(vals)
    print(mode_val, mode_count, sep="\n")


if __name__ == "__main__":
    main()
