

def convert_hour(sec, min):
    sec2min = float(sec) / 60
    min2hour = (sec2min + min) / 60
    return min2hour

def convert_mile(kilo):
    return kilo * (10 / 16)

def calculate_average_milespeed(min, sec, kilo):
    h = convert_hour(sec, min)
    mile = convert_mile(kilo)
    return mile / h

def main():
    min = eval(input("please input minute: "))
    sec = eval(input("please input second: "))
    kilo = eval(input("please input kilometer: "))
    result = calculate_average_milespeed(min, sec, kilo)
    print(f"Speed = {result:.1f}\n")
if __name__ == "__main__":
    main()
