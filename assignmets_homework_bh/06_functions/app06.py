#06_is_odd.
#10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd...

def is_odd(value: int) -> bool:
    """
    Checks if a value is odd.
    Returns True if the value is odd, False otherwise.
    """
    return value % 2 == 1

def main():
    for i in range(10):
        print(f"{i} is {'odd' if is_odd(i) else 'even'}")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
