password_length = 6
counter = 1
permutations = 1
attempts = 5
max_lock = int(permutations/attempts)
locks= 0 
total_lock_time = 0 
lock_time_multiplier = 5
while counter <= password_length:
  permutations*=counter
  counter+=1
for num in range(max_lock):
  locks+=1
  total_lock_time+= (locks*lock_time_multiplier)
  print(f"Your account is locked for {lock_time_multiplier*locks} minutes")

print(f"Assuming the hacker only got the password right with the last possible combination, your account would have been locked for {total_lock_time} minutes in total.")

