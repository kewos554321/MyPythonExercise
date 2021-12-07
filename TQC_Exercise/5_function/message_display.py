"""
This is a function for message display.

To run the script::
    $ python message_display.py
"""


def compute():
    """
    input department, student id and name form user
    ouput them
    """
    info = []
    for _ in range(3):
        user_ip = input()
        info.append(user_ip)

    print(
        f"Department: {info[0]}",
        f"Student ID: {info[1]}",
        f"Name: {info[2]}",
        sep="\n"
    )


def main():
    """main"""
    compute()


if __name__ == "__main__":
    main()
