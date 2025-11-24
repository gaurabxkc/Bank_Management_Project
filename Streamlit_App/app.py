import streamlit as st
from bank_backend import Bank

# Instantiate the bank class
user = Bank()

st.title("GDBL Banking System")

# Create the sidebar menu (replaces your print menu)
options = ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Menu", options)

if choice == "Create Account":
    st.header("Create New Account")
    name = st.text_input("Tell your name")
    age = st.number_input("Tell your age", step=1)
    email = st.text_input("Tell your email")
    pin = st.number_input("Set your 4 digit pin", step=1)
    
    if st.button("Create"):
        status, result = user.createAccount(name, int(age), email, pin)
        if status == "Success":
            st.success("Account Created Successfully")
            st.info(f"Your Account Number is: {result}")
            st.warning("Please note down your account number")
        else:
            st.error(result)

if choice == "Deposit":
    st.header("Deposit Money")
    accNo = st.text_input("Tell your account number")
    pin = st.number_input("Enter your 4 digit pin", step=1)
    amount = st.number_input("How much money you wanna deposit", step=100)
    
    if st.button("Deposit"):
        status, result = user.deposit(accNo, int(pin), int(amount))
        if status == "Success":
            st.success(result)
        else:
            st.error(result)

if choice == "Withdraw":
    st.header("Withdraw Money")
    accNo = st.text_input("Tell your account number")
    pin = st.number_input("Enter your 4 digit pin", step=1)
    amount = st.number_input("How much money you wanna withdraw", step=100)
    
    if st.button("Withdraw"):
        status, result = user.withdraw(accNo, int(pin), int(amount))
        if status == "Success":
            st.success(result)
        else:
            st.error(result)

if choice == "Show Details":
    st.header("Account Details")
    accNo = st.text_input("Tell your account number")
    pin = st.number_input("Enter your 4 digit pin", step=1)
    
    if st.button("Show"):
        status, result = user.showDetails(accNo, int(pin))
        if status == "Success":
            st.write("Your details are:")
            st.json(result)
        else:
            st.error(result)

if choice == "Update Details":
    st.header("Update Details")
    st.write("You cannot change your age and account number")
    
    accNo = st.text_input("Tell your account number")
    pin = st.number_input("Enter your current 4 digit pin", step=1)
    
    st.write("Fill details to change or leave empty")
    new_name = st.text_input("Please tell your name")
    new_email = st.text_input("Please tell your email")
    new_pin = st.text_input("Enter new pin (leave empty to keep same)")

    if st.button("Update"):
        status, result = user.updateDetails(accNo, int(pin), new_name, new_email, new_pin)
        if status == "Success":
            st.success(result)
        else:
            st.error(result)

if choice == "Delete Account":
    st.header("Delete Account")
    accNo = st.text_input("Tell your account number")
    pin = st.number_input("Enter your 4 digit pin", step=1)
    
    if st.button("Delete Permanent"):
        status, result = user.deleteUser(accNo, int(pin))
        if status == "Success":
            st.success(result)
        else:
            st.error(result)