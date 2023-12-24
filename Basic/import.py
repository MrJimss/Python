from random import choice
from statistics import multimode

rota =[]
students= ["Norm", "Gina", "Michael", "Jacob", "Rosa", "Raymond", "Terence", "Amy", "Charles", "Kevin"]

for i in range(20):
  selected= choice(students)
  rota.append(selected)
  print(f'For week {i+1}, {selected} has been selected to share a reflection.')

most_frequent_presenter = multimode(rota)
if len(most_frequent_presenter) > 1:
  print(f"The people we'll be hearing the most from are {most_frequent_presenter}.")
else:
  print(f"The person we'll be hearing the most from is {most_frequent_presenter[0]}.")




