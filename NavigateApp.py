# import necessary modules
from tkinter import *
from tkinter import messagebox
import ast
from PIL import Image, ImageTk
from tkinter.constants import END
from tkinter import ttk
from tkcalendar import DateEntry
import openpyxl
from openpyxl import Workbook
import pathlib
import time
import simpleaudio as sa


# function for the login interface
def login_interface():
    # main login window
    root = Tk()
    root.title('Signin')
    root.geometry('925x500+300+200')
    root.configure(bg="#FFF")
    root.resizable(False, False)

    # function to handle sign in button click
    def signin():
        username = user.get()
        password = code.get()

        file = open('datasheet.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()

        # check if username and password match
        if username in r.keys() and password == r[username]:
            # display a message indicating that the signin was successful
            messagebox.showinfo('SignUp', "Sign in successful!")
            # destroy the window after successful login
            root.destroy()
            # user logs in after entering correct credentials
            home_interface()

        else:
            # if the username and password do not match, display an error message
            messagebox.showerror('Invalid', "Invalid credentials. Please try again.")

    # function to create window for the signup interface
    def signup_command():
        window = Toplevel(root)
        window.title("SignUp")
        window.geometry('925x500+300+200')
        window.configure(bg="#FFF")
        window.resizable(False, False)

        # function to handle sign up button click
        def signup():
            username = user.get()
            password = code.get().strip()
            confirm_password = conf.get().strip()

            # check if password and confirm password match
            if password == confirm_password:
                try:
                    # open the datasheet.txt file and read its contents
                    file = open('datasheet.txt', 'r+')
                    d = file.read()
                    r = ast.literal_eval(d)

                    # add the new user to the dictionary of users and passwords
                    dict2 = {username: password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    # write the updated dictionary of users and passwords back to the file
                    file = open('datasheet.txt', 'w')
                    file.write(str(r))

                    # display a message indicating that the signup was successful
                    messagebox.showinfo('SignUp', "Sign up successful!")

                except:
                    # if there was an error opening the file, create a new file and add the new user to it
                    file = open('datasheet.txt', 'w')
                    pp = str({username: password})
                    file.write(pp)
                    file.close()

            else:
                # if the password and confirm password do not match, display an error message
                messagebox.showerror('Invalid', "Both passwords must match.")

        # load the logo for the background
        image = PhotoImage(file='navigate.png')
        # add the image to the main window
        Label(window, image=image, bg='white').place(x=0, y=20)

        # create a frame for the signup form
        frame = Frame(window, width=350, height=390, bg='white')
        frame.place(x=480, y=50)

        # add a heading to the signup form
        heading = Label(frame, text='Sign up', fg='#0097b2', bg='white', font=('Ubuntu', 23))
        heading.place(x=140, y=5)

        # function to clear the username entry when clicked on
        def on_enter(e):
            user.delete(0, 'end')

        # function to restore the default username if left empty
        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Username')

        # add an entry field for the username
        user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Ubuntu', 12), highlightthickness=0,
                     insertbackground="black")
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        # bind the on_enter and on_leave functions to the username entry
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        # add a separator line between the username and password fields
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        # function to clear the password entry when clicked on
        def on_enter(e):
            if code.get() == 'Password':
                code.delete(0, 'end')
                code.config(show='*')

        # function to restore the default password if left empty
        def on_leave(e):
            if code.get() == '':
                code.insert(0, 'Password')
                code.config(show='')

        # add an entry field for the password
        code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Ubuntu', 12), highlightthickness=0,
                     insertbackground="black")
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        # bind the on_enter and on_leave functions to the password entry
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)

        # create a line separator using a frame widget
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        # function to clear the confirm password entry when clicked on
        def on_enter(e):
            if conf.get() == 'Confirm Password':
                conf.delete(0, 'end')
                conf.config(show='*')

        # function to restore the default confirm password if left empty
        def on_leave(e):
            if conf.get() == '':
                conf.insert(0, 'Confirm Password')
                conf.config(show='')

        # add an entry field for the confirm password
        conf = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Ubuntu', 12), highlightthickness=0,
                     insertbackground="black")
        conf.place(x=30, y=220)
        conf.insert(0, 'Confirm Password')
        # bind the on_enter and on_leave functions to the confirm password entry
        conf.bind("<FocusIn>", on_enter)
        conf.bind("<FocusOut>", on_leave)

        # create a line separator using a frame widget
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

        # create a signup button
        Button(frame, width=25, pady=7, text='Sign up', bg='#0097b2', fg='black', border=0, command=signup).place(x=45,
                                                                                                                  y=285)
        # create a label widget to show text for if the user already an account
        label = Label(frame, text="Already have an account?", fg='black', bg='white', font=('Ubuntu', 9))
        label.place(x=80, y=340)

        # function to destroy the window if the user clicks sign in
        def sign_in():
            window.destroy()

        # create a signin button using a button widget
        sign_in = Button(frame, width=6, padx=2, pady=2, text='Sign in', border=0, bg='white', fg='#0097b2',
                         font=('Ubuntu', 9),
                         highlightthickness=0, highlightbackground='white', command=sign_in)
        sign_in.place(x=200, y=339)

        # start the main loop for the login GUI
        window.mainloop()

    # logo for the background
    img = PhotoImage(file='navigate.png')
    # add the image to the main window
    Label(root, image=img, bg='white').place(x=0, y=20)

    # create a frame for the signin form
    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    # add a heading to the signin form
    heading = Label(frame, text='Sign in', fg='#0097b2', bg='white', font=('Ubuntu', 23))
    heading.place(x=140, y=5)

    # function to clear the username entry when clicked on
    def on_enter(e):
        user.delete(0, 'end')

    # function to restore the default username if left empty
    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    # add an entry field for the username
    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Ubuntu', 12), highlightthickness=0,
                 insertbackground="black")
    user.place(x=30, y=80)
    user.insert(0, "Username")
    # bind the on_enter and on_leave functions to the username entry
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    # add a separator line between the username and password fields
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # function to clear the password entry when clicked on
    def on_enter(e):
        if code.get() == 'Password':
            code.delete(0, 'end')
            code.config(show='*')

    # function to restore the default password if left empty
    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')
            code.config(show='')

    # add an entry field for the password
    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Ubuntu', 12), highlightthickness=0,
                 insertbackground='black')
    code.place(x=30, y=150)
    code.insert(0, "Password")
    # bind the on_enter and on_leave functions to the password entry
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    # create a line separator using a frame widget
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    # create a signin button
    Button(frame, width=25, pady=7, text='Sign in', bg='#0097b2', fg='black', bd=0, command=signin).place(x=45, y=215)
    # create a label widget to show text for creating an account
    label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Ubuntu', 9))
    label.place(x=90, y=270)

    # create a signup button using a button widget
    sign_up = Button(frame, width=6, padx=2, pady=2, text='Sign up', border=0, bg='white', fg='#0097b2',
                     font=('Ubuntu', 9),
                     highlightthickness=0, highlightbackground='white', command=signup_command)
    sign_up.place(x=200, y=269)

    # start the main loop for the GUI
    root.mainloop()


def home_interface():
    # main home window
    homeWindow = Tk()
    homeWindow.title('Home')
    homeWindow.geometry('1100x700+175+100')
    homeWindow.configure(bg="#FFF")
    homeWindow.resizable(False, False)

    # heading
    heading = Label(text="Welcome!", fg='#0097b2', bg='white', font=('Ubuntu', 70))
    heading.pack(pady=10)

    # images and respective buttons for app features
    imgHome = PhotoImage(file="Blue_Images/Home_Blue.png").subsample(8)
    homeButton = Button(homeWindow, image=imgHome, bg='white', bd=0, highlightthickness=0)
    homeButton.place(x=50, y=150)

    imgTask = PhotoImage(file="Gray_Images/Tasks_Gray.png").subsample(8)
    taskButton = Button(homeWindow, image=imgTask, bg='white', bd=0, highlightthickness=0)
    taskButton.place(x=50, y=250)

    imgTime = PhotoImage(file="Gray_Images/Time_Gray.png").subsample(7)
    timeButton = Button(homeWindow, image=imgTime, bg='white', bd=0, highlightthickness=0)
    timeButton.place(x=50, y=350)

    imgGPA = PhotoImage(file="Gray_Images/GPA_Gray.png").subsample(6)
    GPAButton = Button(homeWindow, image=imgGPA, bg='white', bd=0, highlightthickness=0)
    GPAButton.place(x=50, y=455)

    imgSettings = PhotoImage(file="Gray_Images/Set_Gray.png").subsample(8)
    settingsButton = Button(homeWindow, image=imgSettings, bg='white', bd=0, highlightthickness=0)
    settingsButton.place(x=50, y=560)

    homeD_frame = Frame(homeWindow, bg="white", bd=2, highlightbackground='white', highlightthickness=1)
    homeD_frame.config(width=800, height=530)
    homeD_frame.place(x=200, y=125)

    # load the image
    homeDesign = Image.open("Home_Design.png")

    # resize the image to fit the frame
    homeDesign = homeDesign.resize((760, 500), Image.LANCZOS)

    # convert the resized image to a PhotoImage object
    homeDesign = ImageTk.PhotoImage(homeDesign)

    # create the label and place it in the frame
    homeDesign_Label = Label(homeD_frame, image=homeDesign, bg='white', bd=0, highlightthickness=0)
    homeDesign_Label.place(x=10, y=0)

    # functions to destroy current interface and load selected interface
    def taskClick():
        homeWindow.destroy()
        tasks_interface()

    taskButton.config(command=taskClick)

    def timeClick():
        homeWindow.destroy()
        timer_interface()

    timeButton.config(command=timeClick)

    def gpaClick():
        homeWindow.destroy()
        gpa_interface()

    GPAButton.config(command=gpaClick)

    def settingsClick():
        homeWindow.destroy()
        settings_interface()

    settingsButton.config(command=settingsClick)

    # starts the event loop for the home window GUI
    homeWindow.mainloop()


# function for the tasks interface
def tasks_interface():
    # main tasks window
    taskWindow = Tk()
    taskWindow.title("Tasks")
    taskWindow.geometry('1100x700+175+100')
    taskWindow.config(bg='white')
    taskWindow.resizable(False, False)

    # heading for tasks interface
    heading = Label(taskWindow, text='Tasks', font='Ubuntu 70', bg='white', fg='#0097b2')
    heading.pack(pady=10)

    # images and buttons for respective app features
    imgHome = PhotoImage(file="Gray_Images/Home_Gray.png").subsample(8)
    homeButton = Button(taskWindow, image=imgHome, bg='white', bd=0, highlightthickness=0)
    homeButton.place(x=50, y=150)

    imgTask = PhotoImage(file="Blue_Images/Tasks_Blue.png").subsample(8)
    taskButton = Button(taskWindow, image=imgTask, bg='white', bd=0, highlightthickness=0)
    taskButton.place(x=50, y=250)

    imgTime = PhotoImage(file="Gray_Images/Time_Gray.png").subsample(7)
    timeButton = Button(taskWindow, image=imgTime, bg='white', bd=0, highlightthickness=0)
    timeButton.place(x=50, y=350)

    imgGPA = PhotoImage(file="Gray_Images/GPA_Gray.png").subsample(6)
    GPAButton = Button(taskWindow, image=imgGPA, bg='white', bd=0, highlightthickness=0, )
    GPAButton.place(x=50, y=455)

    imgSettings = PhotoImage(file="Gray_Images/Set_Gray.png").subsample(8)
    settingsButton = Button(taskWindow, image=imgSettings, bg='white', bd=0, highlightthickness=0)
    settingsButton.place(x=50, y=560)

    # callback functions: click button to go to a new page.
    def homeClick():
        taskWindow.destroy()
        home_interface()

    homeButton.config(command=homeClick)

    def timeClick():
        taskWindow.destroy()
        timer_interface()

    timeButton.config(command=timeClick)

    def gpaClick():
        taskWindow.destroy()
        gpa_interface()

    GPAButton.config(command=gpaClick)

    def settingsClick():
        taskWindow.destroy()
        settings_interface()

    settingsButton.config(command=settingsClick)

    style = ttk.Style()

    # theme
    style.theme_use("default")
    style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")

    # change selected color
    style.map("Treeview", background=[("selected", "darkred")])

    detail_frame = LabelFrame(taskWindow, text="Add Task", font=("Ubuntu", 20), bg="lightgray", foreground="black",
                              relief=GROOVE)
    detail_frame.place(x=150, y=120, width=300, height=550)

    # data Frame
    data_frame = Frame(taskWindow, background="white", relief=GROOVE)
    data_frame.place(x=470, y=120, width=600, height=550)

    # task Label and Entry
    task_lab = Label(detail_frame, text="Task: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    task_lab.place(x=10, y=16)

    task_ent = Entry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    task_ent.place(x=90, y=17, width=200, height=30)

    # details Label and Entry
    details_lab = Label(detail_frame, text="Details: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    details_lab.place(x=10, y=64)

    details_ent = Entry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    details_ent.place(x=90, y=65, width=200, height=30)

    # location Label and Entry
    location_lab = Label(detail_frame, text="Location:", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    location_lab.place(x=10, y=112)

    location_ent = Entry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    location_ent.place(x=90, y=113, width=200, height=30)

    # start Date Label and Entry
    start_lab = Label(detail_frame, text="Start Date: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    start_lab.place(x=10, y=160)

    start_ent = DateEntry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    start_ent.place(x=90, y=161, width=200, height=30)

    # end Date Label and Entry
    end_lab = Label(detail_frame, text="End Date: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    end_lab.place(x=10, y=208)

    end_ent = DateEntry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    end_ent.place(x=90, y=209, width=200, height=30)

    # status Label and Entry
    status_lab = Label(detail_frame, text="Status: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    status_lab.place(x=10, y=256)

    status_ent = ttk.Combobox(detail_frame, font=("Ubuntu", 14), background='white', foreground='black')
    status_ent["values"] = ("Yet to Start", "In Progress", "Completed")
    status_ent.place(x=90, y=257, width=200, height=30)

    # priority Label and Entry
    priority_lab = Label(detail_frame, text="Priority: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    priority_lab.place(x=10, y=304)

    priority_ent = ttk.Combobox(detail_frame, font=("Ubuntu", 14), background='white', foreground='black')
    priority_ent["values"] = ("Very High", "High", "Medium", "Low", "Very Low")
    priority_ent.place(x=90, y=305, width=200, height=30)

    # database frame
    main_frame = Frame(data_frame, bg="white", bd=2, relief=GROOVE)
    main_frame.pack(fill=BOTH, expand=True)

    y_scroll = Scrollbar(main_frame, orient=VERTICAL)
    x_scroll = Scrollbar(main_frame, orient=HORIZONTAL)

    # treeview database
    table = ttk.Treeview(main_frame, columns=("Task", "Details", "Location", "Start Date", "End Date", "Status",
                                              "Priority"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    # x-scrolls and y-scrolls
    y_scroll.config(command=table.yview)
    x_scroll.config(command=table.xview)

    y_scroll.pack(side=RIGHT, fill=Y)
    x_scroll.pack(side=BOTTOM, fill=X)

    # table headings
    table.heading("Task", text="Task")
    table.heading("Details", text="Details")
    table.heading("Location", text="Location")
    table.heading("Start Date", text="Start Date")
    table.heading("End Date", text="End Date")
    table.heading("Status", text="Status")
    table.heading("Priority", text="Priority")

    table["show"] = "headings"

    # set table column widths
    table.column("Task", width=100)
    table.column("Details", width=100)
    table.column("Location", width=100)
    table.column("Start Date", width=100)
    table.column("End Date", width=100)
    table.column("Status", width=100)
    table.column("Priority", width=100)

    table.pack(fill=BOTH, expand=True)

    data = []

    # creating odd and even rows
    global count
    count = 0
    for record in data:
        if count % 2 == 0:
            table.insert(parent="", index="end", text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("evenrow"))
        else:
            table.insert(parent="", index="end", text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("oddrow"))

        count += 1

    # functions that adds a record from data entries
    def add_record():
        # creating unique backgrounds and colours for odd-even rows
        table.tag_configure("oddrow", background="white", foreground='black')
        table.tag_configure("evenrow", background="#0097b2", foreground='white')

        global count
        if count % 2 == 0:
            table.insert(parent="", index="end", iid=count, text="", values=(task_ent.get(), details_ent.get(),
                                                                             location_ent.get(), start_ent.get(),
                                                                             end_ent.get(), status_ent.get(),
                                                                             priority_ent.get(),), tags=("evenrow"))
        else:
            table.insert(parent="", index="end", iid=count, text="", values=(task_ent.get(), details_ent.get(),
                                                                             location_ent.get(), start_ent.get(),
                                                                             end_ent.get(), status_ent.get(),
                                                                             priority_ent.get(),), tags=("oddrow"))
        count += 1

    # function to delete record
    def delete_record():
        x = table.selection()
        table.delete(x)

    # function to clear an ongoing entry
    def clear_record():
        task_ent.delete(0, END)
        details_ent.delete(0, END)
        location_ent.delete(0, END)
        start_ent.delete(0, END)
        end_ent.delete(0, END)
        status_ent.delete(0, END)
        priority_ent.delete(0, END)

    # function to update records
    def update_record():
        selected = table.focus()
        table.item(selected, text="", values=(
            task_ent.get(), details_ent.get(), location_ent.get(), start_ent.get(), end_ent.get(), status_ent.get(),
            priority_ent.get()))

        task_ent.delete(0, END)
        details_ent.delete(0, END)
        location_ent.delete(0, END)
        start_ent.delete(0, END)
        end_ent.delete(0, END)
        status_ent.delete(0, END)
        priority_ent.delete(0, END)

        # clear boxes
        task_ent.delete(0, END),
        details_ent.delete(0, END),
        location_ent.delete(0, END),
        start_ent.delete(0, END),
        end_ent.delete(0, END)
        status_ent.delete(0, END),
        priority_ent.delete(0, END)

    # add Button
    add_btn = Button(detail_frame, bg="black", foreground="black", text="Add", bd=0, pady=7, highlightthickness=1,
                     font=("Ubuntu", 13), width=10, command=add_record)
    add_btn.place(x=22, y=425)

    # update Button
    update_btn = Button(detail_frame, bg="white", foreground="black", text="Update", bd=0, pady=7, highlightthickness=1,
                        font=("Ubuntu", 13), width=10, command=update_record)
    update_btn.place(x=152, y=425)

    # clear Button
    clear_btn = Button(detail_frame, bg="white", foreground="black", text="Clear", bd=0, pady=7, highlightthickness=1,
                       font=("Ubuntu", 13), width=10, command=clear_record)
    clear_btn.place(x=22, y=470)

    # delete Button
    delete_btn = Button(detail_frame, foreground="black", text="Delete", bd=0, pady=7, font=("Ubuntu", 13), width=10,
                        highlightthickness=1, command=delete_record)
    delete_btn.place(x=152, y=470)

    # function to save the current records
    def save():
        # define the path to the Excel file to be used or created
        file_path = pathlib.Path('data.xlsx')

        # check if the file exists, and if so, attempt to load it with openpyxl
        if file_path.exists():
            try:
                file = openpyxl.load_workbook(file_path)
            except Exception as e:
                # if the file cannot be loaded, display an error message and return
                messagebox.showerror('Error', f'Failed to load Excel file: {str(e)}')
                return
        else:
            # if the file does not exist, create a new workbook with the necessary columns
            file = Workbook()
            sheet = file.active
            sheet['A1'] = "Task"
            sheet['B1'] = "Details"
            sheet['C1'] = "Location"
            sheet['D1'] = "Start Date"
            sheet['E1'] = "End Date"
            sheet['F1'] = "Status"
            sheet['G1'] = "Priority"

        # get the data from the table widget and append it to the Excel sheet
        sheet = file.active
        for record in table.get_children():
            task = table.item(record)['values'][0]
            details = table.item(record)['values'][1]
            location = table.item(record)['values'][2]
            start_date = table.item(record)['values'][3]
            end_date = table.item(record)['values'][4]
            status = table.item(record)['values'][5]
            priority = table.item(record)['values'][6]
            sheet.append([task, details, location, start_date, end_date, status, priority])

        # attempt to save the Excel file and display an error message if saving fails
        try:
            file.save(file_path)
            file.close()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save Excel file: {str(e)}')
            return

        # clear the table widget and display a success message
        for record in table.get_children():
            table.delete(record)
        messagebox.showinfo('Info', 'Successfully saved!')

    # save button
    save_button = Button(taskWindow, text="Save", command=save, background="white", fg="black",
                         pady=7, width=8, highlightthickness=1, bd=0)
    save_button.place(x=965, y=70)

    # starts the event loop for the tasks window GUI
    taskWindow.mainloop()


# function for the timer interface
def timer_interface():
    # timer window
    timeWindow = Tk()
    timeWindow.title("Timer")
    timeWindow.geometry('1100x700+175+100')
    timeWindow.config(bg='white')
    timeWindow.resizable(False, False)

    # heading
    heading = Label(timeWindow, text='Timer', font='Ubuntu 70', bg='white', fg='#0097b2')
    heading.pack(pady=10)

    # images and buttons for respective app features
    imgHome = PhotoImage(file="Gray_Images/Home_Gray.png").subsample(8)
    homeButton = Button(timeWindow, image=imgHome, bg='white', bd=0, highlightthickness=0)
    homeButton.place(x=50, y=150)

    imgTask = PhotoImage(file="Gray_Images/Tasks_Gray.png").subsample(8)
    taskButton = Button(timeWindow, image=imgTask, bg='white', bd=0, highlightthickness=0)
    taskButton.place(x=50, y=250)

    imgTime = PhotoImage(file="Blue_Images/Time_Blue.png").subsample(8)
    timeButton = Button(timeWindow, image=imgTime, bg='white', bd=0, highlightthickness=0)
    timeButton.place(x=50, y=350)

    imgGPA = PhotoImage(file="Gray_Images/GPA_Gray.png").subsample(6)
    GPAButton = Button(timeWindow, image=imgGPA, bg='white', bd=0, highlightthickness=0, )
    GPAButton.place(x=50, y=455)

    imgSettings = PhotoImage(file="Gray_Images/Set_Gray.png").subsample(8)
    settingsButton = Button(timeWindow, image=imgSettings, bg='white', bd=0, highlightthickness=0)
    settingsButton.place(x=50, y=560)

    # callback functions: click button to go to a new page.
    def homeClick():
        timeWindow.destroy()
        home_interface()

    homeButton.config(command=homeClick)

    def taskClick():
        timeWindow.destroy()
        tasks_interface()

    taskButton.config(command=taskClick)

    def gpaClick():
        timeWindow.destroy()
        gpa_interface()

    GPAButton.config(command=gpaClick)

    def settingsClick():
        timeWindow.destroy()
        settings_interface()

    settingsButton.config(command=settingsClick)

    # ribbon image for aesthetics
    ribbon = PhotoImage(file="ribbon.png").subsample(2)
    Label(timeWindow, image=ribbon, bg='white').place(x=540, y=300)

    # entry fields to input time
    hrs = StringVar()
    Entry(timeWindow, textvariable=hrs, width=2, font=('Ubuntu', 70), bg='white', fg='#0097b2').place(x=250, y=260)
    hrs.set("00")

    mins = StringVar()
    Entry(timeWindow, textvariable=mins, width=2, font=('Ubuntu', 70), bg='white', fg='#0097b2').place(x=475, y=260)
    mins.set("00")

    sec = StringVar()
    Entry(timeWindow, textvariable=sec, width=2, font=('Ubuntu', 70), bg='white', fg='#0097b2').place(x=700, y=260)
    sec.set("00")

    # labels for entry fields
    Label(timeWindow, text="hours", font=("Ubuntu", 30), bg='white', fg='#0097b2').place(x=350, y=280)
    Label(timeWindow, text="minutes", font=("Ubuntu", 30), bg='white', fg='#0097b2').place(x=575, y=280)
    Label(timeWindow, text="seconds", font=("Ubuntu", 30), bg='white', fg='#0097b2').place(x=800, y=280)

    global timer_running
    timer_running = False

    # function that runs the timer
    def Timer():
        global times
        global timer_running

        # convert the input time to seconds
        times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
        timer_running = True

        # starts the timer countdown
        while times > -1 and timer_running:
            minute, second = (times // 60, times % 60)

            hour = 0
            if minute > 60:
                hour, minute = (minute // 60, minute % 60)

            # update the display with the current time
            sec.set(second)
            mins.set(minute)
            hrs.set(hour)

            timeWindow.update()
            time.sleep(1)

            # play an audio clip when the timer reaches 0
            if (times == 0):
                wave_obj = sa.WaveObject.from_wave_file("haruthee.wav")
                play_obj = wave_obj.play()
                play_obj.wait_done()
                sec.set("00")
                mins.set("00")
                hrs.set("00")

            times -= 1

    # functions to start, stop and reset the timer
    def start_timer():
        global timer_running
        if not timer_running:
            timer_running = True
            Timer()

    def stop_timer():
        global timer_running
        timer_running = False

    def reset_timer():
        global times
        global timer_running
        timer_running = False
        times = 0
        sec.set("00")
        mins.set("00")
        hrs.set("00")
        timeWindow.update()

    # buttons to start, stop and reset the timer
    Button(timeWindow, text="Start", bg='white', bd=0, fg='#0097b2', width=9, height=2, font='Ubuntu 30',
           command=start_timer).place(x=200, y=500)

    Button(timeWindow, text="Stop", bg='white', bd=0, fg='#0097b2', width=9, height=2, font='Ubuntu 30',
           command=stop_timer).place(x=450, y=500)

    Button(timeWindow, text="Reset", bg='white', bd=0, fg='#0097b2', width=9, height=2,
           font='Ubuntu 30', command=reset_timer).place(x=700, y=500)

    # start the main loop for the GUI
    timeWindow.mainloop()


# function for gpa interface
def gpa_interface():
    # main frame
    gpaWindow = Tk()
    gpaWindow.title("GPA Calculator")
    gpaWindow.geometry('1100x700+175+100')
    gpaWindow.config(bg="#FFF")
    gpaWindow.resizable(False, False)

    # heading
    heading = Label(text="GPA Calculator", fg='#0097b2', bg='white', font=('Ubuntu', 60))
    heading.pack(pady=10)

    # buttons that take user to different pages
    imgHome = PhotoImage(file="Gray_Images/Home_Gray.png").subsample(8)
    homeButton = Button(gpaWindow, image=imgHome, bg='white', bd=0, highlightthickness=0)
    homeButton.place(x=50, y=150)

    imgTask = PhotoImage(file="Gray_Images/Tasks_Gray.png").subsample(8)
    taskButton = Button(gpaWindow, image=imgTask, bg='white', bd=0, highlightthickness=0)
    taskButton.place(x=50, y=250)

    imgTime = PhotoImage(file="Gray_Images/Time_Gray.png").subsample(7)
    timeButton = Button(gpaWindow, image=imgTime, bg='white', bd=0, highlightthickness=0)
    timeButton.place(x=50, y=350)

    imgGPA = PhotoImage(file="Blue_Images/GPA_Blue.png").subsample(6)
    GPAButton = Button(gpaWindow, image=imgGPA, bg='white', bd=0, highlightthickness=0, )
    GPAButton.place(x=50, y=455)

    imgSettings = PhotoImage(file="Gray_Images/Set_Gray.png").subsample(8)
    settingsButton = Button(gpaWindow, image=imgSettings, bg='white', bd=0, highlightthickness=0)
    settingsButton.place(x=50, y=560)

    # callback functions: click button to go to a new page.
    def homeClick():
        gpaWindow.destroy()
        home_interface()

    homeButton.config(command=homeClick)

    def taskClick():
        gpaWindow.destroy()
        tasks_interface()

    taskButton.config(command=taskClick)

    def timeClick():
        gpaWindow.destroy()
        timer_interface()

    timeButton.config(command=timeClick)

    def settingsClick():
        gpaWindow.destroy()
        settings_interface()

    settingsButton.config(command=settingsClick)

    # gpa frame
    GPA_Frame = Frame(gpaWindow, bg="lightgray", bd=2, relief=GROOVE)
    GPA_Frame.config(width=800, height=530)
    GPA_Frame.place(x=200, y=125)

    # semester 1 frame
    sem1_Frame = Frame(GPA_Frame, bg="white", bd=2, relief=GROOVE)
    sem1_Frame.config(width=735, height=210)
    sem1_Frame.place(x=30, y=30)

    # courses
    courseName_label = Label(sem1_Frame, text="Course Name ", bg="white", fg="black", font=('Ubuntu', 15))
    courseName_label.place(x=25, y=15)

    course1_entry = Entry(sem1_Frame, width=20, bg="lightgray", fg="black")
    course1_entry.place(x=26, y=40)

    course2_entry = Entry(sem1_Frame, width=20, bg="lightgray", fg="black")
    course2_entry.place(x=26, y=70)

    course3_entry = Entry(sem1_Frame, width=20, bg="lightgray", fg="black")
    course3_entry.place(x=26, y=100)

    course4_entry = Entry(sem1_Frame, width=20, bg="lightgray", fg="black")
    course4_entry.place(x=26, y=130)

    # letter Grades
    letterGrade_label = Label(sem1_Frame, text="Letter Grade", bg="white", fg="black",
                              font=('Ubuntu', 15))
    letterGrade_label.place(x=320, y=15)

    grade1_var = StringVar()
    grade1_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade1_choose = ttk.Combobox(sem1_Frame, textvariable=grade1_var, values=grade1_values, width=10)
    grade1_choose.place(x=320, y=40)

    grade2_var = StringVar()
    grade2_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade2_choose = ttk.Combobox(sem1_Frame, textvariable=grade2_var, values=grade2_values, width=10)
    grade2_choose.place(x=320, y=70)

    grade3_var = StringVar()
    grade3_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade3_choose = ttk.Combobox(sem1_Frame, textvariable=grade3_var, values=grade3_values, width=10)
    grade3_choose.place(x=320, y=100)

    grade4_var = StringVar()
    grade4_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade4_choose = ttk.Combobox(sem1_Frame, textvariable=grade4_var, values=grade4_values, width=10)
    grade4_choose.place(x=320, y=130)

    # number of credits
    numCredits_label = Label(sem1_Frame, text="Credits", bg="white", fg="black", font=('Ubuntu', 15))
    numCredits_label.place(x=560, y=15)

    cred1_entry = Entry(sem1_Frame, width=10, bg="lightgray", fg="black")
    cred1_entry.place(x=560, y=40)

    cred2_entry = Entry(sem1_Frame, width=10, bg="lightgray", fg="black")
    cred2_entry.place(x=560, y=70)

    cred3_entry = Entry(sem1_Frame, width=10, bg="lightgray", fg="black")
    cred3_entry.place(x=560, y=100)

    cred4_entry = Entry(sem1_Frame, width=10, bg="lightgray", fg="black")
    cred4_entry.place(x=560, y=130)

    def get_GPASem1():
        """This function takes values from all grades and entry boxes 1 through 4 and calculates the Semester GPA.
        It also gives an error message pop up if grades/ credits are not entered but the 'Semester GPA'
        button is clicked. """
        if (grade1_choose.get() == "" or cred1_entry.get() == "" or
            grade2_choose.get() == "" or cred2_entry.get() == "" or
            grade3_choose.get() == "" or cred3_entry.get() == "" or
            grade4_choose.get() == "" or cred4_entry.get() == ""):
            messagebox.showerror("Error", "Please enter a grade/credit")
            return
        total_gradeSem1 = (
                (float(convert_grade(grade1_choose.get())) * float(cred1_entry.get()))
                + (float(convert_grade(grade2_choose.get())) * float(cred2_entry.get()))
                + (float(convert_grade(grade3_choose.get())) * float(cred3_entry.get()))
                + (float(convert_grade(grade4_choose.get())) * float(cred4_entry.get())))
        total_creditsSem1 = (float(cred1_entry.get()) + float(cred2_entry.get()) + float(cred3_entry.get())
                             + float(cred4_entry.get()))
        calculated_GPASem1 = round(total_gradeSem1 / total_creditsSem1, 2)
        display_GPASem1(calculated_GPASem1)
        return calculated_GPASem1

    def convert_grade(letter_grade):
        """This function converts letter grades to float values on a 4.0 scale"""
        if letter_grade == "A":
            return float(4.0)
        elif letter_grade == "A-":
            return float(3.7)
        elif letter_grade == "B+":
            return float(3.3)
        elif letter_grade == "B":
            return float(3.0)
        elif letter_grade == "B-":
            return float(2.7)
        elif letter_grade == "C+":
            return float(2.3)
        elif letter_grade == "C":
            return float(2.0)
        elif letter_grade == "C-":
            return float(1.7)
        elif letter_grade == "D+":
            return float(1.3)
        elif letter_grade == "D":
            return float(1.0)
        elif letter_grade == "D-":
            return float(0.7)
        else:
            return float(0.0)

    def display_GPASem1(calculated_GPASem1):
        """This function displays the 1st semester GPA"""
        calculateGPASem1.config(text=f"Semester GPA: {calculated_GPASem1}")

    # calculate GPA (Semester 1) button
    calculateGPASem1 = Button(sem1_Frame, text="Semester GPA", bg="white", fg="black", borderwidth=0,
                              font=('Ubuntu', 15), highlightthickness=0, command=get_GPASem1)
    calculateGPASem1.place(x=25, y=170)

    # semester 2 frame
    sem2_Frame = Frame(GPA_Frame, bg="white", bd=2, relief=GROOVE)
    sem2_Frame.config(width=735, height=210)
    sem2_Frame.place(x=30, y=245)

    # courses
    courseName_label = Label(sem2_Frame, text="Course Name ", bg="white", fg="black", font=('Ubuntu', 15))
    courseName_label.place(x=25, y=15)

    course5_entry = Entry(sem2_Frame, width=20, bg="lightgray", fg="black")
    course5_entry.place(x=27, y=40)

    course6_entry = Entry(sem2_Frame, width=20, bg="lightgray", fg="black")
    course6_entry.place(x=27, y=70)

    course7_entry = Entry(sem2_Frame, width=20, bg="lightgray", fg="black")
    course7_entry.place(x=27, y=100)

    course8_entry = Entry(sem2_Frame, width=20, bg="lightgray", fg="black")
    course8_entry.place(x=27, y=130)

    # letter Grades
    letterGrade_label = Label(sem2_Frame, text="Letter Grade", bg="white", fg="black", font=('Ubuntu', 15))
    letterGrade_label.place(x=320, y=15)

    grade5_var = StringVar()
    grade5_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade5_choose = ttk.Combobox(sem2_Frame, textvariable=grade5_var, values=grade5_values, width=10)
    grade5_choose.place(x=320, y=40)

    grade6_var = StringVar()
    grade6_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade6_choose = ttk.Combobox(sem2_Frame, textvariable=grade6_var, values=grade6_values, width=10)
    grade6_choose.place(x=320, y=70)

    grade7_var = StringVar()
    grade7_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade7_choose = ttk.Combobox(sem2_Frame, textvariable=grade7_var, values=grade7_values, width=10)
    grade7_choose.place(x=320, y=100)

    grade8_var = StringVar()
    grade8_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    grade8_choose = ttk.Combobox(sem2_Frame, textvariable=grade8_var, values=grade8_values, width=10)
    grade8_choose.place(x=320, y=130)

    # number of credits
    numCredits_label = Label(sem2_Frame, text="Credits", bg="white", fg="black", font=('Ubuntu', 15))
    numCredits_label.place(x=560, y=15)

    cred5_entry = Entry(sem2_Frame, width=10, bg="lightgray", fg="black")
    cred5_entry.place(x=560, y=40)

    cred6_entry = Entry(sem2_Frame, width=10, bg="lightgray", fg="black")
    cred6_entry.place(x=560, y=70)

    cred7_entry = Entry(sem2_Frame, width=10, bg="lightgray", fg="black")
    cred7_entry.place(x=560, y=100)

    cred8_entry = Entry(sem2_Frame, width=10, bg="lightgray", fg="black")
    cred8_entry.place(x=560, y=130)

    def get_GPASem2():
        """This function takes values from all grades and entry boxes 5 through 8 and calculates the Semester GPA.
        It also gives an error message pop up if grades/ credits are not entered but the 'Semester GPA'
        button is clicked. """
        if (grade5_choose.get() == "" or cred5_entry.get() == "" or
            grade6_choose.get() == "" or cred6_entry.get() == "" or
            grade7_choose.get() == "" or cred7_entry.get() == "" or
            grade8_choose.get() == "" or cred8_entry.get() == ""):
            messagebox.showerror("Error", "Please enter a grade/credit")
            return
        total_gradeSem2 = ((float(convert_grade(grade5_choose.get()))
                            * float(cred5_entry.get()))
                           + (float(convert_grade(grade6_choose.get()))
                              * float(cred6_entry.get()))
                           + (float(convert_grade(grade7_choose.get()))
                              * float(cred7_entry.get()))
                           + (float(convert_grade(grade8_choose.get()))
                              * float(cred8_entry.get())))
        total_creditsSem2 = (float(cred5_entry.get()) + float(cred6_entry.get())
                             + float(cred7_entry.get()) + float(cred8_entry.get()))
        calculated_GPASem2 = round(total_gradeSem2 / total_creditsSem2, 2)
        display_GPASem2(calculated_GPASem2)
        return calculated_GPASem2

    def display_GPASem2(calculated_GPASem2):
        """This function displays the 2nd semester GPA"""
        calculateGPASem2.config(text=f"Semester GPA: {calculated_GPASem2}")

    # calculate GPA (Semester 2) button
    calculateGPASem2 = Button(sem2_Frame, text="Semester GPA", bg="white", fg="black", borderwidth=0,
                              font=('Ubuntu', 15), highlightthickness=0, command=get_GPASem2)
    calculateGPASem2.place(x=25, y=170)

    def calcCumGPA():
        """This function takes values from all grades and entry boxes 1 through 8 and calculates the Cumulative GPA of
        both semesters. It also gives an error message pop up if grades/ credits are not entered but the 'Cumulative
        GPA' button is clicked"""
        if (grade1_choose.get() == "" or cred1_entry.get() == "" or
                grade2_choose.get() == "" or cred2_entry.get() == "" or
                grade3_choose.get() == "" or cred3_entry.get() == "" or
                grade4_choose.get() == "" or cred4_entry.get() == "" or
                grade5_choose.get() == "" or cred5_entry.get() == "" or
                grade6_choose.get() == "" or cred6_entry.get() == "" or
                grade7_choose.get() == "" or cred7_entry.get() == "" or
                grade8_choose.get() == "" or cred8_entry.get() == ""):
            messagebox.showerror("Error", "Please enter a grade/credit")
            return
        total_grades_cum = ((float(convert_grade(grade1_choose.get()))
                             * float(cred1_entry.get()))
                            + (float(convert_grade(grade2_choose.get()))
                               * float(cred2_entry.get()))
                            + (float(convert_grade(grade3_choose.get()))
                               * float(cred3_entry.get()))
                            + (float(convert_grade(grade4_choose.get()))
                               * float(cred4_entry.get()))
                            + (float(convert_grade(grade5_choose.get()))
                               * float(cred5_entry.get()))
                            + (float(convert_grade(grade6_choose.get()))
                               * float(cred6_entry.get()))
                            + (float(convert_grade(grade7_choose.get()))
                               * float(cred7_entry.get()))
                            + (float(convert_grade(grade8_choose.get()))
                               * float(cred8_entry.get())))

        total_credits_cum = (float(cred1_entry.get())
                             + float(cred2_entry.get())
                             + float(cred3_entry.get())
                             + float(cred4_entry.get())
                             + float(cred5_entry.get())
                             + float(cred6_entry.get())
                             + float(cred7_entry.get())
                             + float(cred8_entry.get()))
        calculated_GPACum = round(total_grades_cum / total_credits_cum, 2)
        display_GPASCum(calculated_GPACum)
        return calculated_GPACum

    def display_GPASCum(calculated_GPACum):
        """This function displays the cumulative GPA of both semesters"""
        cumulativeGPA.config(text=f"Cumulative GPA: {calculated_GPACum}")

    # cumulative GPA button
    cumulativeGPA = Button(GPA_Frame, text="Cumulative GPA", bg="white", fg="black", borderwidth=0,
                           font=('Ubuntu', 15), highlightthickness=0, command=calcCumGPA)
    cumulativeGPA.place(x=55, y=480)

    # start the main loop for the GUI
    gpaWindow.mainloop()


# function for settings interface
def settings_interface():
    # main frame
    settingsWindow = Tk()
    settingsWindow.title("Settings")
    settingsWindow.geometry('1100x700+175+100')
    settingsWindow.config(bg="#FFF")
    settingsWindow.resizable(False, False)

    # heading
    heading = Label(text="Settings", fg='#0097b2', bg='white', font=('Ubuntu', 60))
    heading.pack(pady=10)

    # buttons that take user to different pages
    imgHome = PhotoImage(file="Gray_Images/Home_Gray.png").subsample(8)
    homeButton = Button(settingsWindow, image=imgHome, bg='white', bd=0, highlightthickness=0)
    homeButton.place(x=50, y=150)

    imgTask = PhotoImage(file="Gray_Images/Tasks_Gray.png").subsample(8)
    taskButton = Button(settingsWindow, image=imgTask, bg='white', bd=0, highlightthickness=0)
    taskButton.place(x=50, y=250)

    imgTime = PhotoImage(file="Gray_Images/Time_Gray.png").subsample(7)
    timeButton = Button(settingsWindow, image=imgTime, bg='white', bd=0, highlightthickness=0)
    timeButton.place(x=50, y=350)

    imgGPA = PhotoImage(file="Gray_Images/GPA_Gray.png").subsample(6)
    GPAButton = Button(settingsWindow, image=imgGPA, bg='white', bd=0, highlightthickness=0, )
    GPAButton.place(x=50, y=455)

    imgSettings = PhotoImage(file="Blue_Images/Set_Blue.png").subsample(9)
    settingsButton = Button(settingsWindow, image=imgSettings, bg='white', bd=0, highlightthickness=0)
    settingsButton.place(x=50, y=560)

    # callback functions: click button to go to a new page.
    def homeClick():
        settingsWindow.destroy()
        home_interface()

    homeButton.config(command=homeClick)

    def taskClick():
        settingsWindow.destroy()
        tasks_interface()

    taskButton.config(command=taskClick)

    def timeClick():
        settingsWindow.destroy()
        timer_interface()

    timeButton.config(command=timeClick)

    def gpaClick():
        settingsWindow.destroy()
        gpa_interface()

    GPAButton.config(command=gpaClick)

    # change credentials frame
    changeCredsFrame = Frame(settingsWindow, width=900, height=550, bg="white", bd=2)
    changeCredsFrame.place(x=200, y=150)

    # ribbon image for aesthetics
    ribbon = PhotoImage(file="ribbon.png").subsample(2)
    Label(changeCredsFrame, image=ribbon, bg='white').place(x=280, y=-30)

    # heading for change credentials form
    heading = Label(changeCredsFrame, text='Change credentials?', fg='#0097b2', bg='white', font=('Ubuntu', 23))
    heading.place(x=65, y=5)

    # function to clear the current username entry when clicked on
    def on_enter(e):
        user.delete(0, 'end')

    # function to restore the default current username if left empty
    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Current Username')

    # add an entry field for the current username
    user = Entry(changeCredsFrame, width=25, fg='black', border=0, bg='white', font=('Ubuntu', 12),
                 highlightthickness=0,
                 insertbackground="black")
    user.place(x=30, y=80)
    user.insert(0, 'Current Username')
    # bind the on_enter and on_leave functions to the current username entry
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    # add a separator line between fields
    Frame(changeCredsFrame, width=295, height=2, bg='black').place(x=25, y=107)

    # function to clear the new username entry when clicked on
    def on_enter(e):
        if new_user.get() == 'New Username':
            new_user.delete(0, 'end')

    # function to restore the new username if left empty
    def on_leave(e):
        if new_user.get() == '':
            new_user.insert(0, 'New Username')
            new_user.config(show='')

    # add an entry field for the new username
    new_user = Entry(changeCredsFrame, width=25, fg='black', border=0, bg='white', font=('Ubuntu', 12),
                     highlightthickness=0,
                     insertbackground="black")
    new_user.place(x=30, y=150)
    new_user.insert(0, 'New Username')
    # bind the on_enter and on_leave functions to the new username entry
    new_user.bind("<FocusIn>", on_enter)
    new_user.bind("<FocusOut>", on_leave)

    # create a line separator
    Frame(changeCredsFrame, width=295, height=2, bg='black').place(x=25, y=177)

    # function to clear the current password entry when clicked on
    def on_enter(e):
        if password.get() == 'Current Password':
            password.delete(0, 'end')
            password.config(show='*')

    # function to restore the default current password if left empty
    def on_leave(e):
        if password.get() == '':
            password.insert(0, 'Current Password')
            password.config(show='')

    # add an entry field for the current password
    password = Entry(changeCredsFrame, width=25, fg='black', border=0, bg='white', font=('Ubuntu', 12),
                     highlightthickness=0,
                     insertbackground="black")
    password.place(x=30, y=220)
    password.insert(0, 'Current Password')
    # bind the on_enter and on_leave functions to the current password entry
    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)

    # create a line separator using a frame widget
    Frame(changeCredsFrame, width=295, height=2, bg='black').place(x=25, y=247)

    def on_enter(e):
        if new_pass.get() == 'New Password':
            new_pass.delete(0, 'end')
            new_pass.config(show='*')

    # function to restore the default new password if left empty
    def on_leave(e):
        if new_pass.get() == '':
            new_pass.insert(0, 'New Password')
            new_pass.config(show='')

    # add an entry field for the new password
    new_pass = Entry(changeCredsFrame, width=25, fg='black', border=0, bg='white', font=('Ubuntu', 12),
                     highlightthickness=0,
                     insertbackground="black")
    new_pass.place(x=30, y=290)
    new_pass.insert(0, 'New Password')
    # bind the on_enter and on_leave functions to the new password entry
    new_pass.bind("<FocusIn>", on_enter)
    new_pass.bind("<FocusOut>", on_leave)

    # create a line separator using a frame widget
    Frame(changeCredsFrame, width=295, height=2, bg='black').place(x=25, y=317)

    # function to update credentials
    def update():
        current_username = user.get()
        current_password = password.get()
        new_username = new_user.get()
        new_password = new_pass.get()

        file = open('datasheet.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()

        # check if username and password match
        if current_username in r.keys() and current_password == r[current_username]:
            r[new_username] = new_password
            del r[current_username]

            # write the updated dictionary back to the file
            with open('datasheet.txt', 'w') as file:
                file.write(str(r))
            # display a message indicating that the update was successful
            messagebox.showinfo('Update', "Update successful!")

        else:
            # if the username and password do not match, display an error message
            messagebox.showerror('Invalid', "Invalid credentials. Please try again.")

    # function to take user back to the login page
    def signout():
        settingsWindow.destroy()
        login_interface()

    # update button
    Button(changeCredsFrame, width=25, height=2, pady=7, text='Update', bg='#0097b2', fg='black', border=0,
           command=update).place(x=45, y=355)

    # signout button
    Button(changeCredsFrame, width=25, height=2, pady=7, text='Sign Out', bg='#0097b2', fg='black',
           border=0, command=signout).place(x=445, y=355)

    # start the main loop for the GUI
    settingsWindow.mainloop()


# calling the login interface
login_interface()


