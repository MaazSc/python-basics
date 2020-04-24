l=[]
n=int(input("Enter the number of inputs!"))
for i in range(0,n):
    q=int(input("Enter the values:"))
    l.append(q)
print(l)
print(len(l))
total=0
for i in l:
    total=total+i
x=format(total,'0.2e')
print(x)
T=tuple(l)
print(T)
jobs=["maaz",20]
tup=("a","b",20,jobs,100)
print(tup)
n=11
while n<20:
   print("n",n)
   n=n+1
