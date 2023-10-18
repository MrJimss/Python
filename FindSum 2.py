import re
numlist = list()
fhand = open('regex_sum_1761772.txt')

for line in fhand:
     line = line.rstrip()
     x= re.findall('\d+',line)
     if len(x) > 0:
         for i in x:
             numlist.append(int(i))
print(sum(numlist))

     
     