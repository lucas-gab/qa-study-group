#Dictionary 

my_list = ['Eduardo','Paula','Leticia']

coding_study_group = {
    'participants': my_list,
    'ages': [30, 31, 29]
     }

print(coding_study_group['participants'][0])
print(coding_study_group.get('participants')) #this one skips the line instead of giving error "None"

coding_study_group2 = {
    'participants': {
        'names' : ['Eduardo','Paula','Leticia'] ,
        'ages': [30, 31, 29]
    }
    
}
print(coding_study_group2['participants']['names'][1])
print(coding_study_group2.get('participants').get('names')[1]) #this one skips the line instead of giving error "None"


#Tuple
#immutable, usually used for important variables that can not be changed.

#Fuctions
#Good practice: Isolated functions for isolated actions, it's easier to mantain.
#Try to keep it simple around 6 lines tops.

my_age = 20

if my_age >= 21:
    print ("Please, come in!")
elif my_age > 18:
    print ("If you bring your Parents, come in!")
else:
    print ("Go home, you are too young kiddo!")

    