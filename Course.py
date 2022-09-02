
#S E C T I O N 3 - DATA TYPES
#Math operations with lists

student_grades = [10, 6.5, 7]
print (student_grades * 2)
print (student_grades + student_grades)


#autogenerate lists
#range datatype to list conversion
listranges = list(range(0,11))
listranges2 = list(range(0,11,2) )#thrird argument is "step")
print (listranges)
print (listranges2)

#Other stuff
print("PATTY is a great person".title())  #title changes every word
print("PATTY is a BAD person".capitalize()) #capitalize only 1st letter of the sentence

#Checking methods dir(datatype) - list, str, float, int etc....
#For functions dir(__builtins__)
my_sum = sum (student_grades)
size = len(student_grades)
average = my_sum/size
print (average)
print ('--------------------------------')


##-----------------------------------------
##-----------------------------------------
#S E C T I O N  #4 - OPERATIONS WITH DATA TYPES
#methods are the operations

#print ('todai'.replace('i','y'))
monday_temperatures = [25, 27, 30, 32]
monday_temperatures.append(26)
print (monday_temperatures)

#getting the index of an specific value on the list
print (monday_temperatures.index(26))
#getting the value for an specific index on the list
print (monday_temperatures[2])


#exercises - removing and appending itens
seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)

seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)

#accessing portion of lists
monday_temperatures [0:5]
monday_temperatures [:5] #from the beggining
monday_temperatures [3:] #all the way to the end after index 3
monday_temperatures [-1] #we can use negatie indexes for running backwards
monday_temperatures [-3:]

#the same thing applies to strings
mystring = 'hello'
mylist = ['hello','world']

mystring[2]
mylist[0][2] #object of index 2 of the object index zero of mylist


#Dictionaries
student_gradesdic = {'Mary':10,'Sim':6.5,'Paula':7}

eng_port = {'sun':'sol','moon':'lua','sky':'céu'}
eng_port ['sun']

dictionaire2 = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}
data_01 = dictionaire2
data_01 ['b'][2] #6

#----------------------------
#----------------------------
#----------------------------
#----------------------------
# S E C T I O N 5 - FUNCTIONS AND CONDITIONALS

#creating functions
#it's important to note the functions need to have a "return" statement
def average (minhalista):
    return sum(minhalista) / len(minhalista)
    
def square (a):
    area = a * a
    return area

def oc_to_mm (size):
    mm = size * 29.57353
    return mm

def average2 (value): #this can be used to any data type list/dict/tuple
    if type(value) == dict:
   #if isinstance (value, dict) would be a better approach
        mean = sum(value.values()) / len (value)
    else:
        mean = sum(value)/ len(value)

    return mean

print (average2(student_grades))
print (average2(student_gradesdic))

#CONDITIONALS
#warm or cold exercise
def iscold (temperature):
    if temperature > 7:
        switch = "warm"
    else:
        switch = "cold"
        
    return switch

print (iscold(5),iscold(7),iscold(10))

def string (string):
    if len (string) < 8:
        return False
    else:
        return True
        
print (string('Potato'),string('Alligator'))

#Elif conditionals - multiple conditionals
x = 3
y = 2

if x > y:  #it's important to have spaces between operators to make your document more readable.
    print (f'{x} is greater than {y}')
elif x == y:
    print (f'{x} is equal to {y}')
else:
    print (f'{x} is less than {y}')

#funcions using elif.
def termometer (temperature):
    if temperature > 25:
        return 'Hot'
    elif temperature >= 15:
        return 'Warm'
    else:
        return 'Cold'
        
print (termometer(10),termometer(15), termometer(20), termometer(26))

##--------------------------------------------------------------------
##--------------------------------------------------------------------
##--------------------------------------------------------------------
##S E C T I O N  6 - PROCESSING USER INPUT

temperature = float(input ('Insert actual temperature: '))
print(f'The weather today is {termometer(temperature)}')

#STRING FORMATTING
name = input ('Enter your name: ')
surname = input ('Enter your surname: ')
message = 'Hello %s %s' % (name ,surname) #python 2 and python 3 - use one %s for each variable u need to convert
message2 = f'Hello {name} {surname}' #python 3.6 and above
message3 = 'Your name is {}. Your surname is {}'.format(name,surname)
print (message)
print (message2)
print (message3)

def hi_person (name):
    return  'Hi {}'.format(name.capitalize())
            #'Hi {name.capitalize()}' - could use title as well.
hi_person ('patty')
