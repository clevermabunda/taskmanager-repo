#***************commnents************
# Create a program for a small business to help manage tasks assigned to each member of the team.
# Use the template provided and modify it to achieve the task.
# Work with two text files,user.txt and tasks.txt.
# task.txt stores a list of tasks the team is working on.
# User.txt stores the username and password for each user that has permission to use program.
# Program should allow the user to ender their username and password.
# Validate the username and password.
# If the credentials are correct the user should be allowed to proceed and only be restricted to options that are for the admin. 

#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
import os, time
import stat

#====Login Section====


def login():                               # login reads the username and password from the user.txt file
    username_list = {}

    with open("user.txt", "r") as login_file:
        for line in login_file:  
            user_credential = line.strip("\n")
            if user_credential != "":
                user_credential = user_credential.split(", ")
                username_list.update({user_credential[0]: user_credential[1]})
            
    return username_list        


def login_account():                      # login account validates the credentials(username and password) before proceeding to the next step. 
    
    username = input("Enter username:").lower()
    password = input("Enter password:") 
    print() 

    username_list = login()
    # All the usernames are found in the username list above.login account will validate them.

    if username in username_list and username_list.get(username) == password:
        return username

    else :
        print ("Invalid username or password, please try again!!")
        return "invalid"
    
    
def menu():                           # Menu shows the main menu 
    
    continue_next = True
    
    while continue_next:
        print("Please select one of the following options:\n")
        print("r -> register user")
        print("a -> add task")
        print("va -> view all tasks")
        print("vm -> view my tasks")
        print("gnt -> generate reports")

    # only admin should be able to access the display(ds) statistics and there restrictions are made.
        if admin_login :
            print("ds -> display statistics")

        print("e -> exit")
        print()
        selection = input()
        print()

        if selection.lower() == "r":
            reg_user()

        elif selection.lower() == "a":
            add_task()

        elif selection.lower() == "va":
            view_all()

        elif selection.lower() == "vm":
            view_mine() 

        elif selection.lower() == "ds":
            display_statistics()

        elif selection.lower() == "e":
            continue_next = False

        elif selection.lower() == "gnt":
            generate_reports()

        else:
            print("Please make the correct selection from the menu!!!\n")                   

def reg_user():                   # Allows the admin to register new usernames and passwords, and store them in user.txt file.
      
      admin_login = 'admin'       # Only admin have the access to register the new username.
      continue_on = True

      username_list = login()

      if admin_login == False:
           print("Only admin have the access to this menu!!!")

      else:
           
           while (continue_on):
                            
                with open('user.txt', 'a') as f:
                     new_username = input("Enter your new username: ")
                     if new_username == username_list:
                         print("The username you entered already exist please another username")
                     else:
                         new_password = input("Enter your new password: ")
                         password_confirm = input("Re-enter your password to confirm: ")
            
                         if new_password == password_confirm:
                             f.write(f"\n{new_username}, {new_password}")
                             print()
                             continue_on = False
                         else:
                             print("Password does not match, please try again!")  


def task_check():
                       # will be able to read task from the file for any further use.
    task = []
    count = 1

    with open("tasks.txt", "r") as file:
        for line in file:
            task_check = line.strip("\n")  # seperate the lines from the file using strip with new line.
            if task_check != "" :
                task_check = [task_check.split(", ") + [count]] # split if not splited and count the number of tasks
                task.extend(task_check)        # append task_check to task[]
                count += 1

    return task


def add_task():                         # add task will allow the user to add the task into the tasks file.

    with open("tasks.txt", "a") as f:
        user_name = input("Enter the username:")
        title = input("Enter the title of the task:")
        description = input("Enter the description of the task:")
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        due_date_input = input("Enter the due date of the task:dd/mm/yyyy:")
        complete = "No"
        f.write(f"{user_name}, {title}, {description}, {current_date}, {due_date_input}, {complete}\n")


def view_all():               # Create a function to view all the tasks
        
    with open("tasks.txt", "r") as f:     # open the tasks.txt file and read it.
        for line in f:
            view_all_task = line.strip('\n').split(', ')   # split the line in the file into a list and use the index number to organise and print all the tasks stored in the file.

            print ('\n-------------------------------------------------------------------------------')
            print (f'Task:\t\t\t{view_all_task[1]}')
            print (f'Assigned to:\t\t{view_all_task[0]}')
            print (f'Date assigned:\t\t{view_all_task[3]}')
            print (f'Due date:\t\t{view_all_task[4]}')
            print (f'Task Complete?\t\t{view_all_task[5]}')
            print (f'Discription:\n{view_all_task[2]}')
            print('-------------------------------------------------------------------------------\n')


def view_mine():                           # Create a funtion to view taks that are allocated to a particular individual.

    task = task_check()

    for i in range(0, len(task)):
       
        if user == task[i][0]:

                print("............................................................")
                print(f"Task number:\t\t{task[i][6]}")
                print(f"Task:\t\t\t{task[i][1]}")
                print(f"Assigned to:\t\t{task[i][0]}")
                print(f"Date assigned:\t\t{task[i][3]}")
                print(f"Due date:\t\t{task[i][4]}")
                print(f"Task complate?\t\t{task[i][5]}")
                print(f"Task description:\n{task[i][2]}")
                print("............................................................")
    select_task()


def select_task() :
    # task_check will be able to read tasks from the file and make easy to select a task.
    tasks = task_check()
    
    # create a varible task_choice and initialising it as True.
    task_choice = True

    while(task_choice):

        task_num = input("Enter the task number: ")

        try:
            task_num = int(task_num)

        except:
            print("Input invalid!!")

        if task_num == -1:
            print("goodbye!")
            task_choice = False
            return
        else:
            for i in range(0, len(tasks)):
                if task_num == tasks[i][6] and tasks[i][5].lower() == "yes":
                    print(f"The task number {task_num} is completely marked and cannot be edited!")

                elif  task_num == tasks[i][6]:
                    specific_menu = input('''Select one of the following options:  
tc - mark task as complete
et - edit task                                                 
-1 - exit
: ''').lower()
                    print()
                    if specific_menu != 'tc' and specific_menu != 'et':
                        print("Invalid!!")

                    elif specific_menu == 'tc':
                        mark_task(task_num)
                        return
                    elif specific_menu == "-1":
                        print ("goodbye!")
                    else:
                        edit_task(task_num)
                        return
                              

def mark_task(task_num):             # Mark task will be able to mark the task as complete.

  tasks = task_check()
  string_task = ""
  # use indexs[6] to change task index 5 from No to Yes. Break after the changes to avoid further looping. 
  for i in range(0, len(tasks)):
      if task_num == tasks[i][6]:
          tasks[i][5] = "Yes"
          break
    
    # creating a variable all_t that contains all tasks as string. After the changes from No to Yes, the tasks needs to be rejoined in a string format.
  all_t = [", ".join(t[:6]) for t in tasks]

  # join all the tasks with newline(\n) and use string_task as a variable.
  string_task = '\n'.join(all_t)

  with open("tasks.txt", "w") as f:
      f.write(string_task)


def edit_task(task_num):             # edit task enables the user to edit the tasks due date, the username allocated to a particular tasks, but only if the task is not marked.

    tasks = task_check()
    username_list = login()

    string_task = ""
    edit = True

    while(edit):
        user_edit = input("Please enter et to edit the task: ")

        if user_edit.lower() == "et":
            new_username = input("Please enter the new assigned task username: ")
            if new_username in username_list:
                new_date = input("Please enter the new due date for the task: dd/mm/yyyy: ")
                      
                 # if the task is not marked, you can modify the username and date.     
                for i in range(0, len(tasks)):
                    if task_num == tasks[i][6]:
                        tasks[i][0] = new_username
                        tasks[i][4] = new_date

                    tasks[i].pop()

                    string_task += ", ".join(tasks[i]) + "\n" 

                    edit = False

            else:
                print("Your username is wrong!!")

    with open("tasks.txt", "w") as f:
        f.write(string_task)            
        

def generate_reports():                    # generate reports shows the total reports of the tasks that are marked as complete and incomplete in percentage
    task = task_check()
    username_list = login()

    username_list = [*username_list]
    # initialize the variables to zero before making the counts.
    total = len(task)
    total_users = len(task)
    complete = 0
    incomplete = 0
    overdue = 0 
    incomplete_percent = 0
    overdue_percent = 0

    for i in range(0, total) :
        if task[i][5].lower() == "yes" :
            complete += 1

        elif task[i][5].lower() == "no" :
            incomplete += 1
            overdue += 1
            incomplete_percent = (incomplete/total) * 100
            overdue_percent = (overdue/total) * 100

        elif task[i][5].lower() == "no":
            incomplete += 1
            incomplete_percent = (incomplete/total) * 100      # calculating the percentage of incomplete tasks.

    with open("task_overview.txt", "w") as f:           # write the reports in task overview txt file.
        f.write(f"Number of tasks\t\t\t-> {total}\n")
        f.write(f"Number of complete\t\t-> {complete}\n")
        f.write(f"Number of incomplete\t\t-> {incomplete}\n")
        f.write(f"Number of overdue\t\t-> {overdue}\n")
        f.write(f"Incomplete percentage\t\t-> {incomplete_percent:2f}%\n")
        f.write(f"Overdue percentage\t\t-> {overdue_percent:.2f}%\n")

    with open("user_overview.txt", "w") as p:            # write the total users and total tasks in user overview txt file.
        p.write(f"Total users\t\t-> {total_users}\n")
        p.write(f"Total tasks\t\t-> {total}\n")

        for i in range(0, total_users):
            # initialize the variables to zero
            user_task = 0
            completed = 0
            none_completed = 0
            user_overdue = 0
            percent = 0
            percentage_of_complete = 0
            percentage_of_incomplete = 0
            percent_of_overdue = 0

            for t in range(0, total):
                if username_list[i] == task[t][0] and task[t][5].lower() == "yes":
                    user_task += 1
                    completed += 1

                elif username_list[i] == task[t][0] and task[t][5].lower() == "no":
                    user_task += 1
                    none_completed += 1
                    user_overdue += 1

                elif username_list[i] == task[t][0] and task[t][5].lower() == "no":
                    user_task += 1
                    none_completed += 1

                percent = (user_task/total) * 100
                if user_task != 0:
                    percentage_of_complete = (completed / user_task) * 100
                    percentage_of_incomplete = (none_completed / user_task) * 100
                    percent_of_overdue = (user_overdue / user_task) * 100

            p.write("-" * 50 + "\n")
            p.write(f"User: {username_list[i]}\n")
            p.write(f"Number of tasks\t\t-> {user_task}\n")
            p.write(f"Total percentage of tasks\t-> {percent:.2f}%\n")
            p.write(f"Percentage of task completed\t\t-> {percentage_of_complete:.2f}%\n")
            p.write(f"Percentage of task incomplete\t\t-> {percentage_of_incomplete:.2f}%\n")
            p.write(f"Percentage of overdue\t\t-> {percent_of_overdue:.2f}%\n")
            
   
def display_statistics():                          # display statistics show the date and time when the tasks were marked as complete or modified.

    past_file = True

    if (os.path.exists("./task_overview.txt") == False) or (os.path.exists("./user_overview.txt") == False):
        generate_reports()

    else:

        task_time = os.stat("task_overview.txt")
        task_time = time .ctime(task_time[stat.ST_MTIME])

        user_time = os.stat("user_overview.txt")
        user_time = time.ctime(user_time[stat.ST_MTIME])

        print(f"task_overview was edited at {task_time}\n")
        print(f"user_overview was edited at {user_time}\n")

        while (past_file):
            regenerate = input("Are you willing to update the files? Please answer with a yes or no: \n")

            if regenerate.lower() == "yes":
                generate_reports()
                past_file = False

            elif regenerate.lower() == "no":
                past_file = False

            else:
                print ("Invalid!!")  

    with open("task_overview.txt", "r") as f:
        for line in f:
            print(line, end = "")

    print()

    with open("user_overview.txt", "r") as p:
        for line in p:
            print (line, end = "")

login_user = True                       # validating the username and making some restrictions to allow admin access.
admin_login = False

while (login_user):
    user = login_account()
    print(user)
    if user == "admin":
        admin_login = True
        login_user = False

    elif user != "invalid":
        login_user = False    
menu()