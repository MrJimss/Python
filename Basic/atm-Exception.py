#small program that tests a function that adds an exception to the code

def withdraw(amount):
   print('$'+str(amount) + " withdrawn!")
   
correct=False
#your code goes here
while correct==False:
    try:
        value=int(input("Please enter an amount to withdraw: "))
        correct=True
    except:
        print('Error! Please enter a number!\n')
withdraw(value)