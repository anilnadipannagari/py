inp=input('Enter the Value')
i=0
out=''
while i<len(inp):
    if not(
        'A'<=inp[i]<='Z'or
        'a'<=inp[i]<='z' or
        '0'<=inp[i]<='9'
        ):
        out =out+"_"
    else:
        out+=inp[i]
    i+=1
print(out)