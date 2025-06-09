#listsm
bicycles = ["trek", "cannondale","redline" ]
print(bicycles)

cycles = ['trek', 'cannondale' , 'redline']
print(cycles[1])

cycles = ['trek', 'cannondale' , 'redline']
print(cycles[0].title())

names = ['Sark','Emma','James','Nicholas']
print(names[1])

motorcycles = ['Suzuki','Yahama','Honda']
print(motorcycles)

motorcycles[0] = 'ducti'
print(motorcycles)

motorcycles = ['Suzuki','Yahama','Honda']
print(motorcycles)

motorcycles.append('ducti')
print(motorcycles)

motorcycles = ['Suzuki','Yahama','Honda']

motorcycles.insert(0,'ducati')
print(motorcycles)

magicians = ['Alice','carloina','dsvid']
for magician in magicians:
  print(magician)

  cats = ('black','white','red')
  for cat in cats:
    print(cat)
#numerical lists
for value in range(1,9):
    print(value)   

numbers = list(range(1,11))
print(numbers)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

dimensions = (200, 50)
print(dimensions[1])

dimensions = (200, 50)
dimensions[0] = 250