import sqlite3
import tkinter as tk
from tkinter import messagebox


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


# Класс для работы с таблицей House
class House:
    def __init__(self, db):
        self.db = db

    def add_house(self, name, location):
        query = "INSERT INTO House (Name, Location) VALUES (?, ?)"
        self.db.execute(query, (name, location))

    def get_all_houses(self):
        query = "SELECT * FROM House"
        return self.db.fetchall(query)


# Класс для работы с таблицей Operation
class Operation:
    def __init__(self, db):
        self.db = db

    def add_operation(self, product_id, house_id, type_operation, kol):
        query = "INSERT INTO Operation (ProductID, HouseID, TypeOperation, Kol) VALUES (?, ?, ?, ?)"
        self.db.execute(query, (product_id, house_id, type_operation, kol))

    def get_all_operations(self):
        query = "SELECT * FROM Operation"
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

        # Интерфейс для добавления продуктов
        self.label_product = tk.Label(root, text="Product Name")
        self.label_product.grid(row=0, column=0)
        self.entry_product_name = tk.Entry(root)
        self.entry_product_name.grid(row=0, column=1)

        self.label_price = tk.Label(root, text="Unit Price")
        self.label_price.grid(row=1, column=0)
        self.entry_unit_price = tk.Entry(root)
        self.entry_unit_price.grid(row=1, column=1)

        self.label_category = tk.Label(root, text="Category")
        self.label_category.grid(row=2, column=0)
        self.entry_category = tk.Entry(root)
        self.entry_category.grid(row=2, column=1)

        self.button_add_product = tk.Button(root, text="Add Product", command=self.add_product)
        self.button_add_product.grid(row=3, column=0, columnspan=2)

        # Кнопка для отображения всех продуктов
        self.button_show_products = tk.Button(root, text="Show All Products", command=self.show_products)
        self.button_show_products.grid(row=4, column=0, columnspan=2)

    def add_product(self):
        product_name = self.entry_product_name.get()
        unit_price = self.entry_unit_price.get()
        category = self.entry_category.get()

        if product_name and unit_price and category:
            self.product.add_product(product_name, unit_price, category)
            messagebox.showinfo("Success", "Product added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def show_products(self):
        products = self.product.get_all_products()
        products_list = "\n".join([f"{p[1]} - {p[2]} - {p[3]}" for p in products])
        messagebox.showinfo("All Products", products_list)


# Основной запуск программы
if __name__ == "__main__":
    db = Database('InventorySQL.db')  # Указываем название вашей базы данных
    root = tk.Tk()
    app = InventoryApp(root, db)
    root.mainloop()
    db.close()
