
done= False
while not done:
    try:
        my_file = input('What file would you like to analyze?')
        fObj=open(my_file,'r')
        done =True
    except FileNotFoundError:
        print('ERROR: file not found.')  
d = {}
for line in fObj:
    pair = line.strip().split(',')
    d[int(pair[0])] = int(pair[1])
dSorted = sorted(d.values())
print(dSorted[0])
print(dSorted[-1])
