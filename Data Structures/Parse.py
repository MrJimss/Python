#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' . You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    words=line.split(' ')
    if 'From' in words:
        print( words[1])
        count+=1
    else:
        continue

print("There were", count, "lines in the file with From as the first word")
