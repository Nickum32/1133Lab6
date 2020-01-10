morse = {'A':'. _','B':'_ . . .','C':'_ . _ .','D':'_ . .','E':'.', \
'F':'. . _ .','G':'_ _ .','H':'. . . .','I':'. .','J':'. _ _ _' \
,'K':'_ . _','L':'. _ . .','M':'_ _','N':'_ .' ,'O':'_ _ _' \
,'P':'._ _.','Q':'_ _ . _','R':'. _ .','S':'. . .','T':'_','U':'. . _' \
,'V':'. . . _','W':'. _ _','X':'_ . . _','Y':'_ . _ _','Z':'_ _ . .'}
my_line=input('Enter the line you would like to convert to morse code.')
my_list=my_line.split('.')
for i in range(len(my_list)):
    sentence=my_list[i]   
    sentence=sentence.strip()
    for k in sentence:
        if k.upper() in morse:
            print(morse[k.upper()])
        else:
            print()
    print()
    print()
        
    
