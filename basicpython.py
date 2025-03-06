 # device power off
import os 

shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 

if shutdown == 'no': 
	exit() 
else: 
	os.system("shutdown /s /t 1") 
 

print("hello word")

print("sayak \nvedio")

a=1
b=0.9
c=9j
d="abc"
e=09e12

print("the type of a is:", type(a))
print("the type of a is:", type(b))
print("the type of a is:", type(c))
print("the type of a is:", type(d))
print("the type of a is:", type(d))

list1=[8, 8, 8, 9, 0, 9, 76]
print(list1)


tuple=(("parrot", "red"), ("dog", "bull"))
print(tuple)


dic={"sayak":"sakshi", 9:"red"}
print(dic)


print(3+4)
print(6-9)
print(7//9)
print(9*9)
print(90/3)



a=90
b=98
print("the value of", a,"+", b, "=", a+b)


sayak=23
number=90
sum=number + sayak
print("the sum is", sum)


name="sayak"
print(name[2])


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')  #adding list
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati')  # inserting list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
del motorcycles[0] #delete element
print(motorcycles)



motorcycles = ['honda', 'yamaha', 'suzuki']  #popped a element from the list
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print(f"The last motorcycle I owned was a {last_owned.title()}.")



motorcycles = ['honda', 'yamaha', 'suzuki']  #popping item from any element
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")



motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")



cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()                                       #organiz list alphabetically
print(cars)




cars = ['bmw', 'audi', 'toyota', 'subaru']     #revers alphabetical
cars.sort(reverse=True)
print(cars)



cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")                   #sort list without sort  fujnction
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)



cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()                                     #printing alist in reverse order
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])



magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(magician)



 magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(f"{magician.title()}, that was a great trick!")



magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(f"{magician.title()}, that was a great trick!") 
 print(f"I can't wait to see your next trick, {magician.title()}.\n")




magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")
 print("Thank you everyone, that was a great magic show!") 
 
 
 
 
 magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n") 
 
 
 
 magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n") 
 #for this the last line repeat every time
 print("Thank you everyone, that was a great magic show!")





for value in range(1, 5):
 print(value)


numbers = list(range(1, 6))
print(numbers)


even_numbers = list(range(2, 11, 2)) 
print(even_numbers)



squares = []
for value in range(1, 11):
  square = value + 2
  squares.append(square)   #We start with an empty list called squares u. At v, we tell Python to loop 
#through each value from 1 to 10 using the range() function. Inside the loop,
  print(squares)


#the current value is raised to the second power and assigned to the variable square w. At x, each new value of square is appended to the list squares. 
#Finally, when the loop has finished running, the list of squares is printed 

#>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#>>> min(digits)




squares = [value**2 for value in range(1, 11)]
print(squares)                                        # A list comprehension allows you to generate 
                                    #this same list in just one line of code. A list comprehension combines the 
                                  #for loop and the creation of new elements into one line, and automatically 
                                       #appends each new element.
                                       



players = ['charles', 'martina', 'michael', 'florence', 'eli'] #slicing a list
print(players[0:3])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])




players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")             #loopinng tthrough slice
for player in players[:3]:
 print(player.title())


#Copying a List

my_foods =['pizza', 'egg', 'fruit']
friends_food=my_foods[:]

print(my_foods)
print(friends_food)

#aappend inc opy

my_foods=['burger', 'pizza']
friends_food=my_foods[:]
my_foods.append('cannoli')
friends_food.append('ice cream')
print(my_foods)
print(friends_food)



#The ability to modify lists is particularly important 
#when you’re working with a list of users on a website or a list of characters in 
#a game. However, sometimes you’ll want to create a list of items that cannot 
#change. Tuples allow you to do just that.

#tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


#Looping Through All Values in a Tuple

diameters=(340, 50)
for diameter in diameters:
  print(diameter)





dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)
 
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)



#if Statements

cars =['audi', 'lamborgini', 'roll roys', 'bmw', 'mustang']
for car in cars:
  if car=='bmw':
    print(car.upper())
  else:
    print(car.title())



requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
 print("Hold the anchovies!")

#Checking Whether a Value Is Not in a Lis

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")




age=int(input("enter your age boyy"))
if age >=18:
  print('you are old enough for vote')
else:
  print('you cant vote')  



age=int(input('enter the age of the boy:'))
name=input("enter name")
if age <=4:
 print(name, "less than 4 years")
 print("Your admission cost is $0.")
elif age < 18:
 print(name, "less than 18 years")
 print("Your admission cost is $10.")
else:
   print(name, "is an adult")
  
   print("Your admission cost is $40.")



#more simplify
age=int(input("enter the age:"))
if age <4:
  price=0
elif age<18:
  
  price=89
else:
  price=120   

print(f' your addmission cost is ${price}.')



#Using Multiple elif Blocks


age = int(input("enter your age :"))
if age < 4:
 price = 0
elif age < 18:
 price = 25
elif age < 65:
 price = 40
else:
 price = 20
print(f"Your admission cost is ${price}.")



#Omitting the else Block
#Python does not require an else block at the end of an if-elif chain.

#with out else function
age = int(input("enter your age :"))
if age < 4:
 price = 0
elif age < 18:
 price = 25
elif age < 65:
 price = 40
elif age >= 65:
 price = 20
print(f"Your admission cost is ${price}.")



#for one test only 

##The if-elif-else chain is powerful, but it’s only appropriate to use when you 
#just need one test to pass. As soon as Python finds one test that passes, it 
#skips the rest of the tests. This behavior is beneficial,
requested_toppings=input('plese enter your favourite topppings.')

if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")
 
 
print("\nFinished making your pizza!")


#Using if Statements with Lists


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
 print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")





requested_topping =['mushrooms', 'green papper', 'extra cheese']
for requested_topping in requested_toppings:
  if requested_topping=='green pappers':
    print('soory, we are not out of green pappers right now')
  else :
   print(f'adding{requested_topping}.')





requested_toppings = []
if requested_toppings:
 for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")
 print("\nFinished making your pizza!")
else:
 print("Are you sure you want a plain pizza?")
 
 
 
 

#Using Multiple List

available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping in available_toppings:
  print(f"Adding {requested_topping}.")
 else:
  print(f"Sorry, we don't have {requested_topping}.")
 
print("\nFinished making your pizza!")




#dictionary

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])




alien_0={'color': 'green', 'point': '5'}
new_points=alien_0['point']
print(f'you just earned {new_points} points')




#Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)




alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)



#modifying dic
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")






alien_0={'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'the original position{alien_0['x_position']}')

if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] =='medium':
  x_increment =2
else:
  x_increment = 3
  
alien_0['x_position'] = alien_0['x_position'] + x_increment     

print(f'new position: {alien_0['x_position']}')



#delete item
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)




favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")







#Using get() to Access Values
#Using keys in square brackets to retrieve the value you’re interested in 
#from a dictionary might cause one potential problem: if the key you ask for 
#doesn’t exist, you’ll get an error



alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)



#Looping Through a Dictionary

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
 print(f"\nKey: {key}")
 print(f"Value: {value}")



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, language in favorite_languages.items():
 print(f"{name.title()}'s favorite language is {language.title()}.")



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in favorite_languages.keys():
 print(name.title())



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',} 
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 print('hi', name.title())
 
if name in friends:
 language = favorite_languages[name].title()
 print(f"\t{name.title()}, I see you love {language}!")





favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
if 'erin' not in favorite_languages.keys():
 print("Erin, please take our poll!")



#Looping Through a Dictionary’s Keys in a Particular Order
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
 print(f"{name.title()}, thank you for taking the poll.")




#Looping Through All Values in a Dictionary
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())



#A List of Dictionarie
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)






# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
aliens.append(new_alien)
 
# Show the first 5 aliens.
for alien in aliens[:5]:
 print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")









# Make an empty list for storing aliens.
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)
 
for alien in aliens[:3]:
 if alien['color'] == 'green':
  alien['color'] = 'yellow'
  alien['speed'] = 'medium'
  alien['points'] = 10
 
# Show the first 5 aliens.
for alien in aliens[:5]:
 print(alien)
print("...")
#Because we want to modify the first three aliens, we loop through a 
#slice that includes only the first three aliens. All of the aliens are green now 
#but that won’t always be the case, so we write an if statement to make sure
#we’re only modifying green aliens. If the alien is green, we change the color 
#to 'yellow', the speed to 'medium', and the point value to 10, as shown in the'''

for alien in aliens[0:3]:
 if alien['color'] == 'green':
  alien['color'] = 'yellow'
  alien['speed'] = 'medium'
  alien['points'] = 10
 elif alien['color'] == 'yellow':
  alien['color'] = 'red'
  alien['speed'] = 'fast'
  alien['points'] = 1








# Make an empty list for storing aliens.
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)
 
for alien in aliens[:3]:
 if alien['color'] == 'green':
  alien['color'] = 'yellow'
  alien['speed'] = 'medium'
  alien['points'] = 10
 
# Show the first 5 aliens.
for alien in aliens[:5]:
 print(alien)
print("...")

for alien in aliens[0:3]:
 if alien['color'] == 'green':
  alien['color'] = 'yellow'
  alien['speed'] = 'medium'
  alien['points'] = 10
 elif alien['color'] == 'yellow':
  alien['color'] = 'red'
  alien['speed'] = 'fast'
  alien['points'] = 15






#list in a dictionary
# Summarize the order.
 #Store information about a pizza being ordered.
pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }
print(f"You ordered a {pizza['crust']}-crust pizza "
 "with the following toppings:")
for topping in pizza['toppings']:
 print("\t" + topping)





favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
 print(f"\n{name.title()}'s favorite languages are:")
for language in languages:
 print(f"\t{language.title()}")
 
 
 
 
 
 
 
 users = {
 'aeinstein': {
 'first': 'albert',

 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
for username, user_info in users.items():
 print(f"\nUsername: {username}")
full_name = f"{user_info['first']} {user_info['last']}"
location = user_info['location']
print(f"\tFull name: {full_name.title()}")
print(f"\tLocation: {location.title()}")





#python user input and while loops

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")



height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
 print("\nYou're tall enough to ride!")
else:
 print("\nYou'll be able to ride when you're a little older.")




number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
 print(f"\nThe number {number} is odd.")



num=int(input('enter a numer:'))
if num%10==0:
  print('this is a multiple of 10')
else:
  print('not multiple of 10')  
   



#The while Loop in Action
#You can use a while loop to count up through a series of numbers. For 
#example, the following while loop counts from 1 to 5:

current_number=1
while current_number<=5:
  print(current_number)
current_number+=1  
  




#Letting the User Choose When to Qui

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
 message = input(prompt)
 print(message)




prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
 message = input(prompt)
 
 if message != 'quit':
  print(message)




prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
  message = input(prompt)
 
  if message == 'quit':
   active = False
  
else:
 print(message)





prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
 city = input(prompt)
 
 if city == 'quit':
   break
 else:
    print(f"I'd love to go to {city.title()}!")





current_number = 0
while current_number < 10:
 current_number += 1
 if current_number % 2 == 0:
  continue
 
 print(current_number)




#infinite loop
x = 1
while x <= 5:
 print(x)


#avoide infinite loop
x = 1
while x <= 5:
 print(x)
 x += 1


#Using a while Loop with Lists and Dictionaries
# Start with users that need to be verified, 
 # and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
 current_user = unconfirmed_users.pop()
 
 print(f"Verifying user: {current_user.title()}")
 confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
 print(confirmed_user.title())





#Removing All Instances of Specific Values from a Lis

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')
 
print(pets)







#Filling a Dictionary with User Inpu
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
 # Prompt for the person's name and response.
 name = input("\nWhat is your name? ")
 response = input("Which mountain would you like to climb someday? ")
 
 # Store the response in the dictionary.
 responses[name] = response
 
 # Find out if anyone else is going to take the poll.
 repeat = input("Would you like to let another person respond? (yes/ no) ")
 if repeat == 'no':
  polling_active = False
 
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
 print(f"{name} would like to climb {response}.")








#def functions 
# a  block of reusable code

def greet_user():
  #"""display a simple greeting"""
  print("hello")


greet_user()

#Any indented lines that follow def greet_user(): make up the body of 
#the function. The text at v is a comment called a docstring, which describes 
#what the function does.



def greet_user(name):
  print(f'glory to lord, {name.title()}!')
  
greet_user('rama')  
greet_user('Hanuman')
  
  


#Positional Arguments

def describe_pet(animal_type, pet_name):
 #"""Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet('hamster', 'harry')








#multiple functions calls

def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')






def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet('harry', 'hamster')







#Keyword Arguments
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet(animal_type='hamster', pet_name='harry')






def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet(animal_type='hamster', pet_name='harry')






#Default Value
def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')





#Equivalent Function Calls
#Avoiding Argument Errors

def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()





def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)





#Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {middle_name} {last_name}"
 return full_name.title()
 
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)






def get_formatted_name(first_name, last_name, middle_name=''):
 """Return a full name, neatly formatted."""
 if middle_name:
   full_name = f"{first_name} {middle_name} {last_name}"
 else:
  full_name = f"{first_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)





#Returning a Dictionary

def build_person(first_name, last_name):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
 return person
musician = build_person('jimi', 'hendrix')
print(musician)





#We add a new optional parameter age to the function definition and 
#assign the parameter the special value None, which is used when a variable 
#has no specific value assigned to it. You can think of None as a placeholder 
#value. In conditional tests, None evaluates to False. If the function call 
#includes a value for age, that value is stored in the dictionary
def build_person(first_name, last_name, age=None):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
 if age:
  person['age'] = age
 return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)








#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()
# This is an infinite loop!
while True:
 print("\nPlease tell me your name:")
 f_name = input("First name: ")
 l_name = input("Last name: ")
 
 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!")








def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()

while True:
 print("\nPlease tell me your name:")
 print("(enter 'q' at any time to quit)")
 
 f_name = input("First name: ")
 if f_name == 'q':
   break

 l_name = input("Last name: ")
 if l_name == 'q':
   break
 
 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!")




l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))






l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)





fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)

next_element = next(enum_fruits)
print(f"Next Element: {next_element}")




next_element = next(enum_fruits)
print(f"Next Element: {next_element}")

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40

class Person:
  pass



#inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
  pass


x = Student("Mike", "Olsen")
x.printname()





Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)



class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)



class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019





class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)



Add a method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)






#Python Iterators

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))




mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)



mystr = "banana"

for x in mystr:
  print(x)



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))




class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)



mytuple = ("apple", "banana", "cherry")
print(len(mytuple))





thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))









class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()













class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()






def myfunc():
  x = 300
  print(x)

myfunc()




def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()






x = 300

def myfunc():
  print(x)

myfunc()

print(x)









x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)







def myfunc():
  global x
  x = 300

myfunc()

print(x)





x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)









def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())





def greeting(name):
  print("Hello, " + name)







import mymodule

mymodule.greeting("Jonathan")








person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}








import mymodule
a = mymodule.person1["age"]
print(a)






import mymodule as mx
a = mx.person1["age"]
print(a)








import platform
x = platform.system()
print(x)







import platform
x = dir(platform)
print(x)







def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}





from mymodule import person1

print (person1["age"])








import datetime

x = datetime.datetime.now()
print(x)







import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))





import datetime

x = datetime.datetime(2020, 5, 17)

print(x)






import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))




































































