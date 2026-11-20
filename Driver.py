"""

    Filename: Driver.py

    Purpose: The user will run this file with their text file along side it, and this
    program will intake that text file, set it as a matrix, and our algorithm files
    will do the work, depending on which is called. The driver should return an int and 
    a matrix, the int being the optimal decision of the least amount of torches, and
    the matrix being a visual of the placed torches in the cave system. 

"""

# Main function
def main():

    # Welcome output 
    print("\nWelcome to Optimal Torch Placement!\n")

    # User input variable 
    user_input = 0

    # Menu loop
    while True:

        # Initial menu 
        print("1. Brute Force Algoritm")
        print("2. Greedy Algorithm")
        print("3. Genetic Algorithm")
        print("4. Compare Algorithms")
        print("5. Quit\n")

        # User input
        try:
            user_input = int(input("Please choose an option: "))

        except ValueError:
            user_input = 0

        # Ensuring proper input 
        while user_input < 1 or user_input > 5:

            # Invalid input prompt + clear input
            try:
                user_input = int(input("\nPlease enter a valid input: "))

            except ValueError:
                user_input = 0

        # Switch statement 
        match user_input:

            case 1:

                # Brute Force Algorithm
                # Code here...
                    # Calls brute force function to return an int and a matrix
                    # Sets them to named values
                    # Returns the info to the user 
                print("\ntest - 1\n")

            case 2:

                # Greedy Algorithm
                # Code here...
                    # Calls greedy function to return an int and a matrix
                    # Sets them to named values
                    # Returns the info to the user 
                print("\ntest - 2\n")

            case 3:

                # Genetic Algorithm
                # Code here...
                    # Calls genetic function to return an int and a matrix
                    # Sets them to named values
                    # Returns the info to the user 
                print("\ntest - 3\n")

            case 4:
                
                # Combination Algorithm
                # Code here...
                    # Calls all functions to return an int and a matrix
                    # Sets them to named values
                    # Compares ints to find the smallest value
                    # Returns the optimal result to the user 
                print("\ntest - 4\n")

            case _:

                # Quit 
                pass

        if user_input == 5:
            break

    # Says goodbye
    print("\nGoodbye!\n")

# Runs main 
if __name__ == "__main__":
    main()