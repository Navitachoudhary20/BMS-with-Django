
fname="sa2222meer"
lname="bhoir"
import re
m=0
for i in fname+lname:
    m+=1
    if re.match('^[0-9]+$',i):
        print("yes",i)
        
print(m)