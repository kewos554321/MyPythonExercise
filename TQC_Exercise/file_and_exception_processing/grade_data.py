"""
write the five data from input to write.txt

To run the script::
    $ python grade_data.py
"""

def main():
    """main"""
    fop = open('write.txt', 'w', encoding="utf-8")
    for _ in range(5):
        state = input()
        fop.write(f"{state}\n")
    fop.close()


if __name__ == "__main__":
    main()
