from tkinter import *


def SignInBtnClick():
    username = txtNum1.get()
    password = txtNum2.get()

    with open("username.txt", "r") as f:
        allData = f.readlines()
        for x in allData:
            data = x.strip().split(",")
            if data[0] == username and data[1] == password:
                lblResult.config(text="User already exists. Wanna Login?")
                break
        else:
            with open("username.txt", "a") as myfile:
                myfile.write(f"{username},{password}\n")
            with open(f"{username}_balance.txt", "w") as balance_file:
                balance_file.write("0")
            lblResult.config(text="New user added. Login, please")


def loginBtnClick():
    obj.destroy()

    def login():
        username = txtNum1.get()
        password = txtNum2.get()

        with open("username.txt", "r") as f:
            allData = f.readlines()
            for x in allData:
                data = x.strip().split(",")
                if data[0] == username and data[1] == password:
                    lblResult.config(text="Login successful")
                    balance_file_name = f"{username}_balance.txt"
                    open_balance_file(balance_file_name)
                    break
            else:
                lblResult.config(text="Login failed")

    def open_balance_file(balance_file_name):
        def view_balance():
            with open(balance_file_name, "r") as balance_file:
                balance = balance_file.read()
                lblResult.config(text=f"Your balance is {balance}")

        def deposit():
            amount = float(txtNum3.get())
            with open(balance_file_name, "r+") as balance_file:
                balance = float(balance_file.read())
                new_balance = balance + amount
                balance_file.seek(0)
                balance_file.write(str(new_balance))
                balance_file.truncate()
                lblResult.config(text=f"Deposit successful. New balance is {new_balance}")

        def withdraw():
            amount = float(txtNum3.get())
            with open(balance_file_name, "r+") as balance_file:
                balance = float(balance_file.read())
                if amount > balance:
                    lblResult.config(text="Insufficient funds")
                else:
                    new_balance = balance - amount
                    balance_file.seek(0)
                    balance_file.write(str(new_balance))
                    balance_file.truncate()
                    lblResult.config(text=f"Withdrawal successful. New balance is {new_balance}")

        obj2 = Tk()
        lblNum3 = Label(obj2, text="Enter Amount")
        txtNum3 = Entry(obj2)
        btnViewBalance = Button(obj2, text="View Balance", command=view_balance)
        btnDeposit = Button(obj2, text="Deposit", command=deposit)
        btnWithdraw = Button(obj2, text="Withdraw", command=withdraw)

        lblNum3.pack()
        txtNum3.pack()
        btnViewBalance.pack()
        btnDeposit.pack()
        btnWithdraw.pack()
        lblResult.pack()

        obj2.mainloop()

    obj2 = Tk()
    lblNum1 = Label(obj2, text="Enter Username")
    lblNum2 = Label(obj2, text="Enter Password")
    lblResult = Label(obj2, text=".........")
    txtNum1 = Entry(obj2)
    txtNum2 = Entry(obj2, show="*")
    btnLogin = Button(obj2, text="Login", command=login)

    lblNum1.pack()
    txtNum1.pack()
    lblNum2.pack()
    txtNum2.pack()
    btnLogin.pack()
    lblResult.pack()

    obj2.mainloop()


obj = Tk()
lblNum1 = Label(obj, text="Enter Username")
lblNum2 = Label(obj, text="Enter Password")
lblResult = Label(obj, text=".........")
txtNum1 = Entry(obj)
txtNum2 = Entry(obj, show="*")
btnSignIn = Button(obj, text="SignIn", command=SignInBtnClick)
btnLogin = Button(obj, text="Login", command=loginBtnClick)

lblNum1.pack()
txtNum1.pack()
lblNum2.pack()
txtNum2.pack()
btnSignIn.pack()
lblResult.pack()
btnLogin.pack()

obj.mainloop()