print("Введите число")
n=list(input())
d=len(n)
f=0
c=0
h=1
for i in range(0,d):
 f+=int(n[c])*(2**(d-h))
 c+=1
 h+=1
print(f)
