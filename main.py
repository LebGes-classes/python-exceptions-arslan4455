class ItemCard:
    """
    Класс, представляющий карточку товара.
    """
    def __init__(self, article_number: int, name: str, quantity: int, location: str, 
                 supplier: str, manufacturer: str, price: float, category: str, 
                 subcategory: str, status: str = "в наличии"):
        self.__int_article_number = article_number
        self.__str_name = name
        self.__int_quantity = quantity
        self.__str_location = location
        self.__str_supplier = supplier
        self.__str_manufacturer = manufacturer
        self.__float_price = price
        self.__str_category = category
        self.__str_subcategory = subcategory
        self.__str_status = status

    # --- ГЕТТЕРЫ ---
    def get_article_number(self) -> int:
        """Returns: int: Артикул."""
        return self.__int_article_number

    def get_name(self) -> str:
        """Returns: str: Имя."""
        return self.__str_name

    def get_quantity(self) -> int:
        """Returns: int: Кол-во."""
        return self.__int_quantity

    def get_price(self) -> float:
        """Returns: float: Цена."""
        return self.__float_price

    def get_status(self) -> str:
        """Returns: str: Статус."""
        return self.__str_status

    # --- СЕТТЕРЫ ---
    def set_name(self, name: str):
        """Args: name (str): Новое имя."""
        try:
            if not name.strip():
                raise ValueError("Ошибка: Имя не может быть пустым.")
            self.__str_name = name
            print("Успешно обновлено.")
        except ValueError as e:
            print(e)

    def set_quantity(self, quantity: int):
        """Args: quantity (int): Новое количество."""
        try:
            if quantity < 0:
                raise ValueError("Ошибка: Количество не может быть отрицательным.")
            self.__int_quantity = quantity
            print("Количество обновлено.")
        except ValueError as e:
            print(e)

    def set_price(self, price: float):
        """Args: price (float): Новая цена."""
        try:
            if price <= 0:
                raise ValueError("Ошибка: Цена должна быть больше 0.")
            self.__float_price = price
            print("Цена обновлена.")
        except ValueError as e:
            print(e)

    def write_off(self):
        """Списание товара согласно схеме."""
        self.__int_quantity = 0
        self.__str_status = "списано"
        print("Товар успешно списан.")

    def __str__(self):
        return (f"\n--- КАРТОЧКА ТОВАРА ---\n"
                f"Артикул: {self.__int_article_number}\n"
                f"Наименование: {self.__str_name}\n"
                f"Количество: {self.__int_quantity}\n"
                f"Цена: {self.__float_price}\n"
                f"Статус: {self.__str_status}\n"
                f"-----------------------")


def run_ui():
    print("Добро пожаловать в систему складского учета!")
    
    item = ItemCard(1001, "Ноутбук", 5, "Секция 1", "Asus Store", "Asus", 75000.0, "Техника", "Laptops")

    while True:
        print("\nМЕНЮ УПРАВЛЕНИЯ:")
        print("1. Показать информацию о товаре")
        print("2. Изменить название")
        print("3. Изменить количество")
        print("4. Изменить цену")
        print("5. Списать товар")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            print(item)
        
        elif choice == "2":
            new_name = input("Введите новое название: ")
            item.set_name(new_name)
        
        elif choice == "3":
            try:
                new_qty = int(input("Введите новое количество: "))
                item.set_quantity(new_qty)
            except ValueError:
                print("Ошибка: Введите целое число для количества.")
        
        elif choice == "4":
            try:
                new_price = float(input("Введите новую цену: "))
                item.set_price(new_price)
            except ValueError:
                print("Ошибка: Введите число для цены.")
        
        elif choice == "5":
            try:
                confirm = input("Вы уверены, что хотите списать товар? (y/n): ")
                if confirm == 'y':
                    item.write_off()
            except ValueError:
                print('Неверный ввод, попробуйте снова.')

        
        elif choice == "0":
            print("Завершение работы...")
            break
        
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    run_ui()
