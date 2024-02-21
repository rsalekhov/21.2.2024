# application/salary.py
def calculate_salary(employees):
    # Ваш код для расчета зарплаты
    total_salary = 0
    for employee in employees:
        total_salary += employee['salary']
    return total_salary

