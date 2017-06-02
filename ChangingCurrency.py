#THIS PROGRAM IS WRITTHEN BY AKINKUOTU MERCY
# CSC/13/4976
# penny=100cents equivalent to  dollar
#1 dime=10 cents equivalent toone tenth a dollar
#1 quater =25 cents equivalent to quarter a dollar
#1 nickel=5 cents equivalent to one twentieh of a dollar
change={100:"penny",25:"quarter",10:"dime",5:"nickel"}# This line of codes creates dictionary to hold the money and there value
h=change.keys()
print "AKINKUOTU MERCY           CSC/13/4976"
#This line of code takes the key of the dictionary above and creates an array for it
m,r,d,t=0,0,0,0

#prints the maxium value of the array
n=input ("Enter the value of cent to be changed")
while(n>=max(h)):
    n= n-max(h)
    m= m+1
print m,"pennies was used"
h.remove(max(h))

#The h.remove(max(h)) removes the maximum value of the array h which as been utilised
while(n>=max(h)):
    n= n-max(h)
    r=r+1
print r,"quarter was used"
h.remove(max(h))
while(n>=max(h)):
    n= n-max(h)
    d=d+1
print d,"dime was used"
h.remove(max(h))
while(n>=max(h)):
    n= n-max(h)
    t=t+1
print t,"nickel was used"
#Total number of coins
total=r+d+m+t
print "Total number of coin used is",total





