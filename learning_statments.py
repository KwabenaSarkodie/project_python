cars = ['audi', 'bmw', 'saburu','toyata']
for car in cars:
    if car == 'bmw':
      print(car.upper())
    else:
       print(car.title())

car = 'bmw'
car == 'bmw'

car = 'audi'
car == 'bmw'


requested_topping = 'mushrooms'

if requested_topping != 'anchovies': 
  print('Hold the anchovies')

answer = 17

if answer != 42 :
   print('This is not the correct answer.Please try again')

banned_users = ['linclon','eden','thorgan']
user ='marie'

if user not in banned_users:
   print(user.title() + ",you can enter your response as you wish")
age = 15
if age >= 18:
   print("You are old enough to vote")
   print("Have you registered yet?")
else :
   print("Sorry you are too young to vote")
   print("Please registered as soon as you turn 18")


age = 19
if age < 4:
  print("Your admission cost is $0")
elif age < 18 :
   print("Your admission cost is $5")
else :
   print("Your admission cost is $10")

age = 2
if age < 4:
  price = 0
elif age < 18 :
   price = 5
else :
   price = 10

print("Your admission cost is $" + str(price) + ".")

age = 50
if age < 4:
  price = 0
elif age < 18 :
   price = 5
elif age < 65 :
   price = 10
elif age >= 65 :
   price = 5

print("Your admission cost is $" + str(price) + ".")

requested_toppings = []
if requested_toppings :
   for requested_topping in requested_toppings : 
    print("Adding" + requested_topping + ".")
    print("\nFinished making your pizza")

else :
   print("Are you sure you want a plain pizza?")

