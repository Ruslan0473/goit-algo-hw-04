import re
import pathlib


def total_salary(path):
    try:
        with open(path,"r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("Файл порожній")
            total_salary = 0
            for line in lines:
                _, salary_str = map(str.strip, line.split(","))
                salary = int(salary_str)
                total_salary += salary
            average_salary = total_salary / len(lines)

            return total_salary, average_salary

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {path} не знайдено")

    except Exception as e:
        raise ValueError(f"Помилка обробки файлу: {str(e)}")


total, average = total_salary("c:/Users/admin/Desktop/PYTHON/M_4/hw_4/hw_4_1.txt")
print(f"Загальна сума заробітної плати: {total} Середня заробітна плата: {average}")
