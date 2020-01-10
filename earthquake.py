fObj = open('2.5_day.csv', 'r')
line = fObj.readline()
items = line.split(',')
for num in range(len(items)):
    print(str(num), items[num])

for line in fObj:
    info=line.split(',')
    print('magnitude: ', info[4])
    place = info[14]
    comma = place.find(',')
    print(place[comma+1:-1])
