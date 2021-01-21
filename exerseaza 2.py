with open('input.txt','r') as f:
    x=f.readline()
with open('rezultat.txt','w')as f:
    f.write(str(x))    
y=sorted(x)
with open('rez.txt','w')as f:
    f.write(str(y))
x.sort(reverse=True)
with open('rez.txt','w')as f:
    f.write(str(x))
x=[1,2,3,4,5]
with open('rez.txt','w')as f:
    f.write(str(len(x)))
    f.write(str(max(x)))
    f.write(str(min(x)))
with open('rez.txt','w')as f:
    f.write(str(x+[111]))
x.insert(2,222)
with open('rez.txt','w')as f:
    f.write(str(x))    

