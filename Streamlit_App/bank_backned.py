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
            pass  # File will be created on update
    except Exception as err:
        print(f"An error occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accNoGenerate(cls):
        alpha = random.choices(string.ascii_uppercase, k=4)
        digits = random.choices(string.digits, k=5)
        id = alpha + digits
        random.shuffle(id)
        return "GDBL" + "".join(id)

    def createAccount(self, name, age, email, pin):
        # Validation checks
        if age < 18:
            return "Error", "Sorry you're not old enough to create an account"
        if len(str(pin)) != 4:
            return "Error", "Pin should be of 4 digits"

        # Logic
        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo.": Bank.__accNoGenerate(),
            "balance": 0,
        }

        Bank.data.append(info)
        Bank.__update()
        return "Success", info["accountNo."]

    def deposit(self, accNo, pin, amount):
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]

        if len(userdata) == 0:
            return "Error", "Sorry no data found"
        else:
            if amount > 10000 or amount < 0:
                return "Error", "Sorry the amount is more than the permissible amount"
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                return "Success", "Amount deposited successfully"

    def withdraw(self, accNo, pin, amount):
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]

        if len(userdata) == 0:
            return "Error", "Sorry no data found"
        else:
            if userdata[0]["balance"] <= amount:
                return "Error", "Insufficient Balance"
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                return "Success", "Amount withdrawn successfully"

    def showDetails(self, accNo, pin):
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]
        if len(userdata) == 0:
            return "Error", "Sorry, no data found"
        else:
            return "Success", userdata[0]

    def updateDetails(self, accNo, pin, name, email, new_pin):
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]

        if len(userdata) == 0:
            return "Error", "Sorry, no data found"
        else:
            newdata = {
                "name": name,
                "email": email,
                "pin": new_pin,
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
            return "Success", "Details updated"

    def deleteUser(self, accNo, pin):
        userdata = [
            i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin
        ]

        if len(userdata) == 0:
            return "Error", "Sorry, no data found"
        else:
            index = Bank.data.index(userdata[0])
            Bank.data.pop(index)
            Bank.__update()
            return "Success", "Account Deleted Successfully"
