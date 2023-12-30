Ga=1
while a<22:
    if a==1:
        for i in range(3,0,-1):
            print(i*" "+(24-i)*"#")
    elif a==2 or a<=8:
        print(6*"#")
    elif a==9 or a<=11:
        print(14*"#")
    else:
        print(6*"#")
    a=a+1    
