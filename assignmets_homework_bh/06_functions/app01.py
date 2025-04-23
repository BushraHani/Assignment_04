#01_chaotic_counting.

import random

import random

# DONE_LIKELIHOOD will be randomly chosen between 0.0 and 1.0
DONE_LIKELIHOOD = random.uniform(0.0, 1.0)
print(f"DONE_LIKELIHOOD is set to: {DONE_LIKELIHOOD:.2f}")

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # this ends the function execution, so we'll get back to the main() function!
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
