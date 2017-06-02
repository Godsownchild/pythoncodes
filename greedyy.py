"""PROGRAM TO  SCHEDULE THE MOST TALKS POSSIBLE IN A SINGLE HALL"""
print"NAME: AKINKUOTU  MERCY   MATRIC NUMBER:CSC/13/4976"
n=input("Enter  the number of  talks ")
S=[]
F=[]
a=[]
b=[]
for i in range(n):
    start=input("enter start time")
    b.append(start)
    finish=input("enter finish time")
    b.append(finish)
    S.append(start)
    F.append(finish)
    a.append(b)
    b=[]
print "a",a
print "start time",S
print "Finish time",F
A=[a[1]]
i=1
for m in range(1,n):
    if( S[m]>=F[i]):
        A.append(a[m])
        i=m
print A
print"maximum number of talks in a single lecture hall is ",len(A)







    
    
