def questions():
   answers = {}
   answers["name"] = input("What is your name?")
   answers["age"] = input("How old are you?")
   answers["colour"] = input("What is your favourite colour?")
   answers["python"] = input("Do you like python?")
   answers["flat"] = input("The world is flat: True or False?")
   return answers

def comments(answers):
   print("\nHello" + answers["name"])
   print("\nNice to meet you.")
   print("\nOh, your favourite colour is" + answers["colour"] + ".")
   if answers["python"].upper() == "YES":
      print("\nWOW.")
   else:
      print("\nFine.")
   if answers["flat"].upper() == "TRUE":
      print("\nThat make sense.")
   else:
      print("\nCorrect.")

ans = questions()
comments(ans)
