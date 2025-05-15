import rpsgame

user_choice = input("Enter your choice,to stop playing enter quit: ").lower()

while user_choice != "quit":
  choices = rpsgame.get_choices()
  result = rpsgame.check_win(choices["player"], choices["computer"])
  print(result)
  print("\nTo stop playing enter quit")
  user_choice = input("Enter your choice: ").lower()
