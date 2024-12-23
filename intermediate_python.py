
s1 = {1, 2, 3, 4, 5}
print(s1)


s1 = {1, 2, 3, 4, 5}
s1.add(9)
print(s1)



s1 = {1, 2, 3, 4, 5}
s1.update([6, 7, 8])
print(s1)




s1 = {1, 2, 3, 4, 5}
s2 ={6, 7, 8}
s1.update(s2)
print(s1)


s1 = {1, 2, 3, 4, 5}
s1.remove(5)
print(s1)




s1 = {1, 2, 3, 4, 5}
s1.discard(5)# it does not generate any error even the dicard number not in list
print(s1)



s1 = {1, 2, 3}
s2 ={2, 3, 4}
s3 = {3, 4, 5}
s4 = s1.intersection(s2)
print(s4)




s1 = {1, 2, 3}
s2 ={2, 3, 4}
s3 = {3, 4, 5}
s4 = s1.difference(s2)
print(s4)



s1 = {1, 2, 3}
s2 ={2, 3, 4}
s3 = {3, 4, 5}
s4 = s1.symmetric_difference(s2)
print(s4)



list1 =[1, 2, 3, 3, 2, 1]

list2 = list(set(list1))
print(list2)


employee =['jim', 'curter', 'tom', 'jane', 'hotty']
developer =['jim', 'curter', 'tom', 'april', 'hotty']

resul =set(employee).intersection(developer)
print(resul)




employee =['jim', 'curter', 'tom', 'jane', 'hotty']
developer =['jim', 'curter', 'tom', 'april', 'hotty']

resul =set(employee).difference(developer)
print(resul)


employee =['jim', 'curter', 'tom', 'jane', 'hotty']
developer =['jim', 'curter', 'tom', 'april', 'hotty']

resul =set(employee).symmetric_difference(developer)
print(resul)





employee =['jim', 'curter', 'tom', 'jane', 'hotty']
developers =['jim', 'curter', 'tom', 'april', 'hotty']
for developer in developers:
    print(developer)
    
    
    
    
#string
str = 'hello'
print(str.capitalize())
    
    
str = 'HellO'
print(str.casefold()) 

str = 'lullo'
print(str.center(40))




str = 'jim'
print(str.count('i'))

str = 'jim'
print(str.encode(encoding='UTF-8', errors='strict'))


str = 'lullo'
print(str.endswith(('o', 'e')))




str = 'jim\tjim\tjim'
print(str.expandtabs(20))

str = 'jim is a good boy'
print(str.find('a'))


str = 'jim is a {adjective} {gender} '
print(str.format(adjective='good', gender= 'boy'))



coordinate: dict = {'x': 10, 'y': -5}
text = 'coordinate: ({x}, {y})'
print(text.format_map(coordinate))


text ='astro nut is good'
print(text.index('good'))


str = 'HellO'
print(str.isalnum()) 

str = 'HellO23@'
print(str.isalpha())


str = 'HellO'
print(str.isascii())


#isdecimal[1, 2, 3]
# isdigit ,
# isnumeric


str = 'HellO'
print(str.isidentifier())


str = 'HellO\n'
print(str.isprintable())


str = 'Hello'
print(str.isspace())


str = '-'
print(str.join(['text00', 'text99', 'text90']))


str = 'text'
print(str.ljust(20, '-'))

str = 'text'
print(str.rjust(20, '-'))

str = ' Hello'
print(str.lstrip())


str = ' Hello '
print(str.rstrip())


str = ' Hello '
trable =str.maketrans('H', 'y')
print(trable)
print(str.translate(trable))


str = 'a + b =c'
print(str.partition('='))

str ='hshhshs'
print(str.removeprefix('hs'))  #removesuffix


str ='remember my comment'
print(str.replace('comment', 'subscribe'))

str ='remember my comment comment'
print(str.replace('comment', 'subscribe', 1))



str = 'a some texxt'
print(str.rfind('a'))


str ='to boy in the jung;ke'
print(str.rpartition('in'))



str ='to boy in the jungle'
print(str.rsplit(sep ='in'))



str ='to boy in the jungle'
print(str.split(maxsplit =5))


str ='to boy in the jungle'
print(str.rsplit(maxsplit =2))


str ='it is a good boy'
print(str.swapcase())


str = 'm'
print(str.zfill(200))



str ='it is a good boy'
print(str.startswith('i'))



gid = 'hello'
for i in gid:
    print(i)


gid = 'hello'
if 'h' in gid:
    print('ok')
else:
    print('no')    
    
    
    

gid = ['hello']   * 4
print(gid)   
    
my_string='eee'
for i in my_string:  #add the same number of word or letter
    my_string += i
    
print(my_string)      
    
    
  
var = 3
my_string ='the vallue of %d' %var  
print(my_string)
    
    
   
var = 3
var2 = 7
my_string ='the vallue of {:.2f} and {} '.format(var, var2)
print(my_string)   
    
    
      
var = 3
var2 = 7
my_string =f'the vallue of {var *2} and {var2} '
print(my_string) 
    
    
    
    
  
    
    
#mutable
#[list, dict, set]


#immutable
#[tuple,  int, float etc....]








import itertools


counter = itertools.count()
print(next(counter))
print(next(counter))



counter =itertools.count()
data = [100, 200, 300, 400]
daily_data = list(zip(itertools.count(), data))
print(daily_data)





counter =itertools.count()
data = [100, 200, 300, 400]
daily_data = list(itertools.zip_longest(range(11), data))
print(daily_data)




counter = itertools.count(start = 5, step=-3.4)
print(next(counter))
print(next(counter))




counter = itertools.cycle([2, 3, 4, 45])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))






counter = itertools.cycle(('on', 'off'))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))



counter = itertools.repeat(9)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))




counter = itertools.repeat(9, times=4)
print(next(counter))





counter = itertools.repeat(3, times=4)
squres =map (pow, range(20), itertools.repeat(3))
print(list(squres))






counter = itertools.repeat(2, times=4)
squres = itertools.starmap(pow, [(0,2), (1, 2), (2, 2)])
print(list(squres))



letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']
result = itertools.combinations(letters, 3 )

for item in result:
    print(item)




letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']
result = itertools.permutations(letters, 3 )

for item in result:
    print(item)






letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']
result = itertools.product(numbers, repeat=4 )

for item in result:
    print(item)






letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']
result = itertools.combinations_with_replacement(numbers, 4 )

for item in result:
    print(item)







letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']
result = itertools.chain(letters, numbers, names )

for item in result:
    print(item)






letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']
result = itertools.islice(range(10), 1, 3, 5)
for item in result:
    print(item)






letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']

sector = [True, True, False, True]
result =itertools.compress(letters, sector)
for item in result:
    print(item)








def lit_3(n):
    if n< 2:
        return True
    return False




letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']

sector = [True, True, False, True]
result = itertools.filterfalse(lit_3, numbers)
for item in result:
    print(item)








letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']

sector = [True, True, False, True]
result = itertools.dropwhile(lit_3, numbers)
for item in result:
    print(item)



letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']

sector = [True, True, False, True]
result = itertools.takewhile(lit_3, numbers)
for item in result:
    print(item)






letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']


result = itertools.accumulate( numbers)
for item in result:
    print(item)


import operator
letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicoles']


result = itertools.accumulate( numbers, operator.mul)
for item in result:
    print(item)



from itertools import groupby
def smaller_than_3(x):
    return x< 3
a =[1, 2, 3, 4]
group_object = groupby(a, key=smaller_than_3)
for key,  value in group_object:
    print(key, list(value))
    
    
    
   

persons = [{'name': 'tim', 'age': '23',}, {'name': 'timmy', 'age': '223',}, {'name': 'ontym', 'age': '22',}, {'name': 'woerd', 'age': '13',} ]
group_object = groupby(persons, key=lambda x : x['age'])
for key,  value in group_object:
    print(key, list(value))







#lambda

x = lambda a : a + 10
print(x(5))



x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))






def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
a =full_name('guido', 'van rossum')

print(a)









def cube(y):
    print(f"Finding cube of number:{y}")
    return y * y * y


lambda_cube = lambda num: num ** 3

# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))







my_list = [1, 2, 3, 4, 5]

# Use lambda to filter out even numbers from the list
new_list = list(filter(lambda x: x % 2 != 0, my_list))

# Print the new list
print(new_list)




a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)



greet = lambda name: "Hello " + name
print(greet("John")) 


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) 




numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)





def make_adder(x):
    return lambda y: x + y
add5 = make_adder(5)
print(add5(3)) 



numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers)


from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, numbers)
print(product)




numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)



employees = [{"name": "John", "age": 32},              {"name": "Jane", "age": 27},              {"name": "Jim", "age": 40}]
sorted_employees = sorted(employees, key=lambda x: x["age"])
print(sorted_employees)









employees = [{"name": "John", "salary": 50000}, {"name": "Jane", "salary": 55000}, {"name": "Jim", "salary": 60000}]
highest_salary_employee = max(employees, key=lambda x: x["salary"])
print(highest_salary_employee)






import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me!", command=lambda: print("Button clicked!"))
button.pack()
root.mainloop()




calculate = lambda x, y: x + y if x > y else x - y
print(calculate(5, 10))











#enumarete
x = ('apple', 'banana', 'cherry')
y = enumerate(x)





fruits = ['Apple', 'Orange', 'Strawberry']

for index, fruit in enumerate(fruits, start=1):
    print(f'{index}.{fruit}')
    
    
   
   
    
fruits = ['Apple', 'Orange', 'Strawberry']
e = enumerate(fruits, start=1)
print(type(e))
    
    
    
    
    
fruits = ['Apple', 'Orange', 'Strawberry']
e = enumerate(fruits, start=1)
print(e.__next__()  )
    
    
    
    
fruits = ['Apple', 'Orange', 'Strawberry']

e = enumerate(fruits, start=1)

print(e.__next__())
print(e.__next__())
print(e.__next__())   
    
    
    
    
    
    
def enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1   
    
    
    
    
    
    
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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
