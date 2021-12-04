def main():
    val = eval(input("please input a positive integer: "))
    if not val % 2:
        print(f"{val} is an even number.")
    else:
        print(f"{val} is not an even number.")

if __name__ == "__main__":
    main()