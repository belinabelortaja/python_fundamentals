#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = {'x': 10, 'y': 20}

x[1][0]=15
print(x)
students[0]['last_name']="Bryant"
print(students)
sports_directory['soccer'][0]="Andres"
print(sports_directory)
z['y']=30
print(z)

#2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for dic in students:
    for val,cal in dic.items():
        print(f'{val} -- {cal}')
        print(f'{val}')

#3
a_key = "first_name"
values_of_a_key = [a_dict[a_key] for a_dict in students]
print(values_of_a_key)
b_key = "last_name"
values_of_b_key = [b_dict[b_key] for b_dict in students]
print(values_of_b_key)

#4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(dojo['locations'],dojo['instructors'])
