"""
Project Name: Splitter

Creates a program that allows users to split expenses across
all members of a group by using Python objects and classes.

The project must accomplish the following requirements:

- At least 2 objects
- Each class must have at least 3 attributes
- Each class must have at least 3 methods
- Classes must be able to describe themselves
"""


class Group:
    def __init__(self, group_name, group_type, currency="USD"):
        self.group_name = group_name
        self.group_type = group_type
        if self.group_type < 1:
            self.group_type = "Other"
        elif self.group_type == 1:
            self.group_type = "Travel"
        elif self.group_type == 2:
            self.group_type = "Home"
        elif self.group_type == 3:
            self.group_type = "Friends"
        elif self.group_type >= 4:
            self.group_type = "Other"
        self.currency = currency
        self.members = []

    def __repr__(self):
        description = "Group name: {group_name}\nMembers length: {members}\nGroup usage: {group_type}".format(group_name=self.group_name, members=len(self.members), group_type=self.group_type)
        return description

    def add_members(self):
        """
        Add a member
        """


class Member:
    def __init__(self, name, age, status="Active"):
        self.name = name
        self.age = int(age)
        self.status = status

    def __repr__(self):
        description = "Name: {name}\nAge: {age}\nStatus: {status}".format(name=self.name, age=self.age, status=self.status)

    def inactivate_member(self):
        self.status = "Inactive"


class Expense:
    def __init__(self, name, expense_type, date, expense_amount):
        self.name = name
        self.expense_type = expense_type
        self.date = date
        self.expense_amount = round(float(expense_amount), 2)


print("\nWelcome to Splitter! The group expense manager.")
print("NOTE: The max amount of members in a group is 5")
print("--------------------------------------------------\n")

print("Let's start by creating your first group.")
print()

int_group_type = int(input("Choose a group usage:\n1 = Travel\n2 = Home\n3 = Friends\n4 = Other\n---> "))

print("\n--------------------------------------------------")

main_group_name = input("Please, give a short name to your group: ")
print()
initial_num_members = int(input("How many members will be added to this group initially?: "))
print("--------------------------------------------------")

# Create empty lists to store members data
members_names = []
members_ages = []

# For each member ask for their name and age
for i in range(initial_num_members):
    members_positions = ["1st", "2nd", "3rd", "4th", "5th"]
    members_names.append(input("What's the name of the {ith_member} member?: ".format(ith_member=members_positions[i])))
    print() # spacing for better reading
    members_ages.append(input("What's the age of the {ith_member} member?: ".format(ith_member=members_positions[i])))
    print() # spacing for better reading

for i in range(initial_num_members):
    members_dict = {}
    members_positions = ["1st", "2nd", "3rd", "4th", "5th"]



print("These are your group details: ")
main_group = Group(main_group_name, int_group_type)
print(main_group)
