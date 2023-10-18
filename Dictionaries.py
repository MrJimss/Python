name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count=dict()
large_count=0
large_sender=None
for line in handle:
     words=line.split(' ')
     if 'From' == words[0]:
          count[words[1]]=count.get(words[1],0)+1
for name in count:
     if large_count < count[name]:
          large_count=count[name]
          large_sender=name
print(large_sender,large_count)
