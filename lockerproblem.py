lockers = []
foo = 0
while foo < 500:
    lockers.append('0')
    foo += 1
lock = 2
counter = 1
input('Hit ENTER to start, hit Ctrl+C to stop the program. 5')
while True:
    try:
        while counter < len(lockers):
            lockers[counter] = str(int(not int(lockers[counter])))
            counter += lock
        print('\n\n'+str(lock)+':')
        for i in range(0, len(lockers)):
            print(lockers[i], end=' ')
        counter = 0
        lock += 1
    except KeyboardInterrupt:
        break
