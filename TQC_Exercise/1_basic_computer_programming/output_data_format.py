def output_integer_format():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # print("|%5d %5d|" %(a, b))
    # print("|%5d %5d|" %(c, d))
    # print("|%-5d %-5d|" %(a, b))
    # print("|%-5d %-5d|" %(c, d))

    print(f"|{a:>5d}{b:>5d}|")
    print(f"|{c:>5d}{d:>5d}|")
    print(f"|{a:<5d}{b:<5d}|")
    print(f"|{c:<5d}{d:<5d}|")

def output_float_format():
    a = eval(input())
    b = eval(input())
    c = eval(input())
    d = eval(input())

    print(f"|{a:>7.2f}{b:>7.2f}|")
    print(f"|{c:>7.2f}{d:>7.2f}|")
    print(f"|{a:<7.2f}{b:<7.2f}|")
    print(f"|{c:<7.2f}{d:<7.2f}|")

def output_string_format():
    a = input()
    b = input()
    c = input()
    d = input()

    print(f"|{a:>10s} {b:>10s}|")
    print(f"|{c:>10s} {d:>10s}|")
    print(f"|{a:<10s} {b:<10s}|")
    print(f"|{c:<10s} {d:<10s}|")

if __name__ == "__main__":
    output_integer_format()
    output_float_format()
    output_string_format()