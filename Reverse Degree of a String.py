s = input("enter word:")
x = 70
list = []
t=1
for x in s:
    y = ord(x)-ord('a')
    j = 26-y
    list.append(j*t)
    t = t+1
    j=0
  
for k in list:
    print(k)
          