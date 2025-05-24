"""
Простой аналог игры Hangman с висилицей.
Здесь представлено несколько слов,
при желании их можно увеличить и будет интереснее,
Так-же можно уменьшить количество жизней (attempts)

"""

import random

words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

choisen_word = random.choice(words)

word_display = ['_' for _ in choisen_word]

attempts = 8 # Максимальное количество ошибок при угадывании слова

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))

    guess = input("Угадайте букву в слове: ").lower()

    if guess in choisen_word:
        for index, letter in enumerate(choisen_word):
            if letter == guess:
                word_display[index] = guess # Показываем букву на экране
    else:
        print("Такой буквы не существует в данном слове.")
        attempts -= 1
        print(f"Осталось {attempts} жизней")

# Заключение в игре
if '_' not in word_display:
    print("Вы угодали слово!")
    print(' '.join(word_display))
    print("Вы смогли выжить")
else:
    print(f"Вы потратили все жизни и не смогли разгадать слово: {choisen_word}")
    print("Вы ПРОИГРАЛИ")