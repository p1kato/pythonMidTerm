def calculate_tax(name, salary):#The code defines a function called calculate_tax that takes in two parameters, name and salary.
    if isinstance(salary, (int, float)) and salary >= 0:#The function checks if the salary input is a non-negative number (integer or float). If it is, the function calculates the tax level by multiplying the salary by 0.2.
        tax = salary * 0.2
        return f"{name}, Уровень налога, который вы будете платить вместе с зарплатой {salary} is {tax}"
    else:#If the salary input is not a non-negative number, the function returns a string that asks the person to enter their desired salary as a digit.
        return f"{name}, Пожалуйста, введите желаемую зарплату в цифровом виде пж."


def get_input():#The code also defines a function called get_input. This function prompts the user to enter their name and desired salary level.
    name = input("Напишите свое имя: ")
    salary = input("Введите желаемый уровень заработной платы: ")

    if salary.isdigit():
        salary = int(salary)
    elif salary.replace('.', '', 1).isdigit():
        salary = float(salary)
    else:
        return calculate_tax(name, salary)

    return calculate_tax(name, salary)#The function checks if the salary input is a digit or a decimal number. If it is, the function converts the salary input to an integer or float and passes it to the calculate_tax function.


print(get_input())