# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 23:42:49 2017

@author: dell
"""
print('                          TIME TABLE                          ')
print('monday    1st         2nd       break     3rd        4th')
print('class1    b1(maths)   b3(phy)             b3(cs)     b2(maths)')
print('class2    b2(phy)     b2(chem)            b1(chem)   b1(cs)')
print('')
print('')
print('tuesday    1st         2nd      break     3rd         4th')
print('class1     b1(maths)   b1(phy)            b2(maths)   b1(cs)')
print('class2     b2(cs)      b3(chem)           b3(phy)     b3(math)')
print('')
print('')
print('wednesday  1st         2nd      break     3rd         4th')
print('class1     b2(maths)   b2(cs)             b2(chem)    b1(lab)')
print('class2     b3(cs)      b1(chem)           b3(maths)   b3(chem)')
print('')
print('')
print('thursday    1st        2nd      break    3rd          4th')
print('class1      b1(maths)  b2(cs)             b2(chem)    b3(chem)')
print('class2      b3(cs)     b3(maths)          b1(cs)      b1(chem)')
print('')
print('')
print('friday    1st          2nd      break    3rd          4th')
print('class1    b1(phy)      b2(phy)            b2(cs)      b2(maths)')
print('class2    b3(chem)     b3(maths)          b1(maths)   b3(cs)')
print('')

t100=0
q=0
r=0
s=0
p='present'
while 1:
    td=raw_input('which day ')
    o=raw_input('are you a teacher ')
    if o=='yes':
        print("welcome to attendance portal")
        print("please write present against your name for other names press enter")
        a=raw_input("Mr. Ravi ")
                     
        b=raw_input("Mr. Ram ")
                    
        c=raw_input("Mr. Shyam ")
                      
        d=raw_input("Miss Meena ")
                     
        if a=='present':
             print('Mr. Ravi(maths faculty) is present')
             t100=t100+1              
        if b=='present':
             print('Mr. Ram(chemistry faculty) is present')
             q=q+1
             
        if c=='present':
             print('Mr. shyam(physics faculty) is present')
             r=r+1  
        if d=='present':
            print('Miss Meena(computer science) is present')
            s=s+1  
    else:
        break
    m=raw_input('are you manager ')
    if m=='yes':
        if a=='present' and b=='present' and c=='present' and d=='present':
            print('follow the above given schedule')
        else:                    
            if td=='monday':
                if a!=p and b==p and c==p and d==p:
                   print('In class-1:batch-1 first period is free')
                   print('in class-1:batch-2 fourth period is free')
                   t=raw_input("which subject you want to allot ")
                   v=raw_input("which subject you want to allot ")
                   print('In class 1 following schedule takes place whereas for class 2 it is same')
                   f="b1("+t+")  b3(phy)  break  b3(cse) b2("+v+")"
                   print(f)
                if a==p and b!=p and c==p and d==p:
                    print('In class-2:batch-2 second period is free')
                    print('In class-2:batch-1 third period is free')
                    t1=raw_input("which subject you want to allot ")
                    v1=raw_input("which subject you want to allot ")
                    print('In class 2 following schedule takes place whereas for class 1 it is same')
                    f1="b2(phy)  b2("+t1+")  break  b1("+v1+") b1(cse)"
                    print(f1)
                if a==p and b==p and c!=p and d==p:
                    print('In class-1:batch-3 second period is free')
                    print('In class-2:batch-2 first period is free')
                    t2=raw_input("which subject you want to allot ")
                    v2=raw_input("which subject you want to allot ")
                    f2="class1  b1(maths)  b3("+t2+")  break  b3(cse) b2(maths)"
                    f3="class2  b2("+v2+")  b2(chem)  break  b1(chem) b1(cse)"
                    print(f2)
                    print(f3)
                if a==p and b==p and c==p and d!=p:
                    print('In class-1:batch-3 third period is free')
                    print('In class-2:batch-1 fourth period is free')
                    t3=raw_input("which subject you want to allot ")
                    v3=raw_input("which subject you want to allot ")
                    f4="class1  b1(maths)  b3(phy)  break  b3("+t3+") b2(maths)"
                    f5="class2  b2(phy) b2(chem)    break  b1(chem) b1("+v3+")"
                    print(f4)
                    print(f5)
                if a!=p and b!=p and c==p and d==p:
                    print('In class-1:batch-1 first period is free')
                    print('in class-1:batch-2 fourth period is free')
                    print('In class-2:batch-2 second period is free')
                    print('In class-2:batch-1 third period is free')
                    e=raw_input("which subject you want to allot ")
                    g=raw_input("which subject you want to allot ")
                    h=raw_input("which subject you want to allot ")
                    i=raw_input("which subject you want to allot ")
                    l1="class1  b1("+e+")  b3(phy)  break  b3(cse) b2("+g+")"
                    l2="class2  b2(phy) b2("+h+")    break  b1("+i+") b1(cse)"
                    print(l1)
                    print(l2)
                if a!=p and b==p and c!=p and d==p:
                    print('In class-1:batch-1 first period is free')
                    print('in class-1:batch-2 fourth period is free')
                    print('In class-1:batch-3 second period is free')
                    print('In class-2:batch-2 first period is free')
                    e1=raw_input("which subject you want to allot ")
                    g1=raw_input("which subject you want to allot ")
                    h1=raw_input("which subject you want to allot ")
                    i1=raw_input("which subject you want to allot ")
                    l3="class1  b1("+e1+")  b3("+g1+")  break  b3(cse) b2("+h1+")"
                    l4="class2  b2("+i1+") b2(chem)    break  b1("+i+") b1(cse)"
                    print(l3)
                    print(l4)
                if a!=p and b==p and c==p and d!=p:
                    print('In class-1:batch-1 first period is free')
                    print('in class-1:batch-2 fourth period is free')
                    print('In class-1:batch-3 third period is free')
                    print('In class-2:batch-1 fourth period is free')
                    e2=raw_input("which subject you want to allot ")
                    g2=raw_input("which subject you want to allot ")
                    h2=raw_input("which subject you want to allot ")
                    i2=raw_input("which subject you want to allot ")
                    l5="class1  b1("+e2+")  b3(phy)  break  b3("+g2+") b2("+h2+")"
                    l6="class2  b2(phy) b2(chem)    break  b1(chem) b1("+i2+")"
                    print(l5)
                    print(l6)
                if a==p and b!=p and c!=p and d==p:
                    print('In class-1:batch-3 second period is free')
                    print('In class-2:batch-2 first period is free')
                    print('In class-2:batch-2 second period is free')
                    print('In class-2:batch-1 third period is free')
                    e3=raw_input("which subject you want to allot ")
                    g3=raw_input("which subject you want to allot ")
                    h3=raw_input("which subject you want to allot ")
                    i3=raw_input("which subject you want to allot ")
                    l7="class1  b1(maths)  b3("+e3+")  break  b3(cse) b2(maths)"
                    l8="class2  b2("+g3+") b2("+h3+")    break  b1("+i3+") b1(cse)"
                    print(l7)
                    print(l8)
                if a==p and b!=p and c==p and d!=p:
                    print('In class-1:batch-3 second period is free')
                    print('In class-2:batch-2 first period is free')
                    print('In class-1:batch-3 third period is free')
                    print('In class-2:batch-1 fourth period is free')
                    e4=raw_input("which subject you want to allot ")
                    g4=raw_input("which subject you want to allot ")
                    h4=raw_input("which subject you want to allot ")
                    i4=raw_input("which subject you want to allot ")
                    l9="class1  b1(maths)  b3(phy)  break  b3("+e4+") b2(maths)"
                    l10="class2  b2(phy) b2("+g4+")    break  b1("+h4+") b1("+i4+")"
                    print(l9)
                    print(l10)
                if a==p and b==p and c!=p and d!=p:
                    print('In class-1:batch-3 second period is free')
                    print('In class-2:batch-2 first period is free')
                    print('In class-1:batch-3 third period is free')
                    print('In class-2:batch-1 fourth period is free')
                    e5=raw_input("which subject you want to allot ")
                    g5=raw_input("which subject you want to allot ")
                    h5=raw_input("which subject you want to allot ")
                    i5=raw_input("which subject you want to allot ")
                    l11="class1  b1(maths)  b3("+e5+")  break  b3("+g5+") b2(maths)"
                    l12="class2  b2("+h5+") b2(chem)    break  b1(chem) b1("+i5+")"
                    print(l11)
                    print(l12)
                    
                    
            if td=='tuesday':
                    
                    if a!=p and b==p and c==p and d==p:
                        print('In class-1:batch-1 first period is free')
                        print('In class-1:batch-2 third period is free')
                        print('In class-2:batch-3 fourth period is free')
                        t=raw_input("which subject you want to allot ")
                        v=raw_input("which subject you want to allot ")
                        w=raw_input("which subject you want to allot ")
                        f="class1  b1("+t+")  b1(phy)  break  b2("+v+") b1(cse)"
                        fa="class2  b2(cse) b3(chem)  break  b3(phy) b3("+w+")"
                        print(f)
                        print(fa)
                    if a==p and b!=p and c==p and d==p:
                        print('In class-1:batch-1 second period is free')
                        print('In class-2:batch-3 third period is free')
                        t1=raw_input("which subject you want to allot ")
                        v1=raw_input("which subject you want to allot ")
                        f1="class1  b1(maths)  b1("+t1+")  break  b2(maths) b1(cse)"
                        f1a="class2  b2(cse) b3(chem)  break  b3("+v1+") b3(maths)"
                        print(f1)
                        print(f1a)
                    if a==p and b==p and c!=p and d==p:
                        print('In class-2:batch-3 second period is free')
                        t2=raw_input("which subject you want to allot ")
                        f2="class1  b1(maths)  b1(phy)  break  b2(maths) b1(cse)"
                        f2a="class2  b2(cse) b3("+t2+")  break  b3(phy) b3(maths)"
                        print(f2)
                        print(f2a)
                    if a==p and b==p and c==p and d!=p:
                        print('In class-1:batch-1 fourth period is free')
                        print('In class-2:batch-2 first period is free')
                        t3=raw_input("which subject you want to allot ")
                        v3=raw_input("which subject you want to allot ")
                        f4="class1  b1(maths)  b1(phy)  break  b2(maths) b1("+t3+")"
                        f5="class2  b2("+v3+") b3(chem)  break  b3(phy) b3(maths)"
                        print(f4)
                        print(f5)
                    if a!=p and b!=p and c==p and d==p:
                        print('In class-1:batch-1 first period is free')
                        print('In class-1:batch-1 second period is free')
                        print('In class-1:batch-2 third period is free')
                        print('In class-2:batch-3 third period is free')
                        print('In class-2:batch-3 fourth period is free')
                        e=raw_input("which subject you want to allot ")
                        g=raw_input("which subject you want to allot ")
                        h=raw_input("which subject you want to allot ")
                        i=raw_input("which subject you want to allot ")
                        j=raw_input("which subject you want to allot ")
                        l1="class1  b1("+e+")  b1("+g+")  break  b2("+h+") b1(cse)"
                        l2="class2  b2(cse) b3(chem)  break  b3("+i+") b3("+j+")"
                        print(l1)
                        print(l2)
                    if a!=p and b==p and c!=p and d==p:
                        print('In class-1:batch-1 first period is free')
                        print('In class-1:batch-2 third period is free')
                        print('In class-2:batch-3 second period is free')
                        print('In class-2:batch-3 fourth period is free')
                        e1=raw_input("which subject you want to allot ")
                        g1=raw_input("which subject you want to allot ")
                        h1=raw_input("which subject you want to allot ")
                        i1=raw_input("which subject you want to allot ")
                        l3="class1  b1("+e1+")  b1(phy)  break  b2("+g1+") b1(cse)"
                        l4="class2  b2(cse) b3("+h1+")  break  b3(phy) b3("+i1+")"
                        print(l3)
                        print(l4)
                    if a!=p and b==p and c==p and d!=p:
                        print('In class-1:batch-1 first period is free')
                        print('in class-1:batch-1 fourth period is free')
                        print('In class-2:batch-2 first period is free')
                        print('In class-1:batch-2 third period is free')
                        print('In class-2:batch-3 fourth period is free')
                        e2=raw_input("which subject you want to allot ")
                        g2=raw_input("which subject you want to allot ")
                        h2=raw_input("which subject you want to allot ")
                        i2=raw_input("which subject you want to allot ")
                        j2=raw_input("which subject you want to allot ")
                        l5="class1  b1("+e2+")  b1(phy)  break  b2("+i2+") b1("+g2+")"
                        l6="class2  b2("+h2+") b3(chem)  break  b3(phy) b3("+j2+")"
                        print(l5)
                        print(l6)
                    if a==p and b!=p and c!=p and d==p:
                        print('In class-1:batch-3 second period is free')
                        print('In class-2:batch-2 first period is free')
                        print('In class-2:batch-2 second period is free')
                        e3=raw_input("which subject you want to allot ")
                        g3=raw_input("which subject you want to allot ")
                        h3=raw_input("which subject you want to allot ")
                        l7="class1  b1(maths)  b1("+e3+")  break  b2(maths) b1(cse)"
                        l8="class2  b2(cse) b3("+g3+")  break  b3("+h3+") b3(maths)"
                        print(l7)
                        print(l8)
                    if a==p and b!=p and c==p and d!=p:
                        print('In class-1:batch-1 second period is free')
                        print('In class-1:batch-1 fourth period is free')
                        print('In class-2:batch-2 first period is free')
                        print('In class-2:batch-3 third period is free')
                        e4=raw_input("which subject you want to allot ")
                        g4=raw_input("which subject you want to allot ")
                        h4=raw_input("which subject you want to allot ")
                        i4=raw_input("which subject you want to allot ")
                        l9="class1  b1(maths)  b1("+e4+")  break  b2(maths) b1("+g4+")"
                        l10="class2  b2("+h4+") b3(chem)  break  b3("+i4+") b3(maths)"
                        print(l9)
                        print(l10)
                    if a==p and b==p and c!=p and d!=p:
                        print('In class-1:batch-1 fourth period is free')
                        print('In class-2:batch-2 first period is free')
                        print('In class-2:batch-3 second period is free')
                        e5=raw_input("which subject you want to allot ")
                        g5=raw_input("which subject you want to allot ")
                        h5=raw_input("which subject you want to allot ")
                        l11="class1  b1(maths)  b1(phy)  break  b2(maths) b1("+e5+")"
                        l12="class2  b2("+g5+") b3("+h5+")  break  b3(phy) b3(maths)"
                        print(l11)
                        print(l12)
            if td=='wednesday':
                if a!=p and b==p and c==p and d==p:
                    print('        in class-1:batch-2 first period is free')
                    print('        in class-2:batch-3 third period is free')
                    r1=raw_input("        which subject you want to allot: ")
                    r2=raw_input("        which subject you want to allot: ")
                    print('')
                    r3="        | b2("+r1+")    | b2(computer)  |break|  b2(chemistry)  | b1(lab)       |"
                    r4="        | b3(computer)  | b1(chemistry) |break|  b3("+r2+")     | b3(chemistry) |"  
                    print(r3)
                    print(r4)
                if a==p and b!=p and c==p and d==p:
                    print('        in class-1:batch-2 third period is free')
                    print('        in class-2:batch-1 second period is free')
                    print('        in class-2:batch-3 fourth period is free')
                    print('')
                    r5=raw_input("        which subject you want to allot: ")
                    r6=raw_input("        which subject you want to allot: ")
                    r7=raw_input("        which subject you want to allot: ")
                    print('')
                    r8="        | b2(maths)     | b2(computer)  |break|  b2("+r5+")     | b1(lab)      |"
                    r9="        | b3(computer)  | b1("+r6+")    |break|  b3(maths)      | b3("+r7+")   |"
                    print(r8)
                    print(r9)
                if a==p and b==p and c!=p and d==p:
                    print('follow the above schedule.')
                if a==p and b==p and c==p and d!=p:
                    print('        in class-1:batch-2 second period is free')
                    print('        in class-2:batch-3 first period is free')
                    print('')
                    r10=raw_input("        which subject you want to allot: ")
                    r11=raw_input("        which subject you want to allot: ")
                    print('')
                    r12="        | class1  | b2(maths)    | b2("+r10+")     |break|  b2(chemistry)| b1(lab)      |"
                    r13="        | class2  | b3("+r11+")   | b1(chemistry)  |break|  b3(maths)    | b3(chemistry)|"
                    print(r12)
                    print(r13)
                if a!=p and b!=p and c==p and d==p:
                    print('in class-1:batch-2 first period is free')
                    print('in class-1:batch-2 third period is free')
                    print('in class-2:batch-2 second period is free')
                    print('in class-2:batch-1 third period is free')
                    print('')
                    r14=raw_input("        which subject you want to allot: ")
                    r15=raw_input("        which subject you want to allot: ")
                    r16=raw_input("        which subject you want to allot: ")
                    r17=raw_input("        which subject you want to allot: ")
                    print('')
                    r18="        | class1  | b1("+r14+")  |  b3(physics)   |break|  b3(computer)   | b2("+r15+")   |"
                    r19="        | class2  | b2(physics)  |  b2("+r16+")   |break|  b1("+r17+")    | b1(computer)  |"
                    print(r18)
                    print(r19)
                if a!=p and b==p and c!=p and d==p:
                    print('        in class-1:batch-2 first period is free')
                    print('        in class-2:batch-3 third period is free')
                    print('')
                    r20=raw_input("        which subject you want to allot: ")
                    r21=raw_input("        which subject you want to allot: ")
                    print('')
                    r22="        | class1  | b2("+r20+") | b2(computer)   |break|  b2(chemistry)  | b1(lab)      |"
                    r23="        | class2  | b3(computer)| b1(chemistry)  |break|  b3("+r21+")    | b3(chemistry)|"
                    print(r22)
                    print(r23)
                if a!=p and b==p and c==p and d!=p:
                    print('        in class-1:batch-2 first period is free')
                    print('        in class-1:batch-2 second period is free')
                    print('        in class-2:batch-3 first period is free')
                    print('        in class-2:batch-3 third period is free')
                    print('')
                    r24=raw_input("        which subject you want to allot: ")
                    r25=raw_input("        which subject you want to allot: ")
                    r26=raw_input("        which subject you want to allot: ")
                    r27=raw_input("        which subject you want to allot: ")
                    print('')
                    r28="        | class1  |  b1("+r24+")  | b2("+r25+")   |break|  b2(chemistry)  | b2(lab)       |"
                    r29="        | class2  |  b3("+r26+")  | b1(chemistry) |break|  b3("+r27+")    | b3(chemistry) |"
                    print(r28)
                    print(r29)
                if a==p and b!=p and c!=p and d==p:
                    print('        in class-1:batch-2 third period is free')
                    print('        in class-2:batch-1 second period is free')
                    print('        in class-2:batch-3 fourth period is free')
                    print('')
                    r30=raw_input("        which subject you want to allot: ")
                    r31=raw_input("        which subject you want to allot: ")
                    r32=raw_input("        which subject you want to allot: ")
                    print('')
                    r33= "        | class1 || b1(maths)    | b2(computer)   |break|  b2("+r30+")  |  b2(lab)    |"
                    r34= "        | class2 || b3(computer) | b1("+r31+")    |break|  b3(maths)    |  b3("+r32+")|"
                    print(r33)
                    print(r34)
                if a==p and b!=p and c==p and d!=p:
                    print('        in class-1:batch-2 second period is free')
                    print('        in class-1:batch-2 third period is free')
                    print('        in class-2:batch-3 first period is free')
                    print('        in class-2:batch-1 second period is free')
                    print('        in class-2:batch-3 fourth period is free')
                    print('')
                    r35=raw_input("        which subject you want to allot: ")
                    r36=raw_input("        which subject you want to allot: ")
                    r37=raw_input("        which subject you want to allot: ")
                    r38=raw_input("        which subject you want to allot: ")
                    r41=raw_input("        which subject you want to allot: ")
                    r39="        | class1 || b2(maths)    | b2("+r35+")   |break|  b2("+r36+") |  b1(lab)        |"
                    r40="        | class2 || b3("+r37+")  | b1("+r38+")   |break|  b3(maths)   |  b3("+r41+")    |"
                    print(r39)
                    print(r40)
                if a==p and b==p and c!=p and d!=p:
                    print('        in class-1:batch-2 second period is free')
                    print('        in class-2:batch-3 first period is free')
                    print('')
                    r42=raw_input("        which subject you want to allot: ")
                    r43=raw_input("        which subject you want to allot: ")
                    r44="        | class1 || b1(maths)   | b2("+r42+")     |break|  b2(chemistry)  | b1(lab)        |"
                    r45="        | class2 || b3("+r43+") | b1(chemistry)   |break|  b3(maths)      | b1(chemistry)  |"
                    print(r44)
                    print(r45)
            if td=='thursday':
                    if a!=p and b==p and c==p and d==p:
                       print('In class-1:batch-1 first period is free')
                       print('in class-2:batch-3 second period is free')
                       s=raw_input("which subject you want to allot ")
                       r=raw_input("which subject you want to allot ")
                       z1="b1("+s+")  b2(cs)  break  b2(chem) b3(chem)"
                       z2="b3(cs)  b3("+r+")  break  b1(cs) b1(chem)"
                       print(z1)
                       print(z2)
                    if a==p and b!=p and c==p and d==p:
                        print('In class-1:batch-2 third period and batch-3 fourth period is free')
                        print('In class-2:batch-1 fourth period is free')
                        s1=raw_input("which subject you want to allot ")
                        s11=raw_input("which subject you want to allot ")
                        r1=raw_input("which subject you want to allot ")
                        z3="b1(maths)  b2(cs)  break  b2("+s1+") b3("+s11+")"
                        z4="b3(cs)  b3(maths)  break  b1(cs) b1("+r1+")"
                        print(z3)
                        print(z4)
                    if a==p and b==p and c!=p and d==p:
                       print("No free period")
                    if a==p and b==p and c==p and d!=p:
                        print('In class-1:batch-2 second period is free')
                        print('In class-2:batch-3 first period and batch-1 third period is free')
                        s2=raw_input("which subject you want to allot ")
                        r2=raw_input("which subject you want to allot ")
                        r22=raw_input("which subject you want to allot ")
                        z5="b1(maths)  b2("+s2+")  break  b2(chem) b3(chem)"
                        z6="b3("+r2+")  b3(maths)  break  b1("+r22+") b1(chem)"
                        print(z5)
                        print(z6)
                    if a!=p and b!=p and c==p and d==p:
                        print('In class-1:batch-1 first period is free')
                        print('In class-1:batch-2 third period and batch-3 fourth period is free')
                        print('in class-2:batch-3 second period is free')
                        print('In class-2:batch-1 fourth period is free')
                        s3=raw_input("which subject you want to allot ")
                        s31=raw_input("which subject you want to allot ")
                        s32=raw_input("which subject you want to allot ")
                        r3=raw_input("which subject you want to allot ")
                        r33=raw_input("which subject you want to allot ")
                        z7="b1("+s3+")  b2(cs)  break  b2("+s31+") b3("+s32+")"
                        z8="b3(cs)  b3("+r3+")  break  b1(cs) b1("+r33+")"
                        print(z7)
                        print(z8)
                    if a!=p and b==p and c!=p and d==p:
                        print('In class-1:batch-1 first period is free')
                        print('in class-2:batch-3 second period is free')
                        s4=raw_input("which subject you want to allot ")
                        r4=raw_input("which subject you want to allot ")
                        z9="b1("+s4+")  b2(cs)  break  b2(chem) b3(chem)"
                        z10="b3(cs)  b3("+r4+")  break  b1(cs) b1(chem)"
                        print(z9)
                        print(z10)
                    if a!=p and b==p and c==p and d!=p:
                        print('In class-1:batch-1 first period is free')
                        print('In class-1:batch-2 second period is free')
                        print('in class-2:batch-3 second period is free')
                        print('In class-2:batch-3 first period and batch-1 third period is free')
                        s5=raw_input("which subject you want to allot ")
                        s51=raw_input("which subject you want to allot ")
                        r5=raw_input("which subject you want to allot ")
                        r51=raw_input("which subject you want to allot ")
                        r52=raw_input("which subject you want to allot ")    
                        z11="b1("+5+")  b2("+s51+")  break  b2(chem) b3(chem)"
                        z12="b3("+r51+")  b3("+r5+")  break  b1("+r52+") b1(chem)"
                        print(z11)
                        print(z12) 
                    if a==p and b!=p and c!=p and d==p:
                        print('In class-1:batch-2 third period and batch-3 fourth period is free')
                        print('In class-2:batch-1 fourth period is free')
                        s6=raw_input("which subject you want to allot ")
                        s61=raw_input("which subject you want to allot ")
                        r6=raw_input("which subject you want to allot ")
                        z13="b1(maths)  b2(cs)  break  b2("+s6+") b3("+s61+")"
                        z14="b3(cs)  b3(maths)  break  b1(cs) b1("+r6+")"
                        print(z13)
                        print(z14)
                    if a==p and b!=p and c==p and d!=p:
                        print('In class-1:batch-2 third period and batch-3 fourth period is free')
                        print('In class-1:batch-2 second period is free')
                        print('In class-2:batch-1 fourth period is free')
                        print('In class-2:batch-3 first period and batch-1 third period is free')
                        s7=raw_input("which subject you want to allot ")
                        s71=raw_input("which subject you want to allot ")
                        s72=raw_input("which subject you want to allot ")
                        r7=raw_input("which subject you want to allot ")
                        r71=raw_input("which subject you want to allot ")
                        r72=raw_input("which subject you want to allot ")
                        z15="b1(maths)  b2("+s72+")  break  b2("+s71+") b3("+s72+")"
                        z16="b3("+r71+")  b3(maths)  break  b1("+r72+") b1("+r7+")"
                        print(z15)
                        print(z16)
                    if a==p and b==p and c!=p and d!=p:
                        print('In class-1:batch-2 second period is free')
                        print('In class-2:batch-3 first period and batch-1 third period is free')
                        s8=raw_input("which subject you want to allot ")
                        r8=raw_input("which subject you want to allot ")
                        r81=raw_input("which subject you want to allot ")
                        z17="b1(maths)  b2("+s8+")  break  b2(chem) b3(chem)"
                        z18="b3("+r8+")  b3(maths)  break  b1("+r81+") b1(chem)"
                        print(z17)
                        print(z18)

            if td=='friday':
                    if a!=p and b==p and c==p and d==p:
                        print('In class-1:batch-2 fourth period is free')
                        print('in class-2:batch-3 second period is free')
                        print('in class-2:batch-1 third period is free')
                        x1=raw_input("which subject you want to allot ")
                        x2=raw_input("which subject you want to allot ")
                        x3=raw_input("which subject you want to allot")
                        x4="class1  b1(phy) b2(phy)  break  b2(cse) b2("+x1+")"
                        x5="class2  b3(chem) b3("+x2+")  break  b1("+x3+") b3(cse)" 
                        print(x4)
                        print(x5)
                    if a==p and b!=p and c==p and d==p:
                        print('In class-2:batch-3 first period is free')
                        x6=raw_input("which subject you want to allot ")
                        print('In class 2 following schedule takes place whereas for class 1 it is same')
                        x7="b3("+x6+")  b3(math)  break  b1(math)  b3(cse)"
                        print(x7)
                    if a==p and b==p and c!=p and d==p:
                        print('In class-1:batch-1 first period is free')
                        print('In class-1:batch-2 second period is free')
                        x8=raw_input("which subject you want to allot ")
                        x9=raw_input("which subject you want to allot ")
                        print('In class 1 following schedule takes place whereas for class 2 it is same')
                        x10="b1("+x8+")  b2("+x9+")  break  b2(cse)  b2(maths)"
                        print(x10)
                    if a==p and b==p and c==p and d!=p:
                        print('In class-1:batch-2 third period is free')
                        print('In class-2:batch-3 fourth period is free')
                        x11=raw_input("which subject you want to allot ")
                        x12=raw_input("which subject you want to allot ")
                        x13="class1  b1(phy)  b2(phy)  break  b2("+x11+")  b2(math)"
                        x14="class2  b3(chem)  b3(math)  break  b1(math)  b3("+x12+")"
                        print(x13)
                        print(x14)
                    if a!=p and b!=p and c==p and d==p:
                        print('in class-1:batch-2 fourth period is free')
                        print('In class-2:batch-3 first period is free')
                        print('In class-2:batch-3 second period is free')
                        print('In class-2:batch-1 third period is free')
                        x15=raw_input("which subject you want to allot ")
                        x16=raw_input("which subject you want to allot ")
                        x17=raw_input("which subject you want to allot ")
                        x18=raw_input("which subject you want to allot ")
                        x20="class1  b1(phy)  b2(phy)  break  b2(cse)  b2("+x15+")"
                        x21="class2  b3("+x16+")  b3("+x17+")  break  b1("+x18+")  b3(cse)"
                        print(x20)
                        print(x21)
                    if a!=p and b==p and c!=p and d==p:
                        print('In class-1:batch-1 first period is free')
                        print('in class-1:batch-2 second period is free')
                        print('In class-1:batch-2 fourth period is free')
                        print('In class-2:batch-3 second period is free')
                        print('In class-2:batch-1 third period is free')
                        x22=raw_input("which subject you want to allot ")
                        x23=raw_input("which subject you want to allot ")
                        x24=raw_input("which subject you want to allot ")
                        x25=raw_input("which subject you want to allot ")
                        x26=raw_input("which subject you want to allot ")
                        x27="class1  b1("+x22+") b2("+x23+")  break  b2(cse) b2("+x24+")"
                        x28="class2  b3(chem) b3("+x25+")  break  b1("+x26+") b3(cse)"    
                        print(x27)
                        print(x28)
                    if a!=p and b==p and c==p and d!=p:
                        print('In class-1:batch-2 third period is free')
                        print('in class-1:batch-2 fourth period is free')
                        print('In class-2:batch-3 second period is free')
                        print('In class-2:batch-1 third period is free')
                        print('In class-2:batch-3 fourth period is free')
                        x29=raw_input("which subject you want to allot ")
                        x30=raw_input("which subject you want to allot ")
                        x31=raw_input("which subject you want to allot ")
                        x32=raw_input("which subject you want to allot ")
                        x33=raw_input("which subject you want to allot ")
                        x34="class1  b1(phy) b2(phy)  break  b2("+x29+") b2("+x30+")"
                        x35="class2  b3(chem) b3("+x31+")  break  b1("+x32+") b3("+x33+")"
                        print(x34)
                        print(x35)
                    if a==p and b!=p and c!=p and d==p:
                        print('In class-1:batch-1 first period is free')
                        print('In class-1:batch-2 second period is free')
                        print('In class-2:batch-3 first period is free')
                        x36=raw_input("which subject you want to allot ")
                        x37=raw_input("which subject you want to allot ")
                        x38=raw_input("which subject you want to allot ")
                        x39="class1  b1("+x36+")  b2("+x37+")  break  b2(cse)  b2(math)"
                        x40="class2  b3("+x38+")  b3(math)  break  b1(math)  b3(cse)"
                        print(x39)
                        print(x40)
                    if a==p and b!=p and c==p and d!=p:
                        print('In class-1:batch-2 third period is free')
                        print('In class-2:batch-3 first period is free')
                        print('In class-2:batch-3 fourth period is free')
                        x41=raw_input("which subject you want to allot ")
                        x42=raw_input("which subject you want to allot ")
                        x43=raw_input("which subject you want to allot ")
                        x44="class1  b1(phy)  b2(phy)  break  b2("+x41+")  b2(math)"
                        x45="class2  b3("+x42+")  b3(math)  break  b1(math)  b3("+x43+")"
                        print(x44)
                        print(x45)
                    if a==p and b==p and c!=p and d!=p:
                        print('In class-1:batch-1 first period is free')
                        print('In class-1:batch-2 second period is free')
                        print('In class-1:batch-2 third period is free')
                        print('In class-2:batch-3 fourth period is free')
                        x46=raw_input("which subject you want to allot ")
                        x47=raw_input("which subject you want to allot ")
                        x48=raw_input("which subject you want to allot ")
                        x49=raw_input("which subject you want to allot ")
                        x50="class1  b1("+x46+")  b2("+x47+")  break  b2("+x48+")  b2(math)"
                        x51="class2  b3(chem)  b3(math)  break  b1(math)  b3("+x49+")"
                        print(x50)
                        print(x51)
    else:
        print('thank you for registering your attendance')
    x=raw_input('press enter to continue')
    if x=='no':
        break
sv=[t100,q,r,s] 
sv1=sorted(sv)
#for k in range(0,4):
for g in range(0,4):
    if sv1[3]==sv[g]:
        if g==0:
            print("ravi is the most commited teacher")
        elif g==1:
            print("ram is the most commited teacher")
        elif g==2:
            print("shyam is the most commited teacher")
        else:
            print("meena is the most commited teacher")
                
       
              
        
    
             
            



                            
                


                
            
