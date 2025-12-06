from typing import List

from domain.entities.order import Order, OrderItem
from domain.entities.product import Product

from infrastructure.database.sqlite_connection import SQLiteConnection

from interfaces.adapters.product_factory import ProductFactory
from interfaces.repositories.order_repo import OrderRepository


class OrderSQLiteRepository(OrderRepository):
    def __init__(self) -> None:
        """
        Description
        -----------
        Inicializa el repositorio en SQLite
        """
        self.conn = SQLiteConnection().get_connection()
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
        result = self.conn.execute("DELETE FROM orders WHERE id = ?", (order_id,))
        self.conn.commit()
        return result.rowcount > 0
    
    
    def get(self, order_id: str) -> Order | None:
        """
        Description
        -----------
        Obtiene una orden de la base de datos SQLite

        Attributes
        ----------
        order_id : str
            Identificador de la orden a obtener

        Returns
        -------
        Order | None
            Orden si se encuentra, None si no se encuentra.
        """
        result = self.conn.execute("SELECT id FROM orders WHERE id = ?", (order_id,))
        row = result.fetchone()

        if not row:
            return None
        
        items_result = self.conn.execute(
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
            WHERE oi.order_id = ?
            """,
            (order_id,)
        )


        items = []
        for item_row in items_result.fetchall():
            product = self._map_product(item_row)
            items.append(OrderItem(product, item_row[1]))

        order = Order(id=row[0], items=items)
        return order

    
    def list_all(self) -> List[Order]:
        """
        Description
        -----------
        Obtiene todas las ordenes de la base de datos

        Returns
        -------
        List[Order]
            Lista de todas las ordenes
        """
        result = self.conn.execute("SELECT id FROM orders")
        orders = []
        for (order_id, ) in result.fetchall():
            order = self.get(order_id)
            if order is not None:
                orders.append(order)
        return orders
        

    def _map_product(self, row: any) -> Product:
        """
        Description
        -----------
        Mapea un producto de la base de datos a un objeto Product

        Attributes
        ----------
        row : any
            Resultado de la consulta a la base de datos

        Returns
        -------
        Product
            Producto mapeado
        """
        product_id, _, product_name, price, category, author, brand = row

        return ProductFactory.create_product(
            kind=category, id=product_id, name=product_name, price=float(price), author=author, brand=brand
        )