RoI=float(input("Enter the Rate of Interest= "))
NoY=int(input("Enter the number of years!= "))
PA=float(input("Enter the principle Amount= "))
r=RoI/100
SimpleInterest=(PA*NoY*r)/100
print("The simple Interest for the Principle Amount:",PA,"is:",SimpleInterest)
print("The amount to be paid after ",NoY," is ",(SimpleInterest+PA))
