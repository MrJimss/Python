print('Hello user welcome to the program!')
print('I will help you calculate any number you want')
first=int(input('Enter number:'))

symbols=['+','-','*','/']
sign= input()
second=int(input('Enter second number:'))
if sign =='+':
    res= first + second
if sign =='-':
    res= first - second
if sign =='*':
    res= first * second
if sign =='/':
    res= first / second
else:
    print("Symbol not supported")

print("the result is: "+str(res))

