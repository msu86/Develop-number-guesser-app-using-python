import random
my_rand_value = random.randrange(1, 50)
attempts = 5
print("Guess a number between 1 to 50")
while True:
    i = int(input("Enter your number - "))
    attempts -= 1
    if attempts == 0:
        print("You lose")
        break
    if i == my_rand_value:
        print("correct")
        break
    if i < my_rand_value:
        print("correct answer is grater")
        print("You have", attempts, "chances left")
    else:
        print("correct answer is smaller")
        print("You have", attempts, "chances left")
