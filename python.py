'''import keyword
print(keyword.kwlist)'''

'''
a=None
print(a)
print(type(a))
print(bool(a))
print(bool(0.0))
print(int())
'''

'''
a=3+5j
print(a)
'''

'''
a = "happy father's day"
print(a)  
print(a[-5])  "s"
print(a[6])  "f"
'''

'''
a={'a':[10,20,30],'b':40}
print(a['a'][1])  "10"
'''
'''
a='hello'
print(a[2:4])  "ll'
print(a[2:4]+a[-3:-2]) "ll ll"
print(a[2:3+1]) "ll"
'''

'''
a="good morning"
print(a[7:11])  "rnin"
print(a[-5:-1])  "rnin"
'''

'''
a='hello'
print(a[3:0:-1])     "lle"
print(a[-2:-5:-1])   "lle"
print(a[::-1])
'''

'''
a="good morning"
print(a[1:5+1:2])  "odm"
print(a[5:11+1:3])  "mng"
print(a[-7::3])    "mng"
'''

'''
a="good morning"
print(a[8:6:-1])
print(a[-4:-6:-1])
'''

'''
a=input("enter ")  
print(a,type(a))    "string"

a=int(input("enter ")) 
print(a,type(a))   "integer"

a=eval(input("enter"))
print(a,type(a))  "type of input given"
'''

'''
""CHECK LENGTH OF LIST""
a=eval(input(("enter a list  : ")))
if len(a) == 5:
    print("the lenth of the list is 5 ")
else:
    print("length of list is not 5 ")

'''

'''
print(ord('a'))  "ASCII VALUE"
print(chr(97))   "give ascii value and get character"
'''

'''
chr = input("enter a char: ")
if "A"<=chr<="Z":
    print('upper')
elif "a"<=chr<="z":
    print("lower")
else:
    print("not an alphabet")
'''

'''
username = input('enter: ')
if username == "hero":
    print("correct username. ")
    pw = input('enter: ')
    if pw == "pass":
        print("password correct           loging in")
    else:
        print("incorrect password!! ")
else:
    print("incorrect username")
'''

'''
i=1
for i in range(51):
    if i%2 == 0:
        print(i,"is even")
        i+=1
'''

'''
s=input("enter")
rev=''
for i in s:
    rev=i+rev
print(rev)
'''

'''
for i in rangr(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
'''


'''
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("@",end="")
        else:
            print('1',end=" ")
    print()
'''

















