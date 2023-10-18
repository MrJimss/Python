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

pf_expression = "5 3 8 * 7 + 4 6 - / 9 2 + 12 4 / * + 15 3 1 + * - "
result = calculator(pf_expression)
print("Result:", result)