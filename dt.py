import time
roomA = []
roomB = []
maxNumForRoomA = 5
counter = 1
flag = True
while flag:
    data = input('Register Student: ')
    if not (counter == maxNumForRoomA):
        print('Room A')
        roomA.append(data)
        print(roomA)

        if(counter >5):
            print('Room B')
            roomB.append(data)
            print(roomB)
    # else:
    #     flag = False
    # print(counter)
    counter = counter + 1
    time.sleep(2)