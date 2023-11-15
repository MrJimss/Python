#converter from decimal to binary

def convert(num):
    if num==1:
        return 1
    return (num % 2 + 10 * convert(num // 2)) 
   
n=int(input("Enter a number:"))
binary=convert(n)
print(binary)