num1 =input()#taking sring of the input from the user 
le=len(num1)# calculating its length
i=0#initializong while loop 
sum=0#taking sum value to calculate all the natural numbers
while i<len(num1):#iterating by taking i as zero and length as input length
    if num1[i] in '1234567890':#serching for the number in the length at 
        sum+=num1[i]
    i=i+1
print(sum)
