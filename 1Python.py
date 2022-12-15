student1=["Max","man",3]

student2=["Eva","woman",4]

student3=["Petya","man",3]

student4=["Masha","woman",5]

molodec=[]

if (student1[1]=="woman" and (student1[2]==4 or student1[2]==5)):
    
	molodec.append(student1[0])

if (student2[1]=="woman" and (student2[2]==4 or student2[2]==5)):
    
	molodec.append(student2[0])

if (student3[1]=="woman" and (student3[2]==4 or student3[2]==5)):
    
	molodec.append(student3[0])

if (student4[1]=="woman" and (student4[2]==4 or student4[2]==5)):
    
	molodec.append(student4[0])

print(molodec)