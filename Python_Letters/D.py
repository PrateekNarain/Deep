a=1
while a<13:
    if a==1:
        for i in range(1,4):
            print(20*"#"+i*"#")
    elif a==2 or a<=11:
        print(3*" "+6*"#"+8*" "+6*"#")
    else:
        for i in range(3,0,-1):
            print(20*"#"+i*"#")
    a=a+1        
