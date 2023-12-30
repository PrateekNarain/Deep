a=1
while a<13:
    if a==1:
        for i in range(6,0,-2):
            print(i*" "+(24-i)*"#")
    elif a==2 or a<=11:
        print(6*"#")
    else:
        for i in range(1,7,2):
            print(i*" "+(24-i)*"#")
    a=a+1        
