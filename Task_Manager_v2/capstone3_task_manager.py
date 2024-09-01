from datetime import date
from datetime import datetime
# =================== Login ===================
login_details_open = open("user.txt", "r+")
login_details_read = login_details_open.readlines() # Reading the txt file and cleaning the whitespaces

cleaned_login_details_read = [details for details in login_details_read if details != "\n"]


# Assigning Login Variables into lists
username_list = []
password_list = []

for line in cleaned_login_details_read:

    username, password = line.strip("\n").split(", ")
    username_list.append(username)      # Clean each index of \n and split it into two seperate variables, username & password
    password_list.append(password)      # then add to above list

# End of assigning login variables into lists

# Convert user_list & pass_list into dictionary for each of access
user_login_information = dict(zip(username_list, password_list))

#print(user_login_information)

login_details_open.close()
# End of conversion

# User Login Section
while True:
    Login = False  # Setting the default Login status to false as no valid username / password is entered at program start
    
    username = input("Username: ")
    password = input("Password: ")

    if user_login_information.get(username) == password: # Returns value for key(username) in dict. If it matches pass, then login
            
        print(f"\nSuccessfully logged in.\nWelcome {username}.\n")
        Login = True
        break

    else:
        print("\nIncorrect Username or Password.") 
        print("Please try again.\n")
        Login = False
        continue

# =================== End of Login ===================

# =================== Register new user ===================
def reg_user(username_check):
    if username_check != "admin":
        print("\nYou do not have the permissions for this option.\n") # Checking if username is admin or not
        return
    
    elif username_check == "admin":                                   # If admin, start gathering details for new user
        add_login = open("user.txt", "a")

        while True:
            new_username = input("Please enter the new username: ")
            if new_username in user_login_information.keys():   # Checks if username is currently in dictionary
                print("\nThis username already exists.")
                print("Please choose a different username.\n") # Prompt to choose a different username
                continue
            else:
                break

        while True: 
            new_password = input("Please enter the new password: ")
            password_check = input("Please re-enter the new password: ")

            if password_check != new_password: # If passwords don't match, promt to re-enter passwords again
                print("Passwords do not match.")
                continue
            elif password_check == new_password:
                break
        
        add_login.write(f"\n{new_username}, {new_password}") # Writing new login details to txt file
        add_login.close()
# =================== End of Register new user ===================

# =================== Add new task ===================
def add_task():
    add_new_task_open = open("tasks.txt", "a")
    while True:
        username_assignment = input("\nUsername of the person to whom the task is assigned to: ")
        if username_assignment in user_login_information.keys():
            break
        else:
            print("\nInvalid username.\n")
    new_task_title = input("\nNew task title:  ")
    new_task_description = input("\nNew task description: \n")  # Gathering variables for assignment
    date_assigned = date.today().strftime("%d %B %Y")
    while True:
        due_date = input("\nNew task due date (eg 5 February 2023): ")
        try: 
            if overdue_check(due_date) == True:
                break
            else:
                print("\nPlease enter a valid date.\n")
                continue
        except:
            print("\nPlease enter a valid date.")
            continue
    default_task_completion = "No"

    add_new_task_open.write(f"\n{username_assignment}, {new_task_title}, {new_task_description}, {date_assigned}, {due_date}, {default_task_completion}")
    # Writing new task to task txt
    add_new_task_open.close()

# =================== Add task end ===================

# =================== Task Dictionary ===================
# The goal of this function is to turn the tasks into an easier to manage format
# Each task in tasks.txt will have it's own task number(key) and then all the details for the task will be displayed afterwards(value)
# With this, it will help me in va & vm
def task_dictionary():
    task_file_open = open("tasks.txt", "r+")
    task_file_read = task_file_open.readlines()

    
    cleaned_task_file_read = [details for details in task_file_read if details != "\n"] # List comprehension to clean whitespaces in file that was read

    assigned_to_list = []
    task_list = []
    task_description_list = []                      # Same reason for user,pass
    assignment_date_list = []
    due_date_list = []
    completion_list = []

    for line in cleaned_task_file_read:
        assigned_to, task, task_description, assignment_date, due_date, completion =  line.strip("\n").split(", ")

        assigned_to_list.append(assigned_to)
        task_list.append(task)
        task_description_list.append(task_description)  # Over here I am essentially doing the same method as I did for user and pass 
        assignment_date_list.append(assignment_date)    # As above, just this time there are more variables
        due_date_list.append(due_date)
        completion_list.append(completion)

    

    task_file_open.close()
    
    # In the below section of this function, I create a dictionary with the task number as the key and the details as the value
    new_task_list = []
    for i in range(len(assigned_to_list)):
        new_task_list.append([assigned_to_list[i],task_list[i],task_description_list[i],assignment_date_list[i],due_date_list[i],completion_list[i]])

    # ^ grouping details for each task into a its own section in the list
    # Now that it is in a list, each item can be modified individually easier and is easier to manage 

    global thisdict #By using global, I allow thisdict to be accessed by other functions even though it is defined in this function
    thisdict = {}  

    for i in range(len(assigned_to_list)):
        
        thisdict[(i+1)] = [assigned_to_list[i], task_list[i], task_description_list[i], assignment_date_list[i], due_date_list[i], completion_list[i]]
    # Updating the dictionary to contain all the tasks and their corresponding task number
    
    return thisdict
    
    
    
    
    

# =================== End of Task Dictionary ===================

# =================== View All ===================
def view_all(tasks):
    for task_number in tasks:
        x = tasks.get(task_number)

                                                # Get values for task (tasknumber) then print it in a neat fashion
        print(f"""
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
Task:                   {task_number}
Assigned to:            {x[0]}
Task title :            {x[1]}
Assigned on:            {x[3]}                  
Due date:               {x[4]}
Completed:              {x[5]}
Task description:       {x[2]}
            
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n""")
        
# =================== End of View All ===================

# =================== View Mine ===================
def view_mine():
    user_task_numbers = []                        # With x allowing me to access each task individually, I can check if x[0] (which is assigned_to)
    for task_number in thisdict:        # matches with the username. If it does I print the task
        x = thisdict.get(task_number)   
        if username == x[0]:
            user_task_numbers.append(task_number)            
            print(f"""
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡               
Task:                   {task_number}
Assigned to:            {x[0]}
Task title :            {x[1]}
Assigned on:            {x[3]}                  
Due date:               {x[4]}
Completed:              {x[5]}
Task description:       {x[2]}
            
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡\n""") 
            
# I decide not to change the task numbers because in a real world scenario, it would be easier for the employee to see what task numbers are theirs
# out of all of the combined tasks. When reporting to the boss they can just mentioned the task number for them rather than having a new task number 
# assigned to them
    task_edit(user_task_numbers)
# =================== End of View Mine ===================

# =================== Edit own menu ===================
def task_edit(task_numbers):
    user_input = input("Do you wish to edit and tasks?(Y/N)   ").lower()

    if user_input == "n":
        print("\nReturning to main menu.\n")
    
    elif user_input == "y":
        while True:
            print("\nYour assigned task numbers are: ")
            for i in task_numbers:
                print(f"Task: {i}")

            task_edit_number = int(input("Which task number do you wish to edit? "))
            
            if task_edit_number not in task_numbers :
                print("\nSorry, this task number is not assigned to you.\n")
                continue
            
            elif task_edit_number in task_numbers:
                x = thisdict.get(task_edit_number)
                complete_check = str(x[5]).lower()
                
                if complete_check == "yes":
                    print("\nSorry, you cannot edit this task as it has been marked as complete.\n")
                    break

                elif complete_check == "no":

                     editing_options = input("""1 - Mark a task as complete
2 - Change a task due date
3 - Change the user assignment for this task
-1 - Return to main menu
Please choose an option:  """)
                     
                     if editing_options == "1":
                         completion_change(x, task_edit_number)
                         break
                     
                     elif editing_options == "2":
                         due_date_change(x, task_edit_number)
                         break
                     
                     elif editing_options == "3":
                         user_assignment_change(x, task_edit_number)
                         break
                     elif editing_options == "-1":
                         print("\nReturning to main menu.\n")
                         break
                     else:
                         print("\nInvalid input.\nPlease choose a number from the list.")
                         continue

    else:
        print("\nInvalid Input.\nReturning to main menu\n")                    
# =================== End of menu ===================


# =================== Start of completion change ===================
def completion_change(task, task_number):

    task_file_open = open("tasks.txt", "r")
    task_file_read = task_file_open.readlines() #reading tasks.txt so i can find what line I will need to edit

    task_title = task[1]
    assigned_on = task[3]

    for count, line in enumerate(task_file_read):      # This iterates through each line in the txt file
        if username in line:                           # I added multiple checks to make we have the right line before we change it
            if task_title in line:                     # Replacing No with Yes
                if assigned_on in line:
                    line = line.replace("No", "Yes")
                    task_file_read[count] = line
    task_file_open.close()
    
    task_file_read = "".join(task_file_read)           # After replacing, join the lists together so txt is back in its normal form
    
    task_file_write_open = open("tasks.txt", "w")
    task_file_write_open.write(task_file_read)      # Open the file in write mode and then write new details including updated completion

    task_file_write_open.close()

    print(f"\nYou have marked task {task_number} as complete.\n")

# =================== End of completion change ===================

# =================== Start of due date change ===================
def due_date_change(task, task_number):

    task_file_open = open("tasks.txt", "r")
    task_file_read = task_file_open.readlines()    

    task_title = task[1]
    due_date = task[4]

    while True:
        new_due_date = input("Please enter the new date the task is due on (eg 5 February 2020): ")
        try:
            if overdue_check(new_due_date) == True:
                break
            else:
                print("\nPlease enter a valid date.\n")
        except:
            print("\nPlease enter a valid date.\n")
        
        
        
         
    for count, line in enumerate(task_file_read):      
        if username in line:                           
            if task_title in line:                     
                if due_date in line:
                    line = line.replace(due_date, new_due_date)
                    task_file_read[count] = line
    task_file_open.close()
                                                                # This func follows the same logic as above just different variables changed
    task_file_read = "".join(task_file_read)           
    
    task_file_write_open = open("tasks.txt", "w")
    task_file_write_open.write(task_file_read)      

    task_file_write_open.close()

    print(f"\nYou have change the due date for task {task_number} from {due_date} to {new_due_date}.\n")

# =================== End of due date change ===================

# =================== Start of overdue_check ===================
def overdue_check(date):
    date_format = "%d %B %Y"
    inputted_date = datetime.strptime(date, date_format)
    present_date = datetime.now()

    if inputted_date.date() > present_date.date(): # turns into date that will help check if the user date is in the past
        return True                                 # If new date > current date
    else:
        return False
# =================== End of overdue_check ===================


# =================== Start of user assignment change ===================
def user_assignment_change(task, task_number):
    task_file_open = open("tasks.txt", "r")
    task_file_read = task_file_open.readlines()    

    task_title = task[1]
    assigned_on = task[3]

    while True:
            new_task_owner = input("\nPlease enter the username of the new task owner (case sensitive): ")

            if new_task_owner in user_login_information.keys():
                for count, line in enumerate(task_file_read):      
                    if username in line:                           
                      if task_title in line:                     
                         if assigned_on in line:
                           line = line.replace(task[0], new_task_owner)
                           task_file_read[count] = line
    
                task_file_open.close()
                                                                # This func follows the same logic as above just different variables changed
                task_file_read = "".join(task_file_read)           
    
                task_file_write_open = open("tasks.txt", "w")
                task_file_write_open.write(task_file_read)      

                task_file_write_open.close()

                print(f"\nYou have change the user for task {task_number} from {username} to {new_task_owner}.\n")
                break

            else:
                print("\nSorry, this username is not in the username list.")
                print("Please try again\n")
                continue

# =================== End of user assignment change ===================

# =================== Start of task_overview ===================
def task_overview():
    task_total = len(thisdict.keys())
    
    complete_count, incomplete_count = completion_check()
    task_overview_report = f"""\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
Total number of tasks: {task_total}
Total completed tasks: {complete_count}, {percentage_cal(complete_count, task_total)}%   
Total incompleted tasks: {incomplete_count}, {percentage_cal(incomplete_count, task_total)}%
Total incomplete and overdue: {incomplete_overdue()}
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡"""
    # print(task_overview_report)                   #writing all required data into variable, then opening file and writing to it
    task_overview_open = open("task_overview.txt", "w", encoding= "utf-8")
    task_overview_open.write("\nTask Overview\n")
    task_overview_open.write(task_overview_report)
    task_overview_open.close()

    

# =================== End of task_overview ===================

# # =================== User overview ===================

def user_overview():


    task_total = len(thisdict.keys())
    registered_users = len(user_login_information)
    task_counter_list = []
    complete_list = []
    incomplete_list = []
    incom_over_list = []
    for username in username_list:
        task_counter = 0
        complete = 0
        incomplete = 0
        incom_over = 0
        for task_number in thisdict:
            x = thisdict.get(task_number)
            if username == x[0]:
                task_counter += 1
            
                if x[5].lower() == "yes":
                    complete += 1
                elif x[5].lower() == "no":
                    incomplete += 1                 #gathering info for eac username
                    due_date = x[4]                 # appending to lists , same logic as beginning task dictionary
                if overdue_check(due_date) == False:
                    incom_over += 1

        task_counter_list.append(task_counter)
        complete_list.append(complete)
        incomplete_list.append(incomplete)
        incom_over_list.append(incom_over)
        # print(f"{username} task counter is {task_counter}")
        # print(f"Com: {complete}, incom: {incomplete}, incom_over: {incom_over}")
        # print(f"{username_list}\n{task_counter_list}\n{complete_list}\n{incomplete_list}\n{incom_over_list}")

    user_overview_dict = {}
    for i in range(len(username_list)):
        user_overview_dict[username_list[i]] = [task_counter_list[i], complete_list[i], incomplete_list[i], incom_over_list[i]]

    user_overview_open = open("user_overview.txt", "w", encoding= "utf-8")

    user_overview_open.write("\nUser Overview\n")
    user_overview_open.write(f"\nThe total number of users registered with task_manager is: {registered_users}\n")
    user_overview_open.write(f"The total number of tasks that have been generated and tracked is {task_total}")
    for username in user_overview_dict:
        y = user_overview_dict.get(username)
        writing_data = f"""\n≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
{username}
Total number of tasks assigned: {y[0]}
Percentage of tasks compared to total tasks: {percentage_cal(y[0], task_total)}%
Completed tasks: {y[1]}, {percentage_cal(y[1], y[0])}%
Incomplete tasks: {y[2]}, {percentage_cal(y[2], y[0])}%
Incomplete & Overdue: {y[3]}, {percentage_cal(y[3], y[0])}%
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡"""
        user_overview_open.write(writing_data)

    user_overview_open.close()
# =================== End of user_overview ===================
# =================== Percentage Calc ===================
def percentage_cal(x,y):
    try:
        percentage = round((x / y) * 100)
        return percentage
    except ZeroDivisionError:
        return 0 



# =================== Start of completion check ===================
def completion_check():
    complete = 0
    incomplete = 0
    for task_number in thisdict:
     x = thisdict.get(task_number)
     if x[5].lower() == "yes":
         complete += 1
     else:                                  # checks the 5th index which is usually completion and adds count to each depending on 
         incomplete += 1                    # value
    
    return complete, incomplete

# =================== End of completion check ===================
# =================== Incomp overdue ===================
def incomplete_overdue():
    incomplete_overdue_counter = 0
    for task_number in thisdict:
        x =  thisdict.get(task_number)
        if x[5].lower() == "no":
            due_date = x[4]
            if overdue_check(due_date) == False:
                incomplete_overdue_counter += 1
    
    return incomplete_overdue_counter

 # =================== End of Incomp overdue ===================   



# =================== Start of Display Statistics ===================
def display_statistics():
    while True:
        try:
            task_overview_open = open("task_overview.txt", "r", encoding= "utf=8")
            user_overview_open = open("user_overview.txt", "r", encoding= "utf-8")

            task_overview_read = task_overview_open.read()
            user_overview_read = user_overview_open.read()
                                                                # open files and reads them, if an error occurs
            print(task_overview_read)                           # generates files using call func then continue 
            print(user_overview_read)

            break
        except:
            task_overview()
            user_overview()
            continue

# =================== End of Display Statistics ===================












                         
                




while Login == True:
    # =================== Displaying  menu's ===================
    print("\nMain Menu\n")
    if username == "admin":
        menu = input("""r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
Please choose one of the options:  """).lower()
    
    else:
        menu = input("""a - add task
va - view all tasks
vm - view my tasks
e - exit
Please choose one of the options: """).lower()
    # =================== End of displaying menu's ===================

    if menu == "r":
        print("\nRegister a new user:\n")
        reg_user(username)    

    elif menu == "a":
        print("\nAdd a new task:\n")
        add_task()
    
    elif menu == "va":
        print("\nDisplaying all tasks: \n")
        task_dictionary()
        view_all(thisdict)
        
    elif menu == "vm":
        print(f"\nDisplaying tasks for: {username}\n")
        task_dictionary()
        view_mine()
    
    elif menu == "gr":
        task_dictionary()
        task_overview()
        user_overview()
        print("\nReports have been generated.\n")
        pass

    elif menu == "ds":
        print(f"\nDisplaying Statistics:\n")
        task_dictionary()
        display_statistics()
        

    elif menu == "e":
        print("\nExiting Program.\n")
        exit()
        
    
            
