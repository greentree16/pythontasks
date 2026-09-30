import random
from operator import truediv


class Membership:
    def __init__(self, name, password, age, member_id):
        self.name = name
        self.password = password
        self.age = age
        self.member_id = member_id

    def __str__(self):
        return f"'{self.name}'  '{self.password}'  '{self.age}'  '{self.member_id}'"

    def __repr__(self):
        return f"'{self.name}'  '{self.password}'  '{self.age}'  '{self.member_id}'"

    def doubleage(self):
        return self.age * 2


all_members = []
while True:
    membership_name = input("Please enter your name : ")
    membership_password = input("Please enter your password : ")
    membership_age = int(input("Please enter your age : "))
    member_id = membership_name + str(random.randint(1, 10000))
    member = Membership(membership_name, membership_password, membership_age, member_id)

    answer = input("Are there details correct? Y or N")
    answer = answer.lower()

    if answer == 'y':
        print("The members id is:", member.member_id)
        all_members.append(member)

    print("All members is:", all_members)


#if answer == 'Y':
 #   membership_name, membership_password = 1, 1
  #  membership_details.append(membership_name)
   # membership_details.append(membership_password)
