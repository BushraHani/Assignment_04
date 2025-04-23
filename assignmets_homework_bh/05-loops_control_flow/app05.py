#05_double_it.

#Write a program that asks a user to enter a number. 
# Your program will then double that number and print out the result. 
# It will repeat that process until the value is 100 or greater.


def double_until_100():
# Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
    
# Keep doubling the number until it is 100 or greater
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value = curr_value * 2
        
        
    print(curr_value)  

double_until_100()

if __name__ == "__main__":
    main() # type: ignore