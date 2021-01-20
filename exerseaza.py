x=[1,2,3,4,5,-1,-2,-3,-4,-5]
print('Lista 1=',x)
y=sorted(x)
print('Lista in ord crescatoare=',y)
x.sort(reverse=True)
print('Lista in ord crescatoare=',x)
print('Lungimea=',len(x))
print('MAX=',max(x))
print('MIN=',min(x))
x=[1,2,3,4,5,-1,-2,-3,-4,-5]
print('Lista 4 noua=',x+[111])
x.insert(2,222)
print('Lista 5 noua=',x)


