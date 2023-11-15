def prefix_to_postfix(prefix_expression):
     def is_operator(char):
          return char in "+-*/"

     stack = []
     tokens=list(prefix_expression)
     tokens.reverse()
     for token in tokens:
          if not is_operator(token):
               stack.append(token)
          else:
               operand1 = stack.pop()
               operand2 = stack.pop()
               result = operand1 + operand2 + token
               stack.append(result)
     return stack

def calculator(postfix_expression):
     def is_operator(char):
          return char in "+-*/"
     stack = []
     tokens = list(postfix_expression)
     for token in tokens:
          if not is_operator(token):
               stack.append(token)
          else:
               operand1 = stack.pop()
               operand2 = stack.pop()
               result = eval(operand1 + token + operand2)
               stack.append(str(result))
     return stack.pop()

def infix_to_postfix(infix_expression):
     def is_operator(char):
          return char in "+-*/"
     stack = []
     tokens = infix_expression.split(" ")
     result = ""
     for token in tokens:
          if not is_operator(token):
               result += token
          else:
               while len(stack) > 0 and stack[-1] != "(" and precedence(stack[-1]) >= precedence(token):
                    result += stack.pop()
               stack.append(token)
     while len(stack) > 0:
          result += stack.pop()
     return result

def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z')) 
 
# Get Infix for a given postfix 
# expression 
def getInfix(exp) :
 
    s = [] 
 
    for i in exp:     
         
        # Push operands 
        if (isOperand(i)) :         
            s.insert(0, i) 
             
        # We assume that input is a 
        # valid postfix and expect 
        # an operator. 
        else:
         
            op1 = s[0] 
            s.pop(0) 
            op2 = s[0] 
            s.pop(0) 
            s.insert(0, "(" + op2 + i +
                             op1 + ")") 
             
    # There must be a single element in 
    # stack now which is the required 
    # infix. 
    return s[0]

# Example usage:

prefix_expression = "-/a+bc*-de+fg"  # Example prefix expression
postfix_expression = prefix_to_postfix(prefix_expression)
infix_exp=getInfix(postfix_expression)
print("Postfix expression:", postfix_expression)
print("Infix expression:", infix_exp)
abc+/de-fg+*-
