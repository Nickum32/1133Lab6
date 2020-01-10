my_file=input('Enter the name of thwe file you would like to write in: ')
fObj=open(my_file, 'w+')
import random
for i in range(1, 1001):
    fObj.write(str(i)+ ',' + str(random.randint(-1000, 1000)) + '\n')
    i+=1
fObj.close()    
