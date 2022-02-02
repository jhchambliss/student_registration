# ----------------------------------------------------------------
#
# Jacqueline Chambliss, Rachel Ward, Edward Jenkins
# 12/5/2021
# Python Project: Registration Module (command line)
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are registered for.
# (in the student module)
#
# It also allows students to review the tuition costs for their course roster.
# (in the billing module)
# -----------------------------------------------------------------
import student as s
import billing
import globals as g


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It uses a loop to serve multiple students.
    # Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    while True:
        # begin loop by asking for user ID
        id = input('Enter ID to log in, or 0 to quit: ')
        # if user enters zero, program should quit
        if id == '0':
            break

        # call login method in a loop that repeats until correct
        # ID/PIN combo is entered
        while True:
            if login(id, g.student_list):
                break
            else:
                id = input('\nEnter ID to log in, or 0 to quit: ')
                # if user enters zero, program should quit
                if id == '0':
                    break
                continue
        # if user enters zero, program should quit
        if id == '0':
            break
        response = ''
        while response != '0':
            # Ask the user for the item type they are adding.
            response = input('\nEnter 1 to add course, 2 to drop course, '
                             '3 to list courses, 4 to show bill, 0 to exit: ')
            # if entry is invalid ask again
            while response not in ['0', '1', '2', '3', '4']:
                response = input('\nEnter 1 to add course, 2 to drop course, '
                                 '3 to list courses, 4 to show bill, 0 to exit: ')
            # Call appropriate method
            if response == '1':
                s.add_course(id, g.course_roster, g.course_max_size, g.course_wait_list)
            elif response == '2':
                s.drop_course(id, g.course_roster, g.course_wait_list)
            elif response == '3':
                registered_list = s.list_courses(id, g.course_roster, g.course_wait_list)[0]
                wait_list = s.list_courses(id, g.course_roster, g.course_wait_list)[1]
                print(registered_list + '\n' + wait_list)
            elif response == '4':
                total_hours = \
                    billing.calculate_hours_and_bill(id, g.student_in_state, g.course_roster, g.course_hours)[0]
                cost = billing.calculate_hours_and_bill(id, g.student_in_state, g.course_roster, g.course_hours)[
                    1]
                billing.display_hours_and_bill(total_hours, cost)
            else:
                print('Session Ended\n')
                break


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    pin = input('Enter your pin: ')
    entry = (id, pin)
    if entry in s_list:
        print('ID and PIN verified.')
        return True
    else:
        print('ID or PIN incorrect. Please try again.')
        return False


main()
