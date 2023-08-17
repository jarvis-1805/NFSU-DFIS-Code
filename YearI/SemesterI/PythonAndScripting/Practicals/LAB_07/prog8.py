s=set()
type(s)
L=[1,2,4,5,5]
s1=set(L)
print(s1)
s.add(6)
print(s)
s=s.union({5,6,7})
print(s)
s1.intersection([6,7])
s.remove(5)
print(s)

