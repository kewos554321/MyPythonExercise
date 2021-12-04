def main():
    a = eval(input("please input a positive integer: "))
    b = eval(input("please input an another positive integer: "))
    o = input("please input an arithmetic operator: ")

    if o == '+':
        print(a + b)
    elif o == '-':
        print(a - b)
    elif o == '*':
        print(a * b)
    elif o == '/':
        print(a / b)
    elif o == '//':
        print(a // b)
    elif o == '%':
        print(a % b)

if __name__ == "__main__":
    main()