import sqlite3
from typing import Any, List

from domain.entities.product import AccessoryProduct, BookProduct, Product
from domain.exceptions.inventory_exceptions import InventoryError, ProductAlreadyExistsError

from infrastructure.database.sqlite_connection import SQLiteConnection

from interfaces.adapters.product_factory import ProductFactory
from interfaces.repositories.inventory_repo import InventoryRepository


class InventorySQLiteRepository(InventoryRepository):
    """
    Description
    -----------
    Clase que representa el repositorio de inventario en SQLite
    """
    def __init__(self) -> None:
        """
        Description
        -----------
        Inicializa el repositorio en SQLite
        """
        self.conn = SQLiteConnection().get_connection()
        self._create_table()
        

    def _create_table(self) -> None:
        """
        Description
        -----------
        Crea la tabla de productos en SQLite
        """
        query = """
            CREATE TABLE IF NOT EXISTS products (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                category TEXT NOT NULL,
                author TEXT,
                brand TEXT
            )
        """
        self.conn.execute(query)
        self.conn.commit()


    def add_product(self, product: Product) -> None:
        """
        Description
        -----------
        Inserta un producto en la tabla de productos

        Attributes
        ----------
        product : Product
            Producto a insertar

        Raise
        -----
        ProductAlreadyExistsError
            Excepción lanzada cuando se intenta insertar un producto que ya existe.
        InventoryError
            Excepción lanzada cuando ocurre un error al insertar el producto.
        """
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
            raise ProductAlreadyExistsError(product.id)
        except Exception as e:
            raise InventoryError(str(e))


    def remove_product(self, product_id: str) -> bool:
        """
        Description
        -----------
        Elimina un producto de la tabla de productos

        Attributes
        ----------
        product_id : str
            Id del producto a eliminar

        Returns
        -------
        bool
            Retorna True si el producto fue eliminado, False en caso contrario.

        Raise
        -----
        ProductNotFoundError
            Excepción lanzada cuando no se encuentra un producto con el id especificado.
        """
        result = self.conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()
        return result.rowcount > 0
        


    def get_product(self, product_id: str) -> Product | None:
        """
        Description
        -----------
        Obtiene un producto de la tabla de productos

        Attributes
        ----------
        product_id : str
            Id del producto a obtener

        Returns
        -------
        Product | None
            Retorna el producto si se encuentra, None en caso contrario.
        """
        query = """
            SELECT id, name, price, category, author, brand
            FROM products
            WHERE id = ?
        """ 
        result = self.conn.execute(query, (product_id,))
        row = result.fetchone()
        
        return None if not row else self._map_result(row)


    def list_products(self) -> List[Product]:
        """
        Description
        -----------
        Obtiene todos los productos de la tabla de productos

        Returns
        -------
        List[Product]
            Retorna una lista de productos.
        """
        result = self.conn.execute("SELECT id, name, price, category, author, brand FROM products")
        rows = result.fetchall()

        return [
            self._map_result(row)
            for row in rows 
        ]


    def _map_result(self, row: Any) -> Product:
        """
        Description
        -----------
        Mapea un resultado de la tabla de productos a un objeto Product

        Attributes
        ----------
        row : Any
            Resultado de la consulta a la tabla de productos

        Returns
        -------
        Product
            Retorna el producto mapeado.
        """
        id, name, price, category, author, brand = row

        return ProductFactory().create_product(
            kind=category, id=id, name=name, price=float(price), author=author, brand=brand
        )