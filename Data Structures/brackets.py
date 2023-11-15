def bracket(str):
     opening = ['(', '[', '{']
     closing = [')', ']', '}']
     stack = []
     char = list(str)
     for i in char:
          if i in opening:
               stack.append(i)
               print(stack)
          elif i in closing:
               
               if(len(stack) == 0):
                    print("Unbalanced")
               else:
                    stack.append(i)
                    print(stack)
                    stack.pop()
                    stack.pop()
                    print(stack)
     if(len(stack) == 0):
         print("Balanced")

bracket("({}{()]{}})")