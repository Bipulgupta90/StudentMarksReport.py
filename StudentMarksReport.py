#Program for accept student number and varidate..
while(True):
    sno=input("Enter Student Numbers:")
    if(sno.isdigit()) and (int(sno) in range (100,201)):
        break
    print("\t{} is invalid Student Number--Try Again".format(sno))

#accept name and validation of name
while(True):
    name=input("Enter Ur Name:") #BIPUL KUMAR GUPTA ....AND Bipul Kuma5r gupta
    namewords=name.split() #['BIPUL','KUMAR', 'GUPTA']
    if(len(namewords)==0):
        print("\Don't Enter Space---Enter Ur Name")
    else:
        res=True
        for word in namewords:
            if(not word.isalpha()):
                res=False
                break
            if(res):
                break
            else:
                print("\t{} is invalid Name--Try Again".format(name))

# accept c lang marks and validate...
    while(True):
        cm=input("Enter Marks in C:")
        if(cm.isdigit()) and (int(cm) in range(0,101)):
            break
        print("\t{} is invalid Marks in C Lang--Try Again".format(cm))

#accept c++ lang marks and validate..
    while(True):
        cppm=input("Enter Marks in C++:")
        if(cppm.isdigit()) and (int(cppm) >=0 and int(cppm)<=100):
            break
        print("\t{} is invalid Marks in c lang --Try Again".format(cppm))

#accept python lang marks and validate..
    while(True):
        pym=input("Enter Marks in PYTHON:")
        if(pym.isdigit()) and (0<=int(pym)<=100):
            break
        print("\t{} is invalid Marks in c lang --Try Again".format(pym))

#calculate totalmarks and percentage of marks
    totalmarks=int(cm) + int(cppm) + int(pym)
    percent=(totalmarks/300)*100

    if(int(cm)<40) or (int(cppm)<40) or (int(pym)<40):
        grade="FAIL"
    else:
        if(totalmarks in range (250,301)):
            grade="DISTINCTION"
        elif(200<=totalmarks<=249):
            grade="FIRST"
        elif(totalmarks>=150 and totalmarks<=199):
            grade="SECOND"
        elif(totalmarks in range(120,150)):
            grade="THIRD"

        print("-"*50)
        print("Student Marks Report")
        print("-"*50)
       
        print("\tStudent Number:{}".format(sno))
        print("\tStudent Name:{}".format(name))
        print("\tStudent Marks in C:{}".format(cm))
        print("\tStudent Marks in C++:{}".format(cppm))
        print("\tStudent Marks in PYTHON:{}".format(pym))

        print("-"*50)
        print("\tStudent totalmarks:{}".format(totalmarks))
        print("\tStudent percentage of marks:{}".format(percent))
        print("\tStudent grade:{}".format(grade))
        print("-"*50)




