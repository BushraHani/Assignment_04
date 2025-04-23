#04_multiple_returns...

#There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.
#To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
     main()
     