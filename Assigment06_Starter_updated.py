# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# EBrown,8.17.2022,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(list_of_rows, remove_item):
        """ Removes data from a list of dictionary rows

        :param status: (boolean) with status of data removal:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        status = False
        row_number = 0
        for row in list_of_rows:
            if remove_item.lower() == row["Task"].lower():
                del table_lst[row_number]
                status = True
        row_number = row_number + 1
        return status, list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        status = False
        file = open(file_name,"w")
        for row in table_lst:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        status = True
        return status


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current Tasks
        2) Add a new Task
        3) Remove an existing Task
        4) Save Data to File  
        5) Reload data from file      
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        task = str(input("Please enter new task:")).strip()
        priority = str(input("Please enter priority of new task:")).strip()
        print()
        return task, priority
        pass

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        remove_item = str(input("Please enter task to remove:"))
        return remove_item

    def remove_data_success(status):
        """Print status of task removal

        :param status: (bool) status of removal to display
        """
        if status:
            print("The task was removed successfully!")
        else:
            print("There is no task with that name in the list.")
        print()

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file( file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show menu
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':
        IO.output_current_tasks_in_list(table_lst)
        continue

    if choice_str.strip() == '2':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Remove an existing Task
        remove_item = IO.input_task_to_remove()
        remove_fn = Processor.remove_data_from_list(table_lst,remove_item)
        IO.remove_data_success(remove_fn)
        IO.output_current_tasks_in_list(table_lst)
        continue  # to show the menu

    elif choice_str == '4':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '5':
        print("WARNING: This action will replace all unsaved changes. Data loss may occur!")
        str_y_or_n = input("Reload file without saving? (y/n)")
        if str_y_or_n.lower() == 'y':
            table_lst.clear()
            table_lst = Processor.read_data_from_file(file_name_str,table_lst)
            IO.output_current_tasks_in_list(table_lst)
        else:
            input("File data was not reloaded. Please press [Enter] to return to the menu.")
            IO.output_current_tasks_in_list(table_lst)

    elif choice_str == '6':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
