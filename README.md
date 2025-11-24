# GDBL Banking System

A Python-based banking management application that allows users to create accounts, manage transactions, and view personal details through a graphical interface.

## Project Overview

This system separates the application logic from the user interface. It uses **Streamlit** for the frontend to provide an interactive web-based dashboard, while the backend handles data processing and storage using a local JSON database.

## Features

- **Account Creation:** Generate unique account numbers (GDBL prefix) and secure accounts with a 4-digit PIN.
- **Transactions:** Deposit and withdraw funds with balance validation.
- **Account Management:** View account details and check current balance.
- **Profile Updates:** specific user details (Name, Email, PIN) can be updated.
- **Delete Account:** Permanently remove user data from the system.
- **Data Persistence:** All user data is saved automatically to `data.json`, ensuring data is not lost when the program closes.

## Prerequisites

- Python 3.x
- Streamlit

## Installation

1.  Download or clone the repository to your local machine.
2.  Open your terminal or command prompt in the project directory.
3.  Install the required library:

    ```bash
    pip install streamlit
    ```

## Usage

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```
