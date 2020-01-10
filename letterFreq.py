punctuation="""' !@#$%^&*()1234567890,.?:;-[]_{}+=" """
my_file = input('enter the name of the file you qould like to check for word frequencies: ')
fObj=open(my_file, 'r')
my_string=fObj.read().replace('\n','')
d = {}
my_string=my_string.lower()
    
for ch in my_string:
    if ch.isalpha():
        d[ch] = d.get(ch, 0) + 1

print(d)
