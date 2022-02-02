#
# Jacqueline Chambliss, Rachel Ward, Edward Jenkins
# 12/6/2021
# Python Project: GUI Module
#

import tkinter as tk
import student as s
import billing
import globals as g


class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Student Registration')
        self.main_window.geometry('300x500')

        self.line1_frame = tk.Frame(self.main_window)  # Student ID line
        self.line2_frame = tk.Frame(self.main_window)  # PIN line
        self.line3_frame = tk.Frame(self.main_window)  # Login/Logout, Login Verification

        self.line4_frame = tk.Frame(self.main_window)  # List Courses, Show Bill, Status Checkbox
        self.line5_frame = tk.Frame(self.main_window)  # Course # Entry, Add, Drop

        self.line6_frame = tk.Frame(self.main_window)  # Output Label
        self.line7_frame = tk.Frame(self.main_window)  # Logout, Quit Button

        # --- Lines 1-3 for initial login attempt

        # Line 1 -- Student ID
        self.ID_label = tk.Label(self.line1_frame,
                                 text='Student ID:')
        self.ID_entry = tk.Entry(self.line1_frame,
                                 width=10)
        self.ID_label.pack(side='left', pady=10)
        self.ID_entry.pack(side='left')

        # Line 2 -- Student PIN
        self.pin_label = tk.Label(self.line2_frame,
                                  text='PIN:')
        self.pin_entry = tk.Entry(self.line2_frame,
                                  width=10)
        self.pin_label.pack(side='left', )
        self.pin_entry.pack(side='left')

        # Line 3 -- Login/Logout Buttons
        self.login_button = tk.Button(self.line3_frame,
                                      text='Login',
                                      command=self.check_login)
        self.logout_button = tk.Button(self.line3_frame,
                                       text='Logout',
                                       command=self.main_window.destroy)
        self.login_button.pack(side='left', padx=6, pady=14)
        self.logout_button.pack(side='left', padx=6, pady=14)

        # ------- Lines 4-8 for Registration Menu -------

        # Line 3 -- Login Verification
        self.login_verification = tk.StringVar()
        self.verification_output = tk.Label(self.line3_frame,
                                            textvariable=self.login_verification)
        self.verification_output.pack(side='left')

        # Line 4 (again) -- List Courses, Show Bill
        self.list_button = tk.Button(self.line4_frame,
                                     text='Course List',
                                     command=self.show_list)
        self.show_bill_button = tk.Button(self.line4_frame,
                                          text='Show Bill',
                                          command=self.show_bill)
        self.list_button.pack_forget()
        self.show_bill_button.pack_forget()

        # Line 4 (again) -- Status Checkbox
        self.status = tk.IntVar()
        self.status.set(0)
        self.status_checkbox = tk.Checkbutton(self.line4_frame,
                                              text='Show Aid Status',
                                              variable=self.status)
        self.status_checkbox.pack_forget()

        # Line 5 -- Course Number Entry
        self.course_label = tk.Label(self.line5_frame,
                                     text='Course #:')
        self.course_entry = tk.Entry(self.line5_frame,
                                     width=10)
        self.add_button = tk.Button(self.line5_frame,
                                    text='Add',
                                    command=self.check_add_course)
        self.drop_button = tk.Button(self.line5_frame,
                                     text='Drop',
                                     command=self.check_drop_course)
        self.course_label.pack_forget()
        self.course_entry.pack_forget()
        self.add_button.pack_forget()
        self.drop_button.pack_forget()

        # Line 6 -- Output Label
        self.output = tk.StringVar()
        self.output_label = tk.Label(self.line6_frame,
                                     textvariable=self.output)
        self.output_label.pack_forget()

        # Line 7 -- Logout/Quit Button
        self.switch_user_button = tk.Button(self.line7_frame,
                                            text='Logout',
                                            command=self.logout)
        self.quit_button = tk.Button(self.line7_frame,
                                     text='Quit',
                                     command=self.main_window.destroy)

        self.line1_frame.pack()
        self.line2_frame.pack()
        self.line3_frame.pack()

        tk.mainloop()

    # Function verifies the user input corresponds to a student and reveals the registration system if criteria are met.
    def check_login(self):
        id = self.ID_entry.get()
        pin = self.pin_entry.get()
        self.verification_output.pack(side='left')
        if g.gui_login(id, pin, g.student_list):
            self.login_verification.set('Login successful.')
            registered_list = s.list_courses(self.ID_entry.get(), g.course_roster, g.course_wait_list)[0]
            wait_list = s.list_courses(self.ID_entry.get(), g.course_roster, g.course_wait_list)[1]
            self.output.set(registered_list + '\n' + wait_list)
            self.display_menu()
        else:
            self.login_verification.set('Invalid ID or PIN.')
            self.pin_entry.delete(0, 'end')
            self.ID_entry.delete(0, 'end')

    # Function gets user input and uses a modified version of the command line system function to add a class
    def check_add_course(self):
        course_number = self.course_entry.get().upper()
        add_output = g.gui_add(self.ID_entry.get(), course_number, g.course_roster, g.course_max_size,
                               g.course_wait_list)
        self.output.set(add_output)

    # Function gets user input and uses a modified version of the command line system function to drop a class
    def check_drop_course(self):
        course_number = self.course_entry.get().upper()
        drop_output = g.gui_drop(self.ID_entry.get(), course_number, g.course_roster, g.course_wait_list)
        self.output.set(drop_output)

    # Function shows most up-to-date list of registered and wait-listed courses
    def show_list(self):
        registered_list = s.list_courses(self.ID_entry.get(), g.course_roster, g.course_wait_list)[0]
        wait_list = s.list_courses(self.ID_entry.get(), g.course_roster, g.course_wait_list)[1]
        self.output.set(registered_list + '\n' + wait_list)

    # Function displays user bill with checkbox option of revealing more data
    # about student that impacts final bill (financial aid, veteran status)
    def show_bill(self):
        display_str = ''

        # Determine Bill
        id = self.ID_entry.get()
        in_state = g.student_in_state
        roster = g.course_roster
        hours = g.course_hours
        total_hours = billing.calculate_hours_and_bill(id, in_state, roster, hours)[0]
        cost = billing.calculate_hours_and_bill(id, in_state, roster, hours)[1]
        display_str += f'Course load: {total_hours} credit hours \n Enrollment cost: ${cost: .2f}\n'

        # Determine Status
        if self.status.get() == 1:
            f_aid = g.finaid_status.get(self.ID_entry.get())
            display_str += f'\n Financial Aid: {f_aid}%'
            if g.veteran_status.get(self.ID_entry.get()):
                display_str += f'\n Veteran: Yes'
            else:
                display_str += f'\n Veteran: No'
        self.output.set(display_str)

    # Function keeps the registration system live, but resets the screen
    # so a different student has the opportunity to login.
    def logout(self):
        self.line4_frame.pack_forget()
        self.line5_frame.pack_forget()
        self.line6_frame.pack_forget()
        self.line7_frame.pack_forget()
        self.login_button.pack(side='left', padx=6, pady=14)
        self.logout_button.pack(side='left', padx=6, pady=14)
        self.verification_output.pack_forget()
        self.ID_entry.delete(0, 'end')
        self.course_entry.delete(0, 'end')
        self.status.set(0)

    # Function displays the registration system menu
    def display_menu(self):
        self.list_button.pack(side='left', padx=6, pady=14)
        self.show_bill_button.pack(side='left', padx=6, pady=14)
        self.status_checkbox.pack(side='left')
        self.course_label.pack(side='left')
        self.course_entry.pack(side='left')
        self.add_button.pack(side='left', padx=6, pady=14)
        self.drop_button.pack(side='left', padx=6, pady=14)
        self.output_label.pack(side='left')
        self.switch_user_button.pack(side='left', padx=6, pady=14)
        self.quit_button.pack(side='left', padx=6, pady=14)
        self.line4_frame.pack()
        self.line5_frame.pack()
        self.line6_frame.pack()
        self.line7_frame.pack()
        self.login_button.pack_forget()
        self.logout_button.pack_forget()
        self.pin_entry.delete(0, 'end')


my_gui = MyGUI()
