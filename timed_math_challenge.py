hello_text = """
           With this small program 
           you can train your speed 
    in solving small mathematical operations

            press ENTER to start

"""

import random
import time

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATORS)

    expr = str(left) + " " + str(operator) + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0

input(hello_text)
# input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()

    while True:
        guess = input("Problem № " + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        else:
            wrong += 1
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds! And You did", wrong, "mistakes")