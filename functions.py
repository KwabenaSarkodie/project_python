def greet_user():
      """Display a simple greeting."""
      print("Hello!")

greet_user()

def greet_user(username):
      """Display a simple greeting."""
      print("Hello," + username.title() + "!")

greet_user('jesse')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog','bingo')
 
