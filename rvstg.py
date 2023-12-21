# inp=str(input())
# d=len(inp)
# i=d #length is 7
# while i>0: #
#     print(inp[i])
# i-=1
a=input()
i=0
out=''
while i<len(a):
    out= a[i]+out
    i+=1
print(out)