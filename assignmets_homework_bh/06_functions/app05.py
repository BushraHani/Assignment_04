#05_get_name
#Fill out the get_name() function to return your name as a string!
#written a main() function has which calls your function to retrieve your name and then prints it in a greeting.

def get_name():
    return "BUSHRA"

# There is no need to edit code beyond this point

def main():
    name = get_name() # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    main()