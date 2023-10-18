def convert(num):
    if num==1:
        return 1
    return (num % 2 + 10 * convert(num // 2)) 
   
n=int(input())
binary=convert(n)
print(binary)