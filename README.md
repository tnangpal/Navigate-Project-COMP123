# Navigate-Project-COMP123
The program is a tkinter-based GUI application called ‘Navigate’ that provides interfaces for user login, home, tasks, timer, GPA, and settings. The structure of the program is organized in a way to make it easy for users to navigate through different sections of the application.

The main parts of the program are:

Login Interface: This is the entry point of the application. Users must enter their credentials to access other interfaces. If successful, they proceed to the home interface.

Home Interface: Acts as the central hub, where users can navigate to tasks, timer, GPA, and settings interfaces.

Tasks, Timer, and GPA Interfaces: These are separate interfaces that provide specific functionalities. Users can access every interface from every other interface.

Settings Interface: Allows users to change their credentials (username and password) and provides options to navigate to the home, tasks, timer, and GPA interfaces.

The logic behind the program organization is to separate each interface into its own function, making it easier to manage and maintain the code. The interfaces are designed to be easily accessible for every other interface and they can interact with one another using callback functions. For example, when a user clicks a button in the home interface, the corresponding interface function is called, and the current window is destroyed to open the new interface.

Each interface function creates a new tkinter window with the necessary widgets like labels, buttons, and entry fields. These functions also bind callback functions to specific events like button clicks or entry field focus, which enable the program to respond to user actions and switch between interfaces. The program stores user credentials in a file called 'datasheet.txt' which is used to validate the user during the login process and update their credentials in the settings interface. The program stores all ‘Saved’ tasks (in the task interface) to an Excel/ Numbers sheet on the user’s personal computer under the title ‘data.’ The user can access this sheet to view their tasks and make customisations. All updates, deletions will reflect in the sheet once the user clicks the ‘Save’ button on the tasks interface.
