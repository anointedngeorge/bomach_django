"""
4. Write a python program to input marks of 
five subjects Physics, Chemistry, Biology, 
Mathematics and Computer. Calculate percentage 
and grade according to following:

Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
"""
import time

mark_container = []

maxi = 2
flag = True
grade = ''
while flag:

    if len(mark_container) <= maxi:
        subject = input('Subject: ')
        mark = int(input('Marks: '))
        
        if mark <= 39:
            grade = "F"
        elif (mark >= 40) and (mark <= 49):
            grade = "E"

        elif (mark >= 50) and (mark <=59):
            grade = "D"
        
        elif (mark >= 60) and (mark <= 69):
            grade = "C"
        
        elif (mark >= 70) and (mark <= 79):
            grade = "B"
        elif (mark >= 80):
            grade = "A"
            
        data = {
            'subject':subject.title(), 
            'percentage':mark, 
            'grade':grade.capitalize()
        }
        mark_container.append(data)

        # terminate the loop when the length of mark container
        # equals 5
        
    else: 
        flag = False
        print(mark_container)
    # print out mark container
    time.sleep(5)







# roomA = []
# roomB = []
# maxNumForRoomA = 5
# counter = 1
# flag = True
# while flag:
#     data = input('Register Student: ')
#     if not (counter == maxNumForRoomA):
#         print('Room A')
#         roomA.append(data)
#         print(roomA)

#         if(counter >5):
#             print('Room B')
#             roomB.append(data)
#             print(roomB)
#     # else:
#     #     flag = False
#     # print(counter)
#     counter = counter + 1
#     time.sleep(2)


