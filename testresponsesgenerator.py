import random
import csv

#25 names
names = [
    "Joi Visconti","Mervin Jeans","Kaitlyn Mcquaid","Hiedi Dickerman","Christeen Canto",
    "Rowena Minnix","Karlyn Hatten","Hope Pierro","Jarred Hagins","Fabian Dugger",
    "Jeannette Freels","Orville Miers","Shirleen Brill","Bambi Shope","Stan Ryer",
    "Mistie Pineo","Whitley Lisby","Toshiko Cowan","Elvia Meyerhoff","Joey Smith",
    "Will Smith","James Bond","Maggie Pierce","John Doe","William Jones" 
]
student_count = 19 #used to generate x number of students
students = []
for i in range(0, student_count):
    students.append(names[i])

with open('test_feedback.csv', mode='w', newline ='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Timestamp', 'Name', 'Hacking', 'Artifical Intelligence (AI)', 'Encryption for Sale', 'Piracy and Open Source', 'Big Data & The Cloud', 'Social Media', 'Robotics & Cybernetics'])
    for i in range(0, len(students)):
        scores = [1, 2, 3, 4, 5, 6, 7]
        student_data = ["Time"] #placeholder for timestamp
        student_data.append(students[i])
        for j in range(0, len(scores)):
            index = random.randint(0, len(scores) - 1)
            student_data.append(scores.pop(index))
        writer.writerow(student_data)
