import re

nr_valid = 0

for i in range(356261,846303+1):
    if list(str(i)) == sorted(str(i)):
        three_plus = set(re.findall(r'([0-9])\1{2,}',str(i)))
        twos = set(re.findall(r'([0-9])\1+',str(i)))
        if len(twos - three_plus) > 0:
            nr_valid+=1
        
print(nr_valid)
