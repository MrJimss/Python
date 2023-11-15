def my_min(x, y, *args):
    min = args[0]
    for n in args:
    		if n<min: 
    			min = n
    if x < min:
    	min = x
    if y < min : 
    	min = y
    return min 
print(my_min(8, 13, 4, 42, 120, 7, 6, 2, 1, 65, 100)) 