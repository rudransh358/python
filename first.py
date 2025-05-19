x=10+20j
print(id(x))
print(type(x))
print(x.real)
print(x.imag)
x=True
print(id(x))
print(type(x))
x=False
print(type(x))
x=True
y=False
print(x+y)
print(x+x)
S="$"
print(type(S))
print(id(S))
n='''rudransh singh'''
print(n)
print(id(n))
n='''rudransh" singh'''
print(n)
print(id(n))
c="rudransh singh"
print (c)
print(type(c))
v='''rudransh singh'''
print(v)
print(type(v))
c="rudransh singh"
print(c[-2])
c=1.23
print(type(c))
c="hello world"
x=c[5:4]
print(x)
y=c[1:10:1]
print(y)
s="123"
n=s*4
print(n)
x=float(12)
print(x)
x=float(True)
print(x)
x=complex(10)
print(x)
y=complex(True)
print(y)
z=complex(10,20)
print(z)

y=bool(0+0j)
print(y)
x=str(12.35)
print(x)
x=25
print(id(x))
x=257
y=257
print(x is y)
a=bytes([2,3,4,10,200])
print(a[1])
print(id(a))
x=bytes([100,200,3,80,5])
print(x[1])
x=[20,30,100,24]
a=bytearray(x)
print(type(a))
print(a[1])
l=[]
l.append(True)
l.append(200)
l.append("Hello")
print(l)
l1=l*3
print(l1)
l=(20,30,12.5,True)
print(type(l))
print(id(l))
print(l)
print(l[0])
print(l[-1])
r=range(10)
print(type(r))
print(r)
r=range(10,100)
for x in r:
    print(x)
r=range(1,10,2)
for x in r:
    print(x)
s=set()
print(type(s))
s.add(True)
s.add(20)
s.add(12.4)
s.add("Hello")
print(s)
s.remove(True)
print(s)
fs=frozenset(s)
print(type(fs))
print(fs)
d={}
print(type(d))
d['key1']='val1'
d['key2']='val2'
print(d)
d1={}
d1[1]='False'
d1[2]='True'
print(d1)
a='Hello'
userdata=input(a)
print(userdata)
data=input("Enter any word")
name=("Rudransh Singh")
l=name.split()
print(l)