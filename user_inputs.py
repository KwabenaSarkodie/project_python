name = input("Please enter your name :")
print("Hello, " + name +"." + "\nSark has a message for you." + "\nI am so lucky to have you as my woman.")

prompt = ("If you tell is who you are,we can personalize the message you see")
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello, " + name + "!")


height = input("How tall are you, in inches?")
height = int(height)

if height >= 36 :
   print("\nYou are tall enough to ride")
else :
   print("\nYou are too short ma flend!")


number = input("Enter a number and I will tell you if its even or odd?")
number = int(number)

if number % 2 ==0:
   print("The number," + str(number) + ", is even")
else :
   print("The number," + str(number) + ", is odd")


current_number = 0
while current_number <= 5 :
   print(current_number)
   current_number += 1



key = "\nTell me something,and I will repeat it to you:"
key += "\nEnter quit to end program." 
message = " "
while message != 'quit':
   message = input(key)

if message != 'quit':
   print(message)


key = "\nTell me something,and I will repeat it to you:"
key += "\nEnter quit to end program." 
active = True
while active:
   message = input(key)
   
if message == 'quit':
   active = False
else : 
   print(message)


