st=str(input())
d=len(st)   
i=1
out=''
while i<d:
    if st[i] in '10':
        if st[i]==0:
            out+='1'
        else:
            out+='0'
        i+=1
print(out)



