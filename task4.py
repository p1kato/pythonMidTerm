class ItemsProcessor:
    def __init__(self):# __init__: This method is used to initialize the object. It initializes an empty dictionary named items_storage that will be used to store the items
        self.items_storage = dict()

    def add_items(self):# add_items: This method prompts the user to enter items separated by commas.
        items = input("Пожалуйста, вводите пункты через запятую ").split(',')
        for item in items:
            item = item.strip()
            if item in self.items_storage:
                self.items_storage[item] += 1
            else:
                self.items_storage[item] = 1

    def display_items(self):# display_items: This method displays all the unique and non-unique items stored in the items_storage dictionary. It also shows the counts of the non-unique items.
        unique_items = set()
        not_unique_items = []

        for item, count in self.items_storage.items():
            if count > 1:
                not_unique_items.append((item, count))
            else:
                unique_items.add(item)

        print("Элементы сохраняются")
        print("Уникальные предметы:", unique_items)
        print("Не уникальные предметы:", tuple(not_unique_items))

if __name__ == "__main__":
    items_processor = ItemsProcessor()#In the main block of the code, an instance of the ItemsProcessor class is created.
    while True:
        print("\nПожалуйста, выберите задачу, которую вы хотите выполнить:")
        print("1) Ввод элементов")
        print("2) Выход")

        user_input = int(input("Enter your choice: "))

        if user_input == 1:
            items_processor.add_items()
        elif user_input == 2:
            items_processor.display_items()
            break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")