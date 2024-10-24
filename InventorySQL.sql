--
-- ���� ������������ � ������� SQLiteStudio v3.4.4 � �� ��� 24 15:57:37 2024
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: House
CREATE TABLE IF NOT EXISTS House (HouseID INTEGER NOT NULL PRIMARY KEY, Name TEXT (255) NOT NULL, Location TEXT (255) NOT NULL);
INSERT INTO House (HouseID, Name, Location) VALUES (228, 'WR', '����� ������ 98');
INSERT INTO House (HouseID, Name, Location) VALUES (666, 'Warp', '���������� 32');
INSERT INTO House (HouseID, Name, Location) VALUES (1337, 'Pudge', '����������� 1');

-- �������: Operations
CREATE TABLE IF NOT EXISTS Operations (OperationID INTEGER PRIMARY KEY NOT NULL, productID INTEGER REFERENCES Products (ProductID) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, houseID INTEGER REFERENCES House (HouseID) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, TypeOperation TEXT NOT NULL, Kol TEXT (255) NOT NULL);
INSERT INTO Operations (OperationID, productID, houseID, TypeOperation, Kol) VALUES (21, 11, 666, '������', '25');
INSERT INTO Operations (OperationID, productID, houseID, TypeOperation, Kol) VALUES (22, 16, 1337, '������', '2');
INSERT INTO Operations (OperationID, productID, houseID, TypeOperation, Kol) VALUES (23, 17, 228, '������', '5');
INSERT INTO Operations (OperationID, productID, houseID, TypeOperation, Kol) VALUES (24, 13, 666, '������', '50');

-- �������: Products
CREATE TABLE IF NOT EXISTS Products (ProductID INTEGER PRIMARY KEY NOT NULL, ProductName TEXT (255) NOT NULL, UnitPrice REAL NOT NULL, Category TEXT (100) NOT NULL);
INSERT INTO Products (ProductID, ProductName, UnitPrice, Category) VALUES (11, '������', 70.0, '��������');
INSERT INTO Products (ProductID, ProductName, UnitPrice, Category) VALUES (12, '����', 36.0, '��������');
INSERT INTO Products (ProductID, ProductName, UnitPrice, Category) VALUES (13, '�������', 89.0, '��������');
INSERT INTO Products (ProductID, ProductName, UnitPrice, Category) VALUES (14, '�����', 189.0, '�������');
INSERT INTO Products (ProductID, ProductName, UnitPrice, Category) VALUES (15, '�����', 45.0, '�������');
INSERT INTO Products (ProductID, ProductName, UnitPrice, Category) VALUES (16, '��-74�', 5000.0, '�������');
INSERT INTO Products (ProductID, ProductName, UnitPrice, Category) VALUES (17, 'Mauzer', 2500.0, '�������');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
