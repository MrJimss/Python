name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hours=list()
count=dict()
for line in handle:
     words=line.split(' ')
     if 'From' == words[0]:
          time=words[6].split(':')
          hours.append(time[0])
hours=sorted(hours)
for hour in hours:
     count[hour]=count.get(hour,0)+1
     print(count.key(),count[hour])
     
     
