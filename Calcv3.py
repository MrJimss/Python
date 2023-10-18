print('Hello user welcome to the program!')
print('I will help you calculate any number you want')
operation=input('Enter operation separated by spaces:')

symbols=['+','-','*','/']
ops={
    '+':lambda x,y: x+y,
    '-':lambda x,y: x-y,
    '*':lambda x,y: x*y,
    '/':lambda x,y: x/y,
    'sqr': lambda x: sqrt(x),
}

operation=operation.split(' ')
res=operation[0]
for index, operand in enumerate(operation):
    if operand in symbols:
        total=(ops[operand](int(res),int(operation[index+1])))
        res=total
        

print(total)