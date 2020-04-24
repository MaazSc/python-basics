def prime():
    a=int(input("Enter the number!!="))
    for i in range(2,a):
        if a%i==0:
            print("Not prime")
            break
    else:
            print("Prime")
prime()
"""how range works!!!
b=10
for i in range(1,b):
    print(i)
"""