"""There are eight native datatype in Python
Boolean
Number
String
Bytes
Tuple
Sets
Dictionaries"""
print("For Boolean Datatype")
number= [1,2,3,4,5]
bool = 3 in number
print(bool)
print("For Numbers Datatype")
num1=5*3
num2=32//3
num3=32/3
print("num1 is",num1)
print("num2 is",num2)
print("num3 is",num3)
print("for String Data type")
str1="Welcome"
str2="to python programming"
str3=str1 + str2
print('The string is',str3)
print(str3[0:10])
print(str3[-5:])
print(str3[:-5])
print("for list data structure")
countries=['Australia','China','Japan','USA','Canada'] # List creation
states=['Montreal','Toronto','Newyork']
for st in states:  # iterating through list elements
    print(st)      # Print the list values
#print(countries)
countries.append('Russia')  # Updating the list with new country
countries.insert(2, 'Brazil') # Adding new country in list, with position
value=len(countries) # Getting the length of the list
print(value)  # printing the list values
countries.append(st)
countries.remove('Russia') # Deleting the elements in list
for count in countries:  # iterating the list value.
    print(count)
print("Tuple data structure")
sports_score = ('cricket',125, 'basketball', 15,'football', 5)
print(sports_score)
for ss in sports_score:
    print(ss)
print(type(sports_score))
sport_list = list(sports_score) # converting tuple to list
sport_list.append('Baseball') # updating list
for sl in sport_list:
    print(sl)
print(type(sport_list))
print("Dictionary")
student= {
    'Name':'David',
    'Student id': 541254,
    'Course':"Java",
    'Address':"Montreal"
}
print("Details of student are:",student)
print(student['Name'])
student['Name']='John'
print(student['Name'])





