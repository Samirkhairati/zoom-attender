f = open('timings.txt')
r = f.readlines()
schedule = [[],[],[],[],[]]
schedule[0] = r[0:6]
schedule[1] = r[6:12]
schedule[2] = r[12:18]
schedule[3] = r[18:24]
schedule[4] = r[24:30]
for i in schedule:
    print(i)