#04_liftoff
#Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
#Here's a sample run of the program:
#10 9 8 7 6 5 4 3 2 1 Liftoff!


def countdown():
# Loop for countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i, end=" ")  # Print the number with a space after it
# After the countdown, print Liftoff!        
    print("Liftoff!")  

# Call the countdown function
countdown()
