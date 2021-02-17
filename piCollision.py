
import math
#Only applies when M2 is smaller than M1
#M2 is stationary and M1 is colliding with M2 with speed V (Initial Conditions)
#ratio between M1 and M2 is a

#Constants
n=8
a = 10**n
M2 = 1
M1=a*M2
V = 1

p1=[]
p2=[]

#Initial Conditions
p1.append(M1*V)
p2.append(0)

count = 0
while(True):
    #print("collision with " + str(p1[len(p1)-1])+" and "+str(p2[len(p2)-1]))
    #Collision happens
    p1.append(((a-1)/(a+1))*p1[len(p1)-1] - (2*a/(a+1))*abs(p2[len(p2)-1]))
    p2.append((2/(a+1))*p1[len(p1)-1] + ((a-1)/(a+1))*abs(p2[len(p2)-1]))
    count += 1
    
    
    #Collision with wall
    
    count += 1 #flipping of sign already encoded in above equation
    #print("WALL")
    if p1[len(p1)-1] <= 0 and abs((p1[len(p1)-1]/M1)) > abs((p2[len(p2)-1]/M2)):
        break

print(math.floor(math.pi/math.sqrt(1/a)))

print(math.floor(count))
##print(p1)
##print(p2)
    
