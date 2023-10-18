tweet=input("Please enter text to tweet:\n")

try:
    if len(tweet)>42:
        raise InvalidLength("Only tweets under 42 characters!")
except:
    print('error')          
else:
    print('posted')