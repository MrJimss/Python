contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name=input('Enter the person s name')
for contact in contacts:
     if name in contact:
          print(str(contact[0])+' is '+str(contact[1]))

     