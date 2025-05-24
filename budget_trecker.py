import json

"""
Расчет быджета изходя из первоначальной суммы
"""

def get_total_expenses(expenses):
    sum = 0
    for expence in expenses:
        sum += expence["amount"]
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Добавлена трата: {description} на сумму: {amount}")

def show_budget_details(budget, expenses):
    print(f"Общий бюджет: {budget}")
    print("\nЗатраты:")
    for expens in expenses:
        print(f"- {expens["description"]}: {expens["amount"]}")

    print(f"Общие траты: {get_total_expenses(expenses)}")
    print(f"Оставшийся бюджет:{round(get_balance(budget, expenses), 2)}")

def load_budget_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except(FileNotFoundError, json.JSONDecodeError):
        return 0, [] # Вернет значения по умолчанию если такого файла нет или он пустой
    
def save_budget_details(file_path, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Добро пожаловать в программу заказов")
    file_path = 'budget_data.json' # Объявление пути для сохранения бюджета в файл
    initial_budget, expenses = load_budget_data(file_path)
    if initial_budget == 0:
            initial_budget = float(input("Пожалуйста введите ваш бюджет: "))

    budget = initial_budget

    while True:
        print("Ваши дальнейшие действия:")
        print("1. Добавить трату")
        print("2. Показать детали бюджета")
        print("3. Выход")

        choice = input("Введите цифру выбора: (1/2/3)")

        if choice == '1':
            description = input("Введите краткое описание данной траты денег. ")
            amount = float(input("Введите сумму, которую вы потратили. "))
            add_expense(expenses, description, amount)
        elif choice == '2':
            show_budget_details(budget, expenses)
        elif choice == '3':
            save_budget_details(file_path, initial_budget, expenses)
            print("Завершение программы! Досвидания!!!")
            break
        else:
            print("Неверный выбор, пожалуйста, выберите правильно...")

if __name__ == "__main__":
    main()