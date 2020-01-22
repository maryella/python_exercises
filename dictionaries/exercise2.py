# Exercise 2: Nested Dictionaries
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}
# 2.1 - get email
email = ramit['email']
print("Ramit's email: " + email)
# 2.2 - get first interest
first_interest = ramit['interests'][0]
print("Ramit's first interest: " + first_interest)
# 2.3 - get Jasmine email address
jasmine_email = ramit['friends'][0]['email']
print("Jasmine's email:" + jasmine_email)
# 2.4 - get Jan's second interest
jan_interest2 = ramit['friends'][1]['interests'][1]
print("Jan's 2nd interest: " + jan_interest2)
