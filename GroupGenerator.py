import csv
import sys

class StudentDictionary(dict):  
    def __init__(self):  
        self = dict()  
    def add(self, key, value):  
        self[key] = value

student_dictionary = StudentDictionary()

group_names = [
    'Hacking', 'Artifical Intelligence (AI)', 'Encryption for Sale', 'Piracy and Open Source', 'Big Data & The Cloud', 'Social Media', 'Robotics & Cybernetics'
]

groups = { 
    'Hacking': [], 'Artifical Intelligence (AI)': [], 'Encryption for Sale': [], 'Piracy and Open Source': [], 'Big Data & The Cloud': [], 'Social Media': [], 'Robotics & Cybernetics': [] 
}

def generateGroups():
    if len(sys.argv) < 2:
        print("Syntax: python GroupMaker.py CSV_FILE")

    print("\nCS 301 Case Scenario Group Generator - Implemented by Francis Scott\n")
    with open(sys.argv[1], mode='r') as csv_file:
        data = [row for row in csv.reader(csv_file)] #reads csv into matrix form

        #populate groups
        for i in range(1, len(data)): #index 0 contains column names - start at 1 for student data
            student_choices = data[i]

            #populate a dictonary with student names as the key and their choices as the value. used for resolving small groups later on
            choices = []
            for x in range(2, len(student_choices)):
                choices.append(student_choices[x])
            student_dictionary.key = student_choices[1]
            student_dictionary.value = choices
            student_dictionary.add(student_dictionary.key, student_dictionary.value)

            #start with the student's first choice and try to add them to that group. otherwise, try their next choice
            for j in range(1, 8):
                choice = student_choices.index(str(j)) - 2 #shift index left by 2 because of timestamp and name entry
                group_name = group_names[choice]
                if len(groups[group_name]) < 3: #checks if group has less than 3 members
                    print("{} has been assigned to their number {} choice: {}".format(student_choices[1], j, group_name))
                    groups[group_name].append(student_choices[1]) #append students name to data
                    break #move on to next student

        #resolve groups that are too small
        small_groups = []
        found_small_group = False
        for k, v in groups.items():
            if len(v) == 1:
                continue
            if len(v) < 3: #check if there are groups with less than 3 members
                small_groups.append(k)
                found_small_group = True
                
        if found_small_group is True:
            print("\nResolving groups that have less than 3 members")
            for i in range(0, len(small_groups)): #iterate over each small group
                group_list = groups[small_groups[i]] #grab the list of student names from the small group
                index = group_names.index(small_groups[i]) + 1
                for j in range(0, len(group_list)): #iterate over each student in the small group
                    name = group_list[j] #grab name
                    choices = student_dictionary[name] #grab their choices
                    start_index = choices.index(str(index)) #here we are grabbing the ranking for the group they were put in so we can place them in the group of their next choice
                    for k in range(start_index+1, 8): #repeat process as above but starting with their next choice
                        choice = choices.index(str(k))
                        group_name = group_names[choice]
                        if len(groups[group_name]) == 3: #if we use '< 4' it may put the student in an unused group
                            groups[group_name].append(name) #append students name to new group
                            print("{} has been moved from {} to {}".format(name, small_groups[i], group_name))
                            break #move on to next student
                groups[small_groups[i]].clear() #clear out small group

def printGroups():
    print("\nFinal group assignments\n")
    group_number = 1
    for k, v in groups.items():
        if len(v) == 0:
            continue
        print("Group {}: {}".format(group_number, k))
        for i in range(0, len(v)):
            print(v[i])
        group_number += 1
        print()

generateGroups()
printGroups()
