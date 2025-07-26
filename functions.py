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

def get_formatted_name(first_name,last_name):
     "Return a full name,formatted well"
     full_name = first_name + ' ' + last_name
     return full_name.title()
musician = get_formatted_name('john','cena')
print(musician)

def get_city_country(city,country):
     "Return a city with its country of location"
     location_name = city + ',' + country
     return location_name.title()
dancer = get_city_country("santiago","chile")
print(dancer)

def make_album(artist_name, album_name ,tracks=None):
    "Return a dictionary for album."
    person = {'artist': artist_name , 'album':album_name}
    if tracks:
         album_name['tracks'] = tracks
    return person
musician = make_album('juice wrld', 'life goes on')
print(musician)

#creating three albums
print(make_album("Forrest Frank", "UP"))
print(make_album("Moses Bliss","Darling Jesus"))