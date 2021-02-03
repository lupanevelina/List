with open('input.txt', 'r') as f:
    lista=f.readline()
x=sorted(lista)
if x==lista :
    print('Da')    
else :
    print('Nu')