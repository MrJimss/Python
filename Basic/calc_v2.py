print('Hello user welcome to the program!')
print('I will help you calculate any number you want')
operation=input('Enter operation separated by spaces:')
symbols=['+','-','*','/']
ops={
    '+':lambda x,y: x+y,
    '-':lambda x,y: x-y,
    '*':lambda x,y: x*y,
    '/':lambda x,y: x/y,
}

operation=operation.split(' ')
print(ops[operation[1]](int(operation[0]),int(operation[2])))