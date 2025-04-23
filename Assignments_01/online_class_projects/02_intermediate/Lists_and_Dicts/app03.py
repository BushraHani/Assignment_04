#Lists_and_Dicts

#code with lists! Implement the functionality described in the comments below.

#def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
## Print the length of the list.
# Add 'mango' at the end of the list. 
# Print the updated list.  

# Print the length of the list.
fruit_list = ['apple', 'banana', 'orange', 'pear', 'orange'] 
list_length = len(fruit_list)
print(list_length)

# Add 'mango' at the end of the list. 
fruit_list.append('mango')

# Print the updated list.
for fruit in fruit_list:
    print(fruit)
    