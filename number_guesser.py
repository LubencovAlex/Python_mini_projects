# In this application you can guess numbers from 0 to the number you want.
# В данном приложении вы можете угадывать числа, сгенерированные случайным образом в заданном вами диапазоне, (от 0 до N)

import random

top_of_range = input("Введите число: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Пожалуйста, введите число больше, чем 0, в следующий раз.")
        quit()

else:
    print("Пожалуйста, введите ЧИСЛО в следующий раз.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Ваши предположения: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Пожалуйста, в следующий раз введите число.")
        continue

    if user_guess == random_number:
        print("Вы отгадали!")
        break
    
    elif user_guess > random_number:
        print("Немного выше чем сгенерировалось!")
    else:
        print("Немного ниже чем сгенерировалось!")

print("Вы отгадали с", guesses, "попытки.")