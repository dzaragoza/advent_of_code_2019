import re

nr_valid = len([i for i in range(356261,846303+1) 
                    if list(str(i)) == sorted(str(i)) 
                        and re.search(r'([0-9])\1+',str(i))])
print(nr_valid)
