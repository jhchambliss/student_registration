#
# Jacqueline Chambliss, Rachel Ward, Edward Jenkins
# 12/5/2021
# Python Project: Global Variables Module
#

import student as s

# Global variables list for access by both GUI and command line loop

# The Student List
student_list = [('1001', '111'), ('1002', '222'),
                ('1003', '333'), ('1004', '444')]

# The In-State List
student_in_state = {'1001': True,
                    '1002': False,
                    '1003': True,
                    '1004': False}

# Veteran Status
veteran_status = {'1001': False,
                  '1002': False,
                  '1003': True,
                  '1004': True}

# Financial Aid Status
finaid_status = {'1001': 15,
                 '1002': 0,
                 '1003': 100,
                 '1004': 0}

# Course Roster
course_roster = {'CSC101': ['1004', '1003'],
                 'CSC102': ['1001'],
                 'CSC103': ['1002'],
                 'CSC104': []}

# Hours / Course
course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}

# Max Size / Class
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

# Course Wait List
course_wait_list = {'CSC101': []}


# This function allows a student to log in to the GUI
def gui_login(id, pin, s_list):
    entry = (id, pin)
    if entry in s_list:
        return True
    else:
        return False


# This function allows a student to use the GUI to add a class.
def gui_add(id, c_number, c_roster, c_max_size, c_wait_list):
    # test for match in course dictionary,
    # else display message and return
    if c_number not in list(c_roster.keys()):
        return 'Course not found'
    # test if student is already enrolled,
    # if so display message and return
    elif id in c_roster[c_number]:
        return 'You are already enrolled in that course'

    # test if the course is already full
    elif c_max_size[c_number] == len(c_roster[c_number]):
        # wait-list student then display message and return
        if c_number in c_wait_list.keys():
            if id not in c_wait_list[c_number]:
                c_wait_list[c_number].append(id)
                return 'Course full, added to wait-list'
            else:
                return 'You are already wait-listed for that course.'
            # a wait-list exists for course already
        else:
            # create wait-list for course
            c_wait_list[c_number] = [id]
            return 'Course full, added to wait-list'
    # all test conditions passed, add student to c_roster
    else:
        c_roster[c_number].append(str(id))
        return 'Course added'


# This function allows a student to use the GUI
# to drop a class.
def gui_drop(id, c_number, c_roster, c_wait_list):
    # test for match in course dictionary,
    # else display message and return
    if c_number not in list(c_roster.keys()):
        return 'Course not found'
    # test if student is enrolled,
    # else display message and return
    elif id not in c_roster[c_number]:
        display_str = ''
        if c_number in c_wait_list.keys():
            if id in c_wait_list[c_number]:
                # remove student from the wait-list
                w_list = c_wait_list[c_number]
                display_str = 'Removed from wait-list'
        else:
            display_str = 'You are not enrolled in that course'
        return display_str
    # both test conditions met, then remove student from c_roster
    else:
        c_roster[c_number].remove(id)
        # call method to check for a wait-list since a spot just opened up
        s.wait_list_get_next(c_number, c_roster, c_wait_list)
        return 'Course dropped'
