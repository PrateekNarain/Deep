def a():
    a=36
    b=1
    print(38*" "+"#")
    for i in range(1,10):
        print(a*" "+b*"#"+2*i*" "+i*"#")
        a=a-2
        b=b+1
    x=40
    for i in range(9,5,-1):
        print(2*i*" "+x*"#")
        x=x+4
    q=10
    w=14
    for i in range(14,20):
        print(q*" "+w*"#"+2*i*" "+i*"#")
        q=q-2
        w=w+1
a()
