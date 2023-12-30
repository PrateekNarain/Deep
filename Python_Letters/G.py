a=1
b=2
c=6
while a<19:
    if a==1:
        for i in range(3,0,-1):
            print(i*" "+(25+b)*"#")
            b=b+2
    elif a<=6:
        print((6*"#")+(21*" ")+(6*"#"))
    elif a<=11:
        print(6*"#")
    elif a<=14:
        print(6*"#"+14*" "+13*"#")
    elif a<=17:
        print(6*"#"+21*" "+6*"#")
    else:
         for i in range(1,4):
            print(i*" "+(37-c)*"#")
            c=c+2
    a=a+1
   
