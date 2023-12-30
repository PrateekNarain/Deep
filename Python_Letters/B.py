a=1
while a<22:
    if a==1:
        for i in range(1,6,2):
            print(17*"#"+i*"#")
    elif a==2:
        for i in range(1,4):
            print((3*" ")+(6*"#")+(7*" ")+i*" "+(6*"#"))
    elif a==3 or a<=8:
        print(3*" "+6*"#"+11*" "+6*"#")
    elif a==9 :
        for i in range(3,0,-1):
            print(3*" "+6*"#"+8*" "+i*" "+6*"#")
    elif a==10 or a<=12:
        print(3*" "+19*"#")
    elif a==13:
        for i in range(1,4):
            print((3*" ")+(6*"#")+(7*" ")+i*" "+(6*"#"))
    elif a==14 or a<=19:
        print(3*" "+6*"#"+11*" "+6*"#")
    elif a==20:
        for i in range(3,0,-1):
            print(3*" "+6*"#"+8*" "+i*" "+6*"#")
    else:
        for i in range(6,1,-2):
            print(17*"#"+i*"#")
    a=a+1    
