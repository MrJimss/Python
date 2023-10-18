n=1
with open("Movies.txt") as f:
    for line in f.readlines():
        word=line.split(' ')
        print("Line "+str(n)+': '+ str(len(word))+" words")
        n+=1

