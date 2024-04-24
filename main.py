if __name__ == "__main__":
  # The simple Python if statement

  age = int(input("Enter your age: "))
  if age >= 18:
    print("You're eligible to vote.")
    print("Let's go and vote.")

  # Python if ... else statement

  if age >= 18:
    print("You're eligible to vote.")
  else:
    print("You're not eligible to vote.")

  # Python if .. elif .. else statement

  if age < 5:
    ticket_price = 5
  elif age < 16:
    ticket_price = 10
  else:
    ticket_price = 18

  print(f"You'll pay {ticket_price} for the ticket")
