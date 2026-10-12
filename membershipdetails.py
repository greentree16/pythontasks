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

def add_member(am):
    membership_name = input("Please enter your name : ")
    membership_password = input("Please enter your password : ")
    membership_age = int(input("Please enter your age : "))
    member_id = membership_name + str(random.randint(1, 10000))
    member = Membership(membership_name, membership_password, membership_age, member_id)

    answer_add = input("Are there details correct? Y or N")
    answer_add = answer_add.lower()

    if answer_add == 'y':
        print("The members id is:", member.member_id)
        am[member.member_id] = member

# looks up a member in a membership map, the first parameter to the function should be the map of members
def lookup_member(am):
    member_id_answer = input("Enter the member's ID here:")
    found_member = am.get(member_id_answer)
    if found_member is None:
        print("Member not found.")
    else :
        print("Member found! The member is:", found_member)

def delete_member(am):
    sure = input("Are you sure you want to delete this member? Y or N")
    sure.lower()
    if sure == "y":
        member_id_answer = input("Enter the member's ID here:")
        del am[member_id_answer]
        print("The member id", member_id_answer, "was deleted.")

def main():
    all_members = {}

    while True:
        answer = input("Welcome to the rock climbing membership site. Would you like to add a member (a), look up a member (l), delete a member (d), or exit the site (e)?")

        if answer == "a":
            add_member(all_members)
        if answer == "p":
            for member in all_members:
                print(member)

        if answer == "l":
          lookup_member(all_members)

        if answer == "e":
            break

        if answer == "d":
            delete_member(all_members)


main()

#if answer == 'Y':
 #   membership_name, membership_password = 1, 1
  #  membership_details.append(membership_name)
   # membership_details.append(membership_password)
