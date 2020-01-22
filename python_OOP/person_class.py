class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greeting_count = 0
         self.people_greeted = []
         self.num_unique_greeted = 0
         
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
        if other_person not in self.people_greeted:
            self.people_greeted.append(other_person)
            self.num_unique_greeted += 1
        self.greeting_count += 1
        return ('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print('{}\'s email: {}, {}\'s phone number: {}'.format(self.name, self.email, self.name, self.phone))

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print(len(self.friends))

#1
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
#2
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#3
print(sonny.greet(jordan))
#4
print(jordan.greet(sonny))
#5a
print("{}'s email is {} and phone is {}".format(sonny.name, sonny.email, sonny.phone))
#5b
print("{}'s email is {} and phone is {}".format(jordan.name, jordan.email, jordan.phone))


#add method 2
sonny.print_contact_info()

#
#sonny.friends.append(jordan)
sonny.add_friend(jordan)
print("sonny friends " , sonny.friends[0])
print("sonny = ", sonny)
sonny.num_friends()
sonny.greet(jordan)
print("sonnys greeting count: ", sonny.greeting_count)
print("unique greetings: ", sonny.num_unique_greeted)

