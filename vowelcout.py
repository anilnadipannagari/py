a='dsifgufs'
vovel_cout=0
cons_cout=0
for var in a:
    if 'A'<=var<='Z' or 'a'<=var<='z':
        if var in 'aeiouAEIOU':
            vovel_cout+=1
        else:
            cons_cout+=1
print(vovel_cout,cons_cout)