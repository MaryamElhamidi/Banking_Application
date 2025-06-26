# Banking Application – Object-Oriented Design

**Creator:** Maryam Elhamidi
**Date:** November 20, 2023

## 📌 Project Overview

This is a console-based banking system developed in Python using Object-Oriented Programming principles. It supports the creation and management of different types of accounts — specifically, Savings and Chequing accounts. Users can interact with their accounts by performing deposits, withdrawals, and balance inquiries.

## 🧱 Class Structure & Relationships

| Class             | Purpose                                                                    |
| ----------------- | -------------------------------------------------------------------------- |
| `Account`         | Base class for shared account attributes and methods                       |
| `SavingsAccount`  | Inherits from `Account`; enforces minimum balance during withdrawals       |
| `ChequingAccount` | Inherits from `Account`; allows overdrafts up to a defined limit           |
| `Bank`            | Manages all accounts, handles account creation and lookup                  |
| `Application`     | Main interface for user interaction, links menu options to account actions |

### UML (Text Description)

* `Bank` **has-a** list of `Account`
* `SavingsAccount` and `ChequingAccount` **is-a** `Account`
* `Application` **uses-a** `Bank`

## 🚀 Features

* Preloaded accounts for testing
* Open new savings or chequing accounts
* Deposit and withdraw money
* View account balance
* Account number validation and generation
* Error handling and input validation

## 🛠 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/MaryamElhamidi/A3_Repository.git
   cd A3_Repository
   ```
2. Ensure all required `.py` files (`Bank.py`, `Account.py`, etc.) are in the same directory.
3. Run the application:

   ```bash
   python Application.py
   ```

## ⚙️ Error Handling

* Invalid inputs are caught using `try/except` blocks.
* Invalid account types prompt re-entry.
* Runtime errors are handled gracefully with descriptive messages.

## ❗Limitations & Future Improvements

* Currently, users can’t fully customize account details during creation beyond balance and type.
* Limited input validation (e.g., text vs numeric for some fields).
* User interaction relies heavily on preloaded values.
* Future versions will include:

  * Fully user-driven account creation.
  * Editable account fields.
  * Persistent account data storage (file or database).

---
