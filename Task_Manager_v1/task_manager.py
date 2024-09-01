from datetime import date
# ==== Login ====
login_details = open("user.txt", "r+")
read_login_details = login_details.readlines()
cleaned_login_details = [details for details in read_login_details if details != "\n"]
# I decided to add this line above because my code would sometimes leave whitespaces in the txt file, which in turn
# breaks my whole code when trying to restart it because of the whitelines in the txt file. With this, i remove the empty lines
# which cleans my list and then i can carry on as normal everytime without having to manually delete the whitelines
#print(cleaned_login_details)
username_list = []
password_list = []
# ============ ASSIGNING LOGIN VARIABLES  ============
for line in cleaned_login_details:
    
    username, password = line.strip("\n").split(", ") # Here I split each list that appears into smaller lists
    username_list.append(username)                    # By splitting it and assigning it into a new list, this means that I can
    password_list.append(password)                    # Easily access a user or pass because each one will have the same index for the other

Login = False                                         # I set the default for being logged in to be false

# ============ END OF ASSIGNING LOGIN VARIABLES  ============


while True:
    try:
        username = input("Username: ")                                  
        password = input("Password: ")
        username_pos = username_list.index(username)
        if password == password_list[username_pos]:

            print(f"\nSuccessfully logged in \nWelcome {username}\n")
            Login = True
            break
                                                                     # I decided to gather the inputs for the username & password in one go
        else:                                                           # After this, I check if the entered username is on the list and find
            print("\nIncorrect Username or Password")                   # The index of it. By using try except, if the username is not in the
            print("Please try again\n")  
            Login = False                                               # List, it will return a valueerror which will then ask the user to
            continue                                                    # Enter their details again
                                                                        # By using the username index, for password list, we can check if the
                                                                        # Password set for the username is right or not.
    except ValueError:
        print("\nIncorrect Username or Password")
        print("Please try again\n")
        Login = False
        continue

login_details.close()
# ==== Login End ====

# ==== Menu Start ====
while Login == True:
    if username == "admin":
        menu = input("""Please select one of the following options:
r - register user
a - add task                                                            
va - view all tasks     
vm - view my tasks
ds - display statistics     
e - exit\n""").lower()
    else:
        menu = input("""Please select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit\n""").lower()
                                                        # Seperate menu's will show depending on whether the person logged in is
                                                        # an admin or not
    if menu == "r":
        if username == "admin":
          print("\nRegistering new user")
          add_login = open("user.txt", "a")
        

          new_username = input("Please enter your new username: ")        # Gather new login details along with password check
          new_password = input("Please enter your new password: ")
          password_check = input("Please re-enter your new password: ")

          if password_check == new_password:
            add_login.write(f"\n{new_username}, {new_password}")        # If passwords match, write new details into text file, else if not
          else:                                                           # Return back to menu
            print("Your passwords do not match.\nReturning back to the menu\n")

          add_login.close()
        
        else:
            print("\nSorry, only the admin can register new users.\n")
    

    elif menu == "a":
        print("\nAdding a new task")
        add_task = open("tasks.txt", "a")
        
        assigned_username = input("Please enter the username of the person to whom the task is assigned to:\n")
        task_title = input("Please enter the task title:\n")
        task_description = input("Please enter the description of the task:\n")
        date_assigned = date.today().strftime("%d %B %Y")
        due_date = input("Please enter the due date for the task:\n")
        task_completion = "No"

        add_task.write(f"\n{assigned_username}, {task_title}, {task_description}, {date_assigned}, {due_date}, {task_completion}")

        add_task.close()
    

    
    elif menu == "va":
        print("\nDisplaying all tasks:")
        
        display_task = open("tasks.txt", "r")
        read_display_task = display_task.readlines()
        cleaned_task_details = [details for details in read_display_task if details != "\n"] # Cleaning list same as above
        assigned_to_list = []
        task_list = []
        task_description_list = []
        assignment_date_list = []
        due_date_list = []
        completion_list = []

        for line in cleaned_task_details:
            assigned_to, task, task_description, assignment_date, due_date, completion =  line.strip("\n").split(", ")

            assigned_to_list.append(assigned_to)
            task_list.append(task)
            task_description_list.append(task_description)  # Over here I am essentially doing the same method as I did for user and pass 
            assignment_date_list.append(assignment_date)    # As above, just this time there are more variables
            due_date_list.append(due_date)
            completion_list.append(completion)
    
        display_task.close()

        # I decided to have the files read and assigned again for VA & VM because it allows the tasks to be updated each time if a new one is
        # Added, compared to if I did a global one, I was not able to have it constantly update if a new task was added


        for count,line in enumerate(cleaned_task_details):
            print("===============\n")
            print(f"Task: \t\t{(count + 1)}")
            print(f"Assigned to: \t{assigned_to_list[count]}")
            print(f"Task: \t\t{task_list[count]}")
            print(f"Date Assigned: \t{assignment_date_list[count]}")
            print(f"Date Due: \t{due_date_list[count]}")
            print(f"Task Complete? \t{completion_list[count]}")
            print(f"Task Description: \n{task_description_list[count]}")
            print("===============\n")
        
        
    elif menu == "vm":
        print(f"\nShowing tasks for: {username}")

        display_task = open("tasks.txt", "r")
        read_display_task = display_task.readlines()
        cleaned_task_details = [details for details in read_display_task if details != "\n"] # Cleaning list same as above
        assigned_to_list = []
        task_list = []
        task_description_list = []
        assignment_date_list = []
        due_date_list = []
        completion_list = []

        for line in cleaned_task_details:
            assigned_to, task, task_description, assignment_date, due_date, completion =  line.strip("\n").split(", ")

            assigned_to_list.append(assigned_to)
            task_list.append(task)
            task_description_list.append(task_description)  # Over here I am essentially doing the same method as I did for user and pass 
            assignment_date_list.append(assignment_date)    # As above, just this time there are more variables
            due_date_list.append(due_date)
            completion_list.append(completion)
    
        display_task.close()
        
        matching_tasks = [indexnumber for indexnumber,index in enumerate(assigned_to_list) if index == username]
        # I use list comprehension to create a new list with the index's for when the username
        # occurs in the assigned to list
        
        for count,index in enumerate(matching_tasks):
            print("===============\n")
            print(f"Task: \t\t{(count + 1)}")
            print(f"Assigned to: \t{assigned_to_list[index]}")
            print(f"Task: \t\t{task_list[index]}")
            print(f"Date Assigned: \t{assignment_date_list[index]}")
            print(f"Date Due: \t{due_date_list[index]}")
            print(f"Task Complete? \t{completion_list[index]}")
            print(f"Task Description: \n{task_description_list[index]}")
            print("===============\n")
    
    elif menu == "ds":
        display_task = open("tasks.txt", "r")
        read_display_task = display_task.readlines()
        cleaned_task_details = [details for details in read_display_task if details != "\n"] # Cleaning list same as above
        assigned_to_list = []
        task_list = []
        task_description_list = []
        assignment_date_list = []
        due_date_list = []
        completion_list = []

        for line in cleaned_task_details:
            assigned_to, task, task_description, assignment_date, due_date, completion =  line.strip("\n").split(", ")

            assigned_to_list.append(assigned_to)
            task_list.append(task)
            task_description_list.append(task_description)  # Over here I am essentially doing the same method as I did for user and pass 
            assignment_date_list.append(assignment_date)    # As above, just this time there are more variables
            due_date_list.append(due_date)
            completion_list.append(completion)
    

        login_details = open("user.txt", "r+")
        read_login_details = login_details.readlines()
        cleaned_login_details = [details for details in read_login_details if details != "\n"]

        username_list = []
        for line in cleaned_login_details:
    
            username = line.strip("\n").split(", ") # Here I split each list that appears into smaller lists
            username_list.append(username) 

        
        print("========================")
        print(f"The total number of tasks is : {len(assigned_to_list)}")
        print(f"The total number of users regisered are: {len(username_list)}")
        print("========================")

        login_details.close()
        display_task.close()

    
        
        
    elif menu == "e":
        print("\nYou have chosen to exit. Goodbye.")
        exit()
    
    else:
        print("\nInvalid input. Please choose one of the options from the menu.\n")

    
        
    

        
            
    

    

