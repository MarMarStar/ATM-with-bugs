def show_menu():
  print("Welcome to the ATM\n\n 1 to check for balance.\n 2 for deposit.\n 3 for withdrawal.\n 4 to exit. ")
  
def show_balance(balance):
  print(f"This is your balance {balance}.\n")

def user_deposit(balance):
  while True:
    deposit = input("Deposit:").strip()
    if not deposit.isdigit():
      print("Invalid input. Please enter a numeric value.")
      continue
    deposit = int(deposit)
    if deposit < 100 or deposit % 50 != 0:
      print(f"Deposit must be at least 100 pesos AND in a valid denomination of 50.")
    else:
      balance += deposit
      print(f"Successfully deposited {deposit}. New balance is {balance}")
    return balance

def withdraw(balance):
  while True:
    withdrawal = input("Withdraw:").strip()
    if not withdrawal.isdigit():
      print("Invalid input. Please enter a numeric value.")
      continue
    withdrawal = int(withdrawal)
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

def verify_pin(correct_pin):
  print("Atm PIN System")
  attempts = 3

  while attempts > 0:
    user_pin = input("Please enter your 4-digit PIN: ").strip()

    if not user_pin:
      print("PIN cannot be empty. Please try again.")
      continue

    if len(user_pin) != 4 or not user_pin.isdigit():
      print("Invalid PIN format. Please enter a 4-digit numeric PIN.")
      continue

    if user_pin == correct_pin:
      print("PIN verified successfully! \n")
      return True
    else:
      attempts -= 1
      print(f"Incorrect PIN. Attempts remaining: {attempts}")
    
  print("Too many incorrect attempts. Your card has been blocked for security.")
  return False

def run_atm():
  balance = 5000
  correct_pin = "1123"

  if not verify_pin(correct_pin):
    return False
  
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
      return False
    else: 
      print("Invalid option. Try again.")
      continue
    
    while True:
      next_action = input("Please input 1 for another transaction\nor\n2 to exit the program and print receipt:  ").strip()
      if next_action == "2":
        user_exit()
        print("Exiting program and printing receipt...")
        return False
      elif next_action == "1":
        break
      else:
        print("Invalid input. Please type '1' or '2'.")

if __name__ == "__main__":
 run_atm()
