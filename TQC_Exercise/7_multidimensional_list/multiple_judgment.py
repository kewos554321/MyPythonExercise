def main():
    val = eval(input("please input a positive integer: "))
    if not val % 15:
        print(f"{val} is a multiple of 3 or 5.")
    elif not val % 3:
        print(f"{val} is a multiple of 3.")
    elif not val % 5:
        print(f"{val} is a multiple of 5.")
    else:
        print(f"{val} is not a multiple of 3 or 5.")


if __name__ == "__main__":
    main()
