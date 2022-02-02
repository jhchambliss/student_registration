#
# Edward Jenkins, Jacqueline Chambliss, Rachel Ward
# 12/5/2021
# Python Project: Billing Module
#

import globals as g  # Import global variables for use in parts of the function


# Create Function: calculate_hours_and_bill (id, s_in_state, c_rosters, c_hours)
# This function calculates the course hours and cost of enrollment.  It has four parameters:
# •	id is the ID of the student
# •	s_in_state is a dictionary of in state students
# •	c_rosters is a dictionary of class rosters
# •	c_hours is a dictionary with the credit hours of each class
# This function calculates the bill based on $225 per credit hour for in-state students and $850 per credit hour for
# out-of-state students. After calculating the bill, the function returns the total number of credit hours and the
# total cost of enrollment.

# Define the calculate_hours_and_bill function:
def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):  # Creates the function with parameters
    # Using the Student ID, check the in-state list to determine if student is in-state to determine tuition cost"
    in_state = s_in_state.get(id)  # Get the true/false value for the id and assign it to the "in_state" variable
    if in_state:  # If "in_state" is true, execute block
        tuition = 225  # Set the value of the "tuition" variable to the in-state value
    else:  # If "in_state" is not true (and thus false), execute block
        tuition = 850  # Set the value of the "tuition" variable to the out-of-state value

    # Determine if the student is signed up for each course and, if so, add the credit hours to the total
    total_c_hours = 0  # Initiate the accumulator variable
    for k in c_rosters:  # Loop through all k/v pairs in c_rosters
        if id in c_rosters.get(k):  # Check if the id is in the value of the key and, if so, execute block
            total_c_hours += c_hours.get(
                k)  # If id is a value of the key, add the value of the key from the c_hours dictionary to the accumulator

    # Determine if the student gets a free ride due to veteran status:
    veteran = g.veteran_status.get(id)  # Get the tru/false value for the id and assign it to the "veteran" variable
    if veteran:  # If "veteran" is true, execute block
        veteran = 0  # Sets "veteran" to zero which will cause the total cost to equal zero
    else:  # If "veteran" is not true (and thus false), execute block
        veteran = 1  # Sets "veteran" to one which will cause the total cost to be unaffected

    # Determine if the student gets a tuition reduction based on their financial aid status:
    f_aid = g.finaid_status.get(id)  # Get the integer value for the id and assign it to the "f_aid" variable
    f_aid = (100 - f_aid) / 100  # Turns the "f_aid" value into a percentage value so it can be multiplied by

    # Determine the total cost of enrollment by multiplying the credit hours by the tuition cost to get total cost
    total_cost = total_c_hours * tuition * veteran * f_aid  # Multiply the variables together to get the total_cost

    # Return the total number of credit hours and the total cost of enrollment
    return total_c_hours, total_cost  # Return the total credit hours and total cost


# Create Function: display_hours_and_bill(hours, cost)
# This function displays the course hours and the cost of enrollment. It has two parameters:
# •	hours is the number of course hours
# •	cost is the total cost of enrollment
# This function displays the total number of credit hours and the total cost of enrollment.

# Define the display_hours_and_bill function:
def display_hours_and_bill(hours, cost):  # Creates the function with parameters
    # Display the total number of credit hours:
    print(f'Course load: {hours} credit hours')  # Prints the number of credit hours to stout

    # Display the total number of credit hours:
    print(f'Enrollment cost: ${cost:.2f}')  # Prints the number of credit hours to stout
