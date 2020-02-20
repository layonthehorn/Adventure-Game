import time

# testing cooking puzzle

# gets starting time
start_time = time.time()

# loop to wait for player input
cooking = True
while cooking:
    user_input = input("Press enter to quit.")
    cooking = False

# checks if you let it cook for about 20 seconds
total_time = time.time() - start_time
print(total_time, "Time taken.")
if 25.0 > total_time > 18.0:
    print("It's working now!")
else:
    print("I didn't time it right.")
