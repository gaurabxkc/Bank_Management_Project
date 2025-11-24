import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []
    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(Bank.data))
            print("Data Upload Successful")

    @classmethod
    def __accNoGenerate(cls):
        aplha = random.choices(string.ascii_uppercase, k=4)
        digits = random.choices(string.digits, k=5)
        id = aplha + digits
        random.shuffle(id)
        return "GDBL" + "".join(id)

    def createAccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin": int(input("Set your 4 digit pin: ")),
            "accountNo.": Bank.__accNoGenerate(),
            "balance": 0,
        }
        print(info["accountNo."])
        if info["age"] < 18:
            print("Sorry you're not old enough to create an account")
        elif len(str(info["pin"])) != 4:
            print("Pin should be of 4 digits")
        else:
            print("Account Created Succcessfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("\nPlease note down your account number")
            Bank.data.append(info)
            Bank.__update()

    def deposit(self):
        accNo = input("Tell you account number")
        pin = int(input("Enter you 4 digit pin"))
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]
        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much money you wanna deposit: "))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is more than the permissible amount")

            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print("Amount deposited successfully")

    def withdraw(self):
        accNo = input("Tell you account number")
        pin = int(input("Enter you 4 digit pin"))
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]
        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much money you wanna withdraw: "))

            if userdata[0]["balance"] <= amount:
                print("Insufficient Balance")
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print("Amount withdrawn successfully")

    def showDetails(self):
        accNo = input("Tell you account number: ")
        pin = int(input("Enter you 4 digit pin: "))
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]
        if userdata == False:
            print("Sorry, no data found")
        else:
            print("Your details are\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updateDetails(self):
        accNo = input("Tell you account number: ")
        pin = int(input("Enter you 4 digit pin: "))
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]

        if bool(userdata) == False:
            print("Sorry, no data found")
        else:
            print("You cannot change your age and account number\n")
            print(
                "Fill the details for change or leave it empty if you dont wanna update"
            )

            newdata = {
                "name": input("Please tell your name: "),
                "email": input("Please tell your email: "),
                "pin": input("Enter new pin: "),
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            else:
                newdata["pin"] = int(newdata["pin"])

            for i in newdata:
                userdata[0][i] = newdata[i]
            Bank.__update()

    def deleteUser(self):
        accNo = input("Tell you account number: ")
        pin = int(input("Enter you 4 digit pin: "))
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]

        if bool(userdata) == False:
            print("Sorry, no data found")
        else:
            response = input("Press Y to confirm deletion")
            if response == "Y" or response == "y":
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Account Delted Successfully")


user = Bank()

print("Press 1 for creating an account")
print("Press 2 for making deposit")
print("Press 3 for wihtdrawing the money")
print("Press 4 for details")
print("Press 5 for updatindg the details")
print("Press 6 for deleting your account\n")

response = int(input("Tell your response: "))

if response == 1:
    user.createAccount()

if response == 2:
    user.deposit()

if response == 3:
    user.withdraw()

if response == 4:
    user.showDetails()

if response == 5:
    user.updateDetails()

if response == 6:
    user.deleteUser()
