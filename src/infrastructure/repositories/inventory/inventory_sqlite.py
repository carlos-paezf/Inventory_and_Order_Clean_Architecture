import sqlite3
from typing import Any, List
from domain.entities.product import AccessoryProduct, BookProduct, Product
from interfaces.repositories.inventory_repo import InventoryRepository


class InventorySQLiteRepository(InventoryRepository):
    def __init__(self, db_path: str = "database.db") -> None:
        self.conn = sqlite3.connect(db_path)
        self._create_table()
        

    def _create_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS products (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                price TEXT NOT NULL,
                category TEXT NOT NULL,
                author TEXT,
                brand TEXT
            )
        """
        self.conn.execute(query)
        self.conn.commit()


    def add_product(self, product: Product) -> None:
        query = """
            INSERT INTO products (id, name, price, category, author, brand) 
            VALUES (?, ?, ?, ?, ?, ?)
        """
        author = product.author if isinstance(product, BookProduct) else None
        brand = product.brand if isinstance(product, AccessoryProduct) else None

        try:
            self.conn.execute(
                query,
                (product.id, product.name, product.price, product.category, author, brand)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError(f"500 - Ha ocurrido un error al insertar el producto")


    def remove_product(self, product_id: str) -> bool:
        result = self.conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()
        return result.rowcount >= 0
        


    def get_product(self, product_id: str) -> Product | None:
        query = """
            SELECT id, name, price, category, author, brand
            FROM products
            WHERE id = ?
        """ 
        result = self.conn.execute(query, (product_id,))
        row = result.fetchone()
        
        return None if not row else self._map_result(row)


    def list_products(self) -> List[Product]:
        result = self.conn.execute("SELECT id, name, price, category, author, brand FROM products")
        rows = result.fetchall()

        return [
            self._map_result(row)
            for row in rows 
        ]


    def _map_result(self, row: Any):
        id, name, price, category, author, brand = row

        if category.lower() == "book":
            return BookProduct(id, name, float(price), category, author)
        elif category.lower() == "accessory":
            return AccessoryProduct(id, name, float(price), category, brand)
        else:
            return Product(id, name, float(price), category)