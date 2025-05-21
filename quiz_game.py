
questions = [
    {
        "prompt": "Столица Франции?",
        "options": ["A. Париж", "B. Лондон", "C. Берлин", "D. Мадрид"],
        "answer": "A"
    },
    {
        "prompt": "Основной язык в Бразилии?",
        "options": ["A. Испанский", "B. Португальский", "C. Английский", "D. Французкий"],
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("\nВведите ваш ответ (A, B, C, или D): ").upper()

        if answer == question["answer"]:
            print("Правильно УРАААА!!!\n")
            score += 1
        else:
            print("Не правильно Двоечник!!! Правильный ответ", question["answer"], "\n")
    print(f"У тебя {score} правильных ответа из {len(questions)}\n")

is_want = input("Вы хотите решить тест? (Y/N) ").upper()

if is_want == "Y":
    print("\nСупер, тогда начинаем:\n")
    run_quiz(questions)
elif is_want == "N":
    print("Жаль что не хотите, было бы весело.")
else:
    print("Не понятно что вы ответили, буду думать, что вы не хотите решать тесты :(")