balance = 5000
correct_pin = "1123"
attempts = 3


print("Atm PIN System")
while attempts > 0:
  user_pin = input("Please enter your 4-digit PIN: ")

  if user_pin == correct_pin:
    print("PIN verified successfully! \n")
    break
  else:
    attempts -= 1
    print(f"Incorrect PIN. Attempts remaining: {attempts}")
  if attempts == 0:
    print("Too many incorrect attempts. Your card has been blocked for security.")
    exit()

def show_menu():
  print("Welcome to the ATM\n\n 1 to check for balance.\n 2 for deposit.\n 3 for withdrawal.\n 4 to exit. ")
  
def show_balance(balance):
  print(f"This is your balance {balance}.\n")

def user_deposit(balance):
  deposit = int(input("Enter how much to deposit: "))
  if deposit < 100 or deposit % 50 != 0:
    print("Invalid input. Minimum is 100 and in denomination of 50.")
  else:
    balance += deposit 
    print(f"Successfully deposited {deposit}. Your new balance is {balance}.")
  return balance

def withdraw(balance):
  withdrawal = int(input("Withdraw:"))
  if withdrawal < 100  or withdrawal % 50 != 0: 
    print(f"Withdrawal must be at least 100 pesos AND in a valid denomination of 50.")
  elif withdrawal > balance:
    print(f"Insufficient balance. Your current balance is {balance}")
  else: 
    balance -= withdrawal
    print(f"Successfully withdrawn {withdrawal}. Remaining balance is {balance}")
  return balance

def user_exit():
  print("Thank you for using the ATM.")

while True:
  
  show_menu()
  user_choice = input(f"Choose: ")
  
  if user_choice == "1":
    show_balance(balance)
  elif user_choice == "2":
    balance = user_deposit(balance)
  elif user_choice == "3":
    balance = withdraw(balance)
  elif user_choice == "4":
    user_exit()
    break
  else: 
    print("Invalid option. Try again.")