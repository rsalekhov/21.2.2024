# main.py
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime  # Добавляем импорт модуля datetime

def main():
    employees = get_employees()
    total_salary = calculate_salary(employees)
    print(f'Total salary for employees: {total_salary}')

    current_date = datetime.now()  # Получаем текущую дату и время
    print(f'Current date: {current_date}')

if __name__ == "__main__":
    main()
