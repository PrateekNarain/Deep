a=1
while a<20:
    if a==1:
        for i in range(3,0,-1):
            print(i*" "+(24-i)*"#")
    elif a==2 or a<=8:
        print(6*"#")
    elif a==9 or a<=11:
        print(14*"#")
    elif a==12 or a<=18:
        print(6*"#")
    else:
        for i in range(1,4):
            print(i*" "+(24-i)*"#")
    a=a+1    
