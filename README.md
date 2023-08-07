# Navigate-Project-COMP123
The program is a tkinter-based GUI application called ‘Navigate’ that provides interfaces for user login, home, tasks, timer, GPA, and settings. The structure of the program is organized in a way to make it easy for users to navigate through different sections of the application.

The main parts of the program are:

**Login Interface:** This is the entry point of the application. Users must enter their credentials to access other interfaces. If successful, they proceed to the home interface.

**Home Interface:** Acts as the central hub, where users can navigate to tasks, timer, GPA, and settings interfaces.

**Tasks, Timer, and GPA Interfaces:** These are separate interfaces that provide specific functionalities. Users can access every interface from every other interface.

**Settings Interface:** Allows users to change their credentials (username and password) and provides options to navigate to the home, tasks, timer, and GPA interfaces.

The logic behind the program organization is to separate each interface into its own function, making it easier to manage and maintain the code. The interfaces are designed to be easily accessible for every other interface and they can interact with one another using callback functions. For example, when a user clicks a button in the home interface, the corresponding interface function is called, and the current window is destroyed to open the new interface.

Each interface function creates a new tkinter window with the necessary widgets like labels, buttons, and entry fields. These functions also bind callback functions to specific events like button clicks or entry field focus, which enable the program to respond to user actions and switch between interfaces. The program stores user credentials in a file called 'datasheet.txt' which is used to validate the user during the login process and update their credentials in the settings interface. The program stores all ‘Saved’ tasks (in the task interface) to an Excel/ Numbers sheet on the user’s personal computer under the title ‘data.’ The user can access this sheet to view their tasks and make customisations. All updates, deletions will reflect in the sheet once the user clicks the ‘Save’ button on the tasks interface.

# User Manual 

In order to run the program, open the .py file called ‘NavigateApp.py’. When you first open the app you are prompted to the sign in interface. All username and password data is saved as a dictionary to a datasheet.txt file.

<img width="913" alt="Screenshot 2023-06-02 at 1 04 42 PM" src="https://github.com/tnangpal/Navigate-Project-COMP123/assets/124189649/4f129a46-1168-4c18-ba21-37f4db05ef4b">

Depending on whether or not you are  successfully able to sign in, a message box will appear after you click the ‘Sign in’ button that lets you know whether the login attempt was successful or not. 

If you wish to create a new account, you can click the ‘Sign up’ button, which will take you to the following interface:

<img width="915" alt="Screenshot 2023-06-02 at 1 05 30 PM" src="https://github.com/tnangpal/Navigate-Project-COMP123/assets/124189649/fbad6b76-9e09-47aa-aa8e-9f746dca5f4c">

If you successfully enter a username and a password that is identical in both ‘password’ and ‘confirm password’ fields, a message box will appear indicating that your sign up was successful. Then, proceed to click the sign in button and enter your credentials to log in. If your passwords don’t match, a message box will appear indicating that the passwords do not match and your sign up will not be successful. 

Once you have successfully signed in and clicked ‘OK’ on the message box saying the sign in was successful, you will be directed to the home interface.

<img width="1086" alt="Screenshot 2023-06-02 at 1 05 57 PM" src="https://github.com/tnangpal/Navigate-Project-COMP123/assets/124189649/0d246498-0b86-4ccb-8417-04c343c95e82">

The home interface gives you a simple description of what the app is all about. On the left side of the app is a menu bar that has 5 different toggleable buttons: home button, task manager, timer, GPA calculator, and settings. Each button will direct you to each respective interface. 

<img width="1085" alt="Screenshot 2023-06-02 at 1 06 39 PM" src="https://github.com/tnangpal/Navigate-Project-COMP123/assets/124189649/3f1e5bcd-8941-491f-a0f9-97d056a17537">

The tasks interface allows you to add the tasks, its details, location, start and end dates, your status of completion and its priority. You could also choose to not fill every box if you feel it is unnecessary. Once you click ‘Add’, your entry will pop up on the frame on the right hand side. The three other buttons at the bottom do the following: ‘Clear’ clears what you have entered on the ‘Add Task’ frame. It does not clear anything on the database frame on the right. ‘Delete’ allows you to clear an entry on the database frame once selected. Similarly, once selected, the ‘update’ button enables you to change an entry, which then updates on the database frame. The button on the top right hand side, ‘Save’, clears all the entries on the database frame and saves it to an excel file, which you can access and edit. 

<img width="1089" alt="Screenshot 2023-06-02 at 1 07 58 PM" src="https://github.com/tnangpal/Navigate-Project-COMP123/assets/124189649/cf313846-2750-4c05-a5ab-2ac12a66d59d">

On the timer interface, you can enter a time and click ‘Start’, which starts the timer. The ‘Stop’ button pauses the timer and the ‘Reset’ button resets the timer to 0. Once the time is up, an audio clip will play for 10 seconds to notify you. 

<img width="1087" alt="Screenshot 2023-06-02 at 1 08 54 PM" src="https://github.com/tnangpal/Navigate-Project-COMP123/assets/124189649/3bacce30-de30-4670-90ea-f18dc99b01d3">

The GPA calculator allows you to enter the course name, which is not necessary to add, letter grade, which appears as a dropdown, and the amount of credits that class is worth. If you do not enter either the letter grade or credits, the program will show a messagebox asking you to do so. If you have ‘pass or failed’ a class, simply enter a random letter grade with 0 credits. Then proceed to click the ‘Semester GPA: ’ button to reveal your GPA. If you would like to include another semester in order to calculate your cumulative GPA, enter the details and click ‘Semester GPA: ’ to see that semester’s GPA and ‘Cumulative GPA: ’. Note: You will have to click the calculate GPA button everytime you change any details, or it will show the previously calculated details. You also do not have to enter details for both semesters if you only wish to calculate the GPA for one semester. 

<img width="1089" alt="Screenshot 2023-06-02 at 1 09 29 PM" src="https://github.com/tnangpal/Navigate-Project-COMP123/assets/124189649/71506a8c-73da-4305-bba4-f3fbb157924c">

The final interface is ‘Settings’, which allows you to change your credentials if you wish. In order to do that, you will have to correctly enter your current username and password, and also enter a new username and password. You will then have to click ‘Update’. Depending on whether or not this is successful, a message box will appear. Finally, the ‘Sign Out’ button simply takes you back to the sign in interface. You will have to re-enter your credentials if you wish to sign in to the app again. 

Thank you for using Navigate!




