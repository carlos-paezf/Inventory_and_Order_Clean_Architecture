from typing import Dict, List

from domain.entities.product import Product
from domain.exceptions.inventory_exceptions import ProductAlreadyExistsError
from interfaces.repositories.inventory_repo import InventoryRepository


class InventoryMemoryRepository(InventoryRepository):
    """
    Description
    -----------
    Implementación del repositorio de inventario en memoria

    Attributes
    ----------
    _products : Dict[str, Product]
        Diccionario que almacena los productos en memoria
    """
    def __init__(self):
        """
        Description
        -----------
        Inicializa el repositorio en memoria
        """
        self._products: Dict[str, Product] = {}


    def add_product(self, product: Product) -> None:
        """
        Description
        -----------
        Agrega un producto al repositorio en memoria

        Attributes
        ----------
        product : Product
            Producto a agregar

        Raises
        ------
        ProductAlreadyExistsError
            Si el producto ya existe en el repositorio
        """
        if product.id in self._products:
            raise ProductAlreadyExistsError(product_id)
        self._products[product.id] = product


    def remove_product(self, product_id: str) -> bool:
        """
        Description
        -----------
        Elimina un producto del repositorio en memoria

        Attributes
        ----------
        product_id : str
            Identificador del producto a eliminar

        Returns
        -------
        bool
            True si se eliminó el producto, False si no se encontró.
        """
        if product_id not in self._products:
            return False
        else:
            del self._products[product_id]
            return True

    
    def get_product(self, product_id: str) -> Product | None:
        """
        Description
        -----------
        Obtiene un producto del repositorio en memoria

        Attributes
        ----------
        product_id : str
            Identificador del producto a obtener

        Returns
        -------
        Product | None
            Producto si se encuentra, None si no se encuentra.
        """
        return self._products.get(product_id) if product_id in self._products else None


    def list_products(self) -> List[Product]:
        """
        Description
        -----------
        Obtiene todos los productos del repositorio en memoria

        Returns
        -------
        List[Product]
            Lista de todos los productos.
        """
        return list(self._products.values())