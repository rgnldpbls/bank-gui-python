#imports
from tkinter import * #graphical user interface in python programming language.
import os #provides a way of using operating system dependent functionality.
from PIL import ImageTk, Image #PIL is Python Imaging Library which provides the python interpreter with image editing capabilities.

#Main Screen
master = Tk() #allows you to program the execution of your own function so that it is executed after a certain amount of time.
master.title('Metrobank App')
master.configure(background="dark blue")

#Functions
def register(): #It is the function for the register
    #Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    register_screen.configure(background="dark blue")

    #Labels provide text information
    Label(register_screen, text="Please enter your details below to register", bg="dark blue", fg="white",font=("Georgia",16,"bold")).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", bg="dark blue", fg="white",font=('Georgia',16)).grid(row=1, sticky=W)
    Label(register_screen, text="Age", bg="dark blue", fg="white",font=('Georgia',16)).grid(row=2, sticky=W)
    Label(register_screen, text="Gender", bg="dark blue", fg="white",font=('Georgia',16)).grid(row=3, sticky=W)
    Label(register_screen, text="Password", bg="dark blue", fg="white",font=('Georgia',16)).grid(row=4, sticky=W)
    notif = Label(register_screen, bg="dark blue",font=('Georgia',16,"bold"))
    notif.grid(row=6,sticky=N,pady=10)

    #Entry or a text box where in the user can type via the keyboard
    Entry(register_screen, textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password).grid(row=4, column=0)

    #Buttons is a control that the user clicks to trigger a specific action or to select an option in a program.
    Button(register_screen, text="Register",fg="dark blue",command=finish_reg, font=('Georgia',12,"bold"),width=12).grid(row=5,sticky=N,pady=10)

def finish_reg(): #This function is used for checking the def register
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_account = os.listdir()
    if name == "" or age == "" or gender == "" or password == "": #This statement check the empty input
        notif.config(fg="yellow", text="All fields required")
        return

    for name_check in all_account:
        if name == name_check: #This statement check if the account name is duplicated
            notif.config(fg="yellow", text="Account already exists")
            return
        else: #If the following condition is not satisfied it will create a new file
            new_file = open(name, "w") #Opening a file
            new_file.write(name+'\n')  #Writing a file
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close() #Closing a file
            notif.config(fg="light green", text="Account has been created")

def login(): #It is the function for login
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title("Login")
    login_screen.configure(background="dark blue")

    #Labels provide text information
    Label(login_screen, text="Login to your account", bg = "dark blue", fg= "white", font=('Georgia',16,"bold")).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", bg = "dark blue", fg= "white", font=('Georgia', 16)).grid(row=1, sticky=W, pady=10)
    Label(login_screen, text="Password", bg = "dark blue", fg= "white",font=('Georgia', 16)).grid(row=2, sticky=W, pady=10)
    login_notif = Label(login_screen, bg="dark blue",font=('Georgia',16,"bold"))
    login_notif.grid(row=4,sticky=N)

    #Entry or a text box where in the user can type via the keyboard
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password).grid(row=2, column=1, padx=5)

    #Button is a control that the user clicks to trigger a specific action or to select an option in a program.
    Button(login_screen, text="Login", fg="blue", command=login_session, width=12, font=('Georgia',14,"bold")).grid(row=3,sticky=W,pady=5,padx=5)

def login_session(): #It is the function for checking the information in login and it displayed the account dashboard
    global login_name
    global account_dashboard
    all_account = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_account:
        if name == login_name: #It is a condition to compare the input name and the stored login name
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]

            #Account Dashboard
            if login_password == password: #It is a condition to compare the input password and stored password
                login_screen.destroy() #It destroyed the last screen
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                account_dashboard.configure(background="sky blue")

                #Labels provide text information
                Label(account_dashboard, text="Account Dashboard", bg="sky blue",font=('Georgia',16,"bold","underline")).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome, " + name, bg="sky blue", font=('Georgia',16,"bold")).grid(row=1,sticky=N,pady=5)

                #Buttons is a control that the user clicks to trigger a specific action or to select an option in a program.
                Button(account_dashboard, text="Account Details", fg = "blue",font=('Georgia',16,"bold"),width=20, command=account_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard, text="Deposit",fg="blue", font=('Georgia',16,"bold"),width=20, command=deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard, text="Withdraw", fg="blue",font=('Georgia',16,"bold"),width=20, command=withdraw).grid(row=4,sticky=N,padx=10)
                Label(account_dashboard, bg="sky blue").grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="yellow",text="Password Incorrect!!")
                return
        else:
            login_notif.config(fg="yellow", bg="dark blue", text="No Account Found!")
def deposit(): #It is the function for deposit
    #Vars
    global deposit_amount
    global deposit_notif
    global current_balance_label
    deposit_amount = StringVar()

    file = open(login_name, "r") #Opening a file
    file_data = file.read() #Reading a file
    user_details = file_data.split('\n') #Splitting the data from the file
    details_balance = user_details[4]

    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")
    deposit_screen.configure(background="sky blue")

    #Label provide text information
    Label(deposit_screen, bg="sky blue", text="Deposit", font=('Georgia',16,"bold")).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen, bg="sky blue", text="Current Balance: ₱"+ details_balance, font=('Georgia',16))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen, bg="sky blue",text="Amount:₱", font=('Georgia', 16)).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_screen,bg="sky blue", font=('Georgia',16))
    deposit_notif.grid(row=4,sticky=N,pady=5)

    #Entry or a text box where in the user can type via the keyboard
    Entry(deposit_screen, textvariable=deposit_amount).grid(row=2,column=1,padx=5)

    #Button is a control that the user clicks to trigger a specific action or to select an option in a program.
    Button(deposit_screen, text="Finish", fg="blue", font=('Georgia',12,"bold"),command=finish_deposit,width=10).grid(row=3,sticky=W,pady=5,padx=5)

def finish_deposit(): #This function is for checking the inputs and updating the balance
    if deposit_amount.get() == "": #It is a statement to check if the entry is empty
        deposit_notif.config(text="Amount is required!",fg="red")
        return
    if float(deposit_amount.get()) <0: #It is a statement to check if the input is less than 0
        deposit_notif.config(text="Negative Currency is not Accepted!",fg="red")
        return

    file = open(login_name, 'r+') #Opening the file
    file_data = file.read() #Reading the file
    details = file_data.split('\n') #Splitting the file
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(deposit_amount.get()) #Computing
    file_data = file_data.replace(current_balance, str(round(updated_balance,2))) # It is utilized to search for a sub-string and replace it with another sub-string.
    file.seek(0) #change the position of the File Handle to a given specific position.
    file.truncate(0)
    file.write(file_data)
    file.close() #Closing the file

    current_balance_label.config(text="Current Balance: ₱"+str(round(updated_balance,2)),fg="green")
    deposit_notif.config(text="Balance Updated",fg="green")

def withdraw(): #It is the function for withdraw
    # Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()

    file = open(login_name, "r") #Opening the file
    file_data = file.read() #Reading the file
    user_details = file_data.split('\n') #Splitting the file
    details_balance = user_details[4]

    #Withdraw Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")
    withdraw_screen.configure(background="sky blue")

    # Label provide text information
    Label(withdraw_screen, bg="sky blue", text="Withdraw", font=('Georgia', 16,"bold")).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, bg="sky blue", text="Current Balance: ₱" + details_balance, font=('Georgia', 16))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, bg="sky blue", text="Amount:₱", font=('Georgia', 16)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, bg="sky blue", font=('Georgia', 16))
    withdraw_notif.grid(row=4, sticky=N, pady=5)

    # Entry or a text box where in the user can type via the keyboard
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2, column=1,padx=5)

    # Button is a control that the user clicks to trigger a specific action or to select an option in a program.
    Button(withdraw_screen, text="Finish", fg="blue", font=('Georgia', 12,"bold"), command=finish_withdraw,width=10).grid(row=3, sticky=W, pady=5,padx=5)

def finish_withdraw(): #This function is for checking the data inputted in the upper function and for updating the balance
    if withdraw_amount.get() == "": #It is a statement to check if the entry is empty
        withdraw_notif.config(text="Amount is required!",fg="red")
        return
    if float(withdraw_amount.get()) <0: #It is a statement to check if the input data is less than 0
        withdraw_notif.config(text="Negative Currency is not Accepted!",fg="red")
        return

    file = open(login_name, 'r+') #Opening the file
    file_data = file.read() #Reading the file
    details = file_data.split('\n') #Splitting the file
    current_balance = details[4]
    if float(withdraw_amount.get()) > float(current_balance): #It is statement to check if the input data is greater than on the current balance
        withdraw_notif.config(text="Insufficient Funds!",fg="red")
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get()) #Computing
    file_data = file_data.replace(current_balance, str(round(updated_balance,2))) # It is utilized to search for a sub-string and replace it with another sub-string.
    file.seek(0) #change the position of the File Handle to a given specific position.
    file.truncate(0)
    file.write(file_data)
    file.close() #Closing the file

    current_balance_label.config(text="Current Balance: ₱"+str(round(updated_balance,2)),fg="green")
    withdraw_notif.config(text="Balance Updated",fg="green")

def account_details(): #It is the function for the account details
    global acc_details_screen
    #Vars
    file = open(login_name, 'r') #Opening the file
    file_data = file.read() #Reading the file
    user_details = file_data.split('\n') #Splitting the file
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]

    #Account Details Screen
    acc_details_screen = Toplevel(master)
    acc_details_screen.title("Account Details")
    acc_details_screen.configure(background="sky blue")

    #Label provide text information
    Label(acc_details_screen, bg="sky blue", text="Account Details", font=("Georgia",16,"bold")).grid(row=0,sticky=N,pady=10)
    Label(acc_details_screen, bg="sky blue", text="Name:"+details_name, font=("Georgia", 16)).grid(row=1, sticky=W)
    Label(acc_details_screen, bg="sky blue", text="Age: " + details_age, font=("Georgia", 16)).grid(row=2, sticky=W)
    Label(acc_details_screen, bg="sky blue", text="Gender: " + details_gender, font=("Georgia", 16)).grid(row=3, sticky=W)
    Label(acc_details_screen, bg="sky blue",text="Balance: ₱" + details_balance, font=("Georgia", 16)).grid(row=4, sticky=W,pady=10)

    #Button is a control that the user clicks to trigger a specific action or to select an option in a program.
    Button(acc_details_screen, text="Edit Account Details", fg="blue", font=('Georgia', 12, "bold"), width=15,command=edit_details).grid(row=5, sticky=W, padx=10)

def edit_details(): #This function is for editing the account details
    global update_password
    global update_age
    global update_gender
    global edit_details_notif
    update_password = StringVar()
    update_age = StringVar()
    update_gender = StringVar()
    file = open(login_name, "r")  #Opening the file
    file_data = file.read() #Reading the file
    user_details = file_data.split('\n') #Splitting the file
    details_name = user_details[0]

    # Edit_details Screen
    acc_details_screen.destroy()
    edit_details_screen = Toplevel(master)
    edit_details_screen.title("Edit Details")
    edit_details_screen.configure(background="sky blue")

    # Label provide text information
    Label(edit_details_screen,bg="sky blue", text="Edit Account Details", font=('Georgia', 16, "bold")).grid(row=0, sticky=N, pady=10)
    Label(edit_details_screen, bg="sky blue", text="Name: " + details_name, font=('Georgia', 16)).grid(row=1, sticky=W)
    Label(edit_details_screen, bg="sky blue", text="Password: ", font=('Georgia', 16)).grid(row=2, sticky=W)
    Label(edit_details_screen, bg="sky blue", text="Age: ", font=('Georgia', 16)).grid(row=3, sticky=W)
    Label(edit_details_screen, bg="sky blue", text="Gender: ", font=('Georgia', 16)).grid(row=4, sticky=W)
    edit_details_notif = Label(edit_details_screen, bg="sky blue", font=('Georgia', 16))
    edit_details_notif.grid(row=6, sticky=N, pady=5)

    # Entry or a text box where in the user can type via the keyboard
    Entry(edit_details_screen, textvariable=update_password).grid(row=2,column=1,padx=5)
    Entry(edit_details_screen, textvariable=update_age).grid(row=3,column=1,padx=5)
    Entry(edit_details_screen, textvariable=update_gender).grid(row=4,column=1,padx=5)

    # Button is a control that the user clicks to trigger a specific action or to select an option in a program.
    Button(edit_details_screen, text="Save", fg="blue", command=finish_edit_details, font=('Georgia', 12, "bold"),width=15).grid(row=5,sticky=W,pady=10,padx=5)

def finish_edit_details(): #This function is for checking the inputted data and updating the file
    if update_password.get() == "" or update_age.get() == "" or update_gender.get() == "": #It is a statement to check if the entry is empty
        edit_details_notif.config(fg="red", text="All fields required")
        return
    file = open(login_name, 'r+') #Opening the file
    file_data = file.read() # Reading the file
    details = file_data.split('\n') #Splitting the file

    current_password = details[1]
    current_age = details[2]
    current_gender = details[3]

    new_password = update_password.get()
    new_age = update_age.get()
    new_gender = update_gender.get()

    file_data = file_data.replace(current_password, str(new_password))
    file_data = file_data.replace(current_age, str(new_age))
    file_data = file_data.replace(current_gender, str(new_gender))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    edit_details_notif.config(text="Account Details Updated", fg="green")

#Image import
img = Image.open('logo.png')
img = img.resize((200,150))
img = ImageTk.PhotoImage(img)

#Labels is provide text information
Label(master, bg="dark blue", text= "Metrobank", fg="white", font=("Georgia",40,"bold")).grid(row=0,sticky=N,pady=10)
Label(master, bg="dark blue", text= "\"You're in good hands\"",fg="white", font=('Georgia',20)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#Buttons is a control that the user clicks to trigger a specific action or to select an option in a program.
Button(master, text="Register",fg="blue",font=('Georgia',16,"bold"),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="Login", fg= "blue",font=('Georgia',16,"bold"),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop() #It is like a while loop,  this will keep running until the user exits