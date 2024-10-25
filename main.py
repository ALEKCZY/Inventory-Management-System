import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


# Класс для работы с базой данных
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


# Класс для работы с таблицей Products
class Product:
    def __init__(self, db):
        self.db = db

    def add_product(self, product_name, unit_price, category):
        query = "INSERT INTO Products (ProductName, UnitPrice, Category) VALUES (?, ?, ?)"
        self.db.execute(query, (product_name, unit_price, category))

    def get_all_products(self):
        query = "SELECT * FROM Products"
        return self.db.fetchall(query)

    def delete_product(self, product_id):
        query = "DELETE FROM Products WHERE ProductID = ?"
        self.db.execute(query, (product_id,))


# Класс для работы с таблицей House
class House:
    def __init__(self, db):
        self.db = db

    def get_all_houses(self):
        query = "SELECT * FROM House"
        return self.db.fetchall(query)


# Класс для работы с таблицей Operation
class Operation:
    def __init__(self, db):
        self.db = db

    def get_all_operations(self):
        query = "SELECT * FROM Operations"
        return self.db.fetchall(query)


# Класс для интерфейса приложения
class InventoryApp:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.product = Product(self.db)
        self.house = House(self.db)
        self.operation = Operation(self.db)

        self.root.title("Inventory Management")
        self.setup_ui()
        self.show_products()

    def setup_ui(self):
        button_font = ("Arial", 14)
        self.tree = ttk.Treeview(self.root, show="headings")
        self.tree.grid(row=0, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")
        self.button_add_product = tk.Button(self.root, text="Добавить товар", font=button_font,
                                            command=self.add_product_window)
        self.button_add_product.grid(row=1, column=0, padx=10, pady=10)
        self.button_delete_product = tk.Button(self.root, text="Удалить товары", font=button_font,
                                               command=self.delete_product)
        self.button_delete_product.grid(row=1, column=1, padx=10, pady=10)
        self.button_show_products = tk.Button(self.root, text="Показать товары", font=button_font,
                                              command=self.show_products)
        self.button_show_products.grid(row=1, column=2, padx=10, pady=10)
        self.button_show_houses = tk.Button(self.root, text="Показать склады", font=button_font, command=self.show_houses)
        self.button_show_houses.grid(row=1, column=3, padx=10, pady=10)
        self.button_show_operations = tk.Button(self.root, text="Показать операции", font=button_font,
                                                command=self.show_operations)
        self.button_show_operations.grid(row=1, column=4, padx=10, pady=10)

    def add_product_window(self):
        # Окно добавления продукта
        new_window = tk.Toplevel(self.root)
        new_window.title("Добавить товар")

        label_font = ("Arial", 14)

        tk.Label(new_window, text="Название товара", font=label_font).grid(row=0, column=0, padx=10, pady=10)
        entry_product_name = tk.Entry(new_window)
        entry_product_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(new_window, text="Цена", font=label_font).grid(row=1, column=0, padx=10, pady=10)
        entry_unit_price = tk.Entry(new_window)
        entry_unit_price.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(new_window, text="Категория", font=label_font).grid(row=2, column=0, padx=10, pady=10)
        entry_category = tk.Entry(new_window)
        entry_category.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(new_window, text="Добавить", command=lambda: self.add_product(entry_product_name, entry_unit_price, entry_category, new_window)).grid(row=3, column=0, columnspan=2, pady=10)

    def add_product(self, entry_product_name, entry_unit_price, entry_category, window):
        product_name = entry_product_name.get()
        unit_price = entry_unit_price.get()
        category = entry_category.get()

        if product_name and unit_price and category:
            self.product.add_product(product_name, unit_price, category)
            messagebox.showinfo("Успех", "Товар успешно добавлен!")
            window.destroy()
            self.show_products()
        else:
            messagebox.showwarning("Ошибка ввода", "Пожалуйста заполните все поля")

    def clear_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def configure_tree_for_products(self):
        # Настроить столбцы для продуктов
        self.tree["columns"] = ("ProductID", "ProductName", "UnitPrice", "Category")
        self.tree.heading("ProductID", text="ID")
        self.tree.heading("ProductName", text="Название товара")
        self.tree.heading("UnitPrice", text="Цена")
        self.tree.heading("Category", text="Категория")

    def configure_tree_for_houses(self):
        # Настроить столбцы для складов
        self.tree["columns"] = ("HouseID", "Name", "Location")
        self.tree.heading("HouseID", text="ID")
        self.tree.heading("Name", text="Название")
        self.tree.heading("Location", text="Локация")

    def configure_tree_for_operations(self):
        # Настроить столбцы для операций
        self.tree["columns"] = ("OperationID", "ProductID", "HouseID", "TypeOperation", "Kol")
        self.tree.heading("OperationID", text="ID")
        self.tree.heading("ProductID", text="ID Товара")
        self.tree.heading("HouseID", text="ID Склада")
        self.tree.heading("TypeOperation", text="Тип")
        self.tree.heading("Kol", text="Количество")

    def show_products(self):
        self.clear_table()
        self.configure_tree_for_products()
        products = self.product.get_all_products()
        for product in products:
            self.tree.insert("", "end", values=product)

    def delete_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item)["values"][0]
            self.product.delete_product(product_id)
            messagebox.showinfo("Успех", "Товар успешно удален!")
            self.show_products()
        else:
            messagebox.showwarning("Ошибка выбора", "Пожалуйста выделите товар для удаления")

    def show_houses(self):
        self.clear_table()
        self.configure_tree_for_houses()
        houses = self.house.get_all_houses()
        for house in houses:
            self.tree.insert("", "end", values=house)

    def show_operations(self):
        self.clear_table()
        self.configure_tree_for_operations()
        operations = self.operation.get_all_operations()
        for operation in operations:
            self.tree.insert("", "end", values=operation)


# Основной запуск программы
if __name__ == "__main__":
    db = Database('inventorySystem.db')
    root = tk.Tk()
    root.state('zoomed')

    app = InventoryApp(root, db)
    root.mainloop()
    db.close()
