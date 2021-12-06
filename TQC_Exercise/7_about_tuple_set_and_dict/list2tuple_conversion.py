"""
This is a function to merge two tuples then sort.
And the ouput show the tuple that before sort and the list that after sort.

To run the script::
    $ python merge_tuples_and_sort.py
"""

def main():
    """main"""
    vals = []
    while True:
        val = input()
        if val == "-9999":
            break
        vals.append(int(val))

    vals2tuple = tuple(vals)
    print(vals2tuple)
    print(
        f"Length: {len(vals2tuple)}",
        f"Max: {max(vals2tuple)}",
        f"Min: {min(vals2tuple)}",
        f"Sum: {sum(vals2tuple)}",
        sep="\n"
     )

if __name__ == "__main__":
    main()
