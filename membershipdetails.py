import random


class Membership:
    def __init__(self, name, password, age, member_id):
        self.name = name
        self.password = password
        self.age = age
        self.member_id = member_id
        self.still_active_member = True

    def __str__(self):
        return f"'{self.name}'  '{self.password}'  '{self.age}'  '{self.member_id}'"

    def __repr__(self):
        return f"'{self.name}'  '{self.password}'  '{self.age}'  '{self.member_id}'"

    def end_membership(self):
        self.still_active_member = False
        # Send an email

all_members = {}

while True:
    answer = input("Welcome to the rock climbing membership site. Would you like to add a member (a), look up a member (l), delete a member (d), or exit the site (e)?")

    if answer == "a":

        membership_name = input("Please enter your name : ")
        membership_password = input("Please enter your password : ")
        membership_age = int(input("Please enter your age : "))
        member_id = membership_name + str(random.randint(1, 10000))
        member = Membership(membership_name, membership_password, membership_age, member_id)

        answer_add = input("Are there details correct? Y or N")
        answer_add = answer_add.lower()

        if answer_add == 'y':
            print("The members id is:", member.member_id)
            all_members[member.member_id] = member

    if answer == "l":
        member_id_answer = input("Enter the member's ID here:")
        found_member = all_members.get(member_id_answer)
        if found_member is None:
            print("Member not found.")
        else :
            print("Member found! The member is:", found_member)

    if answer == "e":
        break

    if answer == "d":
        sure = input("Are you sure you want to delete this member? Y or N")
        sure.lower()
        if sure == "y":
            member_id_answer = input("Enter the member's ID here:")
            del all_members[member_id_answer]
            print("The member id", member_id_answer, "was deleted.")




#if answer == 'Y':
 #   membership_name, membership_password = 1, 1
  #  membership_details.append(membership_name)
   # membership_details.append(membership_password)
