"""
This is a function to convert a list to a tuple and show length, max, min, and sum.

To run the script::
    $ python list2tuple_conversion.py
"""

def get_input_val():
    """ get input value"""
    vals = []
    while True:
        val = input()
        if val == "-9999":
            break
        vals.append(int(val))
    return vals

def main():
    """main"""
    vals_1 = get_input_val()
    vals_2 = get_input_val()

    merge = vals_1 + vals_2
    merge2tuple = tuple(merge)
    merge_sorted = sorted(merge)

    print(
        f"Combined tuple before sorting: {merge2tuple}",
        f"Combined list after sorting: {merge_sorted}",
        sep="\n"
     )

if __name__ == "__main__":
    main()
