import operator

operations = {#This code first defines a dictionary called operations, which maps operation symbols to their corresponding Python function from the operator module.
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}

print("Пожалуйста, выберите операцию, которую вы хотите выполнить:")
print("1. +")
print("2. -")
print("4. *")
print("5. /")
print("6. ^")

operation = input()#Next, the code uses the input() function to get the user's choice. The input() function returns a string, which is then used as a key to retrieve the corresponding Python function from the operations dictionary.

try:
    func = operations[operation]
    numbers = list(
        map(int, input("Пожалуйста, введите два числа для операции {}, разделенные запятой".format(operation)).split(',')))

    if operation == "^" and numbers[1] == 0:
        print("Бесконечные числа не могут быть возведены в степень.")
    else:
        print(func(*numbers))

except Exception as e:
    print("ошибка брат:", str(e))