import sqlite3
from typing import List
from domain.entities.order import Order
from domain.entities.product import AccessoryProduct, BookProduct, Product
from interfaces.repositories.order_repo import OrderRepository


class OrderSQLiteRepository(OrderRepository):
    def __init__(self, db_path: str = "database.db") -> None:
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self) -> None:
        """
        Description
        -----------
        Crea las tablas necesarias para la persistencia de ordenes

        Attributes
        ----------
        None
        """
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id TEXT PRIMARY KEY
            )
            """
        )
        self.conn.commit()
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS order_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id TEXT,
                product_id TEXT,
                quantity INTEGER,
                FOREIGN KEY (order_id) REFERENCES orders(id),
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
            """
        )
        self.conn.commit()

    
    def save(self, order: Order) -> None:
        """
        Description
        -----------
        Guarda una orden en la base de datos SQLite

        Attributes
        ----------
        order : Order
            Orden a guardar
        """
        self.conn.execute("INSERT OR REPLACE INTO orders (id) VALUES (?)", (order.id,))
        self.conn.commit()

        self.conn.execute("DELETE FROM order_items WHERE order_id = ?", (order.id,))

        for item in order.items:
            self.conn.execute(
                """
                INSERT INTO order_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
                """,
                (order.id, item.product.id, item.quantity,)
            )
            self.conn.commit()

    
    def delete(self, order_id: str) -> bool:
        """
        Description
        -----------
        Elimina una orden y los items asociados a la misma

        Attributes
        ----------
        order_id : str
            Identificador de la orden a eliminar

        Returns
        bool
            True si se aplicó la eliminación, 
            False si no se encontró la orden a eliminar.
        """
        self.conn.execute("DELETE FROM order_items WHERE order_id = ?", (order_id,))
        result = self.con.execute("DELETE FROM orders WHERE id = ?", (order_id,))
        self.conn.commit()
        return result.rowcount >= 0
    
    
    def get(self, order_id: str) -> List[Order]:
        result = self.conn.execute("SELECT id FROM orders WHERE id = ?", (order_id,))
        row = result.fetchone()
        if not row:
            raise ValueError(f"404 - La orden con el id {order_id} no fue encontrada")

        order = Order(id=row[0])
        items = self.conn.execute(
            """
            SELECT 
                oi.product_id, 
                oi.quantity,
                p.name,
                p.price,
                p.category,
                p.author,
                p.brand
            FROM order_items oi
            INNER JOIN products p ON oi.product_id = p.id
            WHERE order_id = ?
            """,
            (order_id,)
        )

        for row in items.fetchall():
            print(row)
            product = self._map_product(row)
            order.add_item(product, quantity=row[1])

        return order

    
    def list_all(self) -> List[Order]:
        result = self.conn.execute("SELECT id FROM orders")
        orders = []
        for (order_id, ) in result.fetchall():
            orders.append(self.get(order_id))
        return orders
        

    def _map_product(row: any) -> Product:
        product_id, _, product_name, price, category, author, brand = row

        if category.lower() == "book":
            product = BookProduct(product_id, product_name, float(price), category, author)
        elif category.lower() == "accessory":
            product = AccessoryProduct(product_id, product_name, float(price), category, brand)
        else:
            product = Product(product_id, product_name, float(price), category)
        
        return product