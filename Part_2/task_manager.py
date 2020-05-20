print("\t\t\t\t\t\t\t\t\tL O G I N")
fl = open("user.txt", "r+")
rfl = fl.read()
user = input("Enter your username:\n")
password = input("Enter your password (case sensitive):\n")


while user.lower() not in rfl:
    print("This username does not exist, please try again.")
    user = input("\n\nEnter your username:\n")
    break


while password.lower() not in rfl:
    print("The password entered is incorrect,check and try again.")
    password = input("Enter your password (case sensitive):\n")
    break

fl.close()
print("Welcome! \n\n")
if user == "admin":                       # Provides only 'admin' with the stats option in the menu.
    print("Please select one of the following options:\n "
          "r - register user\n "
          "a - add task\n "
          "va - view all tasks\n "
          "vm - view my tasks\n "
          "s - view statistics\n "
          "e - exit\n")
else:
    print("Please select one of the following options:\n "
          "r - register user\n "
          "a - add task\n "
          "va - view all tasks\n "
          "vm - view my tasks\n "
          "e - exit\n")

option = input(":\t")


if option.lower() == "r":
    if user == admin:                   # Ensures that only 'admin' can access this option.
        fl = open('user.txt', 'r+')
        rfl = fl.read()
        new_user = input("Enter new username:\n")
        new_pass1 = input("Enter a password for this user:\n")
        new_pass2 = input("Confirm the above password:\n")

        while new_pass2 != new_pass1:
            print("\n\n Your passwords do not match, please check and try again. \n")
            new_pass2 = input("Confirm the above password:\n")
    
        fl.write("\n" + new_user + ", " + new_pass1)
        user_count = 0
        for line in fl:
            user_count += line
        fl.close()
        
    else:
        print("Only Admin users can use this feature.")
    
elif option.lower() == "a":
    task_user = input("Enter the user that this task will be assigned to:\n")
    title = input("Enter the title of this task:\n")
    desc = input("Enter a task description:\n")
    from datetime import date                           
    today = str(date.today())                           
    due = input("Enter the tasks due date:\n")
    fl = open('tasks.txt', 'r+')
    rfl = fl.read()
    fl.write("Task:\t" + title+"\n"
             + "Assigned to:\t" + task_user+"\n"
             + "Description of task:\t" + desc + "\n"
             + "Date assigned:\t"+today + "\n"
             + "Due date:\t" + due + "\n"
             + "Completed?:\t" + "No")
    fl.close()
    
                                        
elif option.lower() == "va":                            
    fl = open("tasks.txt", "r+")
    rfl = fl.read()
    print(rfl)
    fl.close()
    
    
elif option.lower() == "vm":                            
    with open('tasks.txt') as fl:                       
        for line in fl:
            if user in line:
                for i in range(5):
                    after_line = next(fl)               
                    print("\n" + after_line)
    fl.close()
    
elif option.lower() == "s":         # For 's'.
    if user == 'admin':
        with open('user.txt') as fl:
            line_count = 0
            for i in fl:
                line_count += 1
                users = line_count - 1
        print("Total number of registered users:\t", users)
        fl.close()
    # Since each user in "user.txt" is on a new line the for loop counts each line then
    # subtracts 1 (to exclude empty lines), ultimately counting the amount of users.

        with open('tasks.txt', 'r+') as fl:
            task_count = 0
            for line in fl:
                if "Task:" in line:
                    task_count += 1
        print("Total number of tasks:\t", task_count)
        fl.close()                
        # Since each task contains the string "Task:"  the for loop counts every line
        # that contains the specified string,ultimately counting each task.
        

elif option.lower() == "e":                             
    exit(0)
    
else:
    exit(0)
