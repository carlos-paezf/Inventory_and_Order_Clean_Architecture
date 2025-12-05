from typing import List
from abc import ABC, abstractmethod
from domain.entities.product import Product


class InventoryRepository(ABC):
    """
    Description
    -----------
    Clase abstracta que definen los métodos a implementar en cada repositorio
    asociado a la persistencia del inventario.
    """

    @abstractmethod
    def add_product(self, product: Product) -> None:
        """
        Description
        -----------
        Método abstracto para añadir productos en la persistencia.

        Attributes
        ----------
        product : Product
            Producto a registrar en la persistencia.
        """
        pass


    @abstractmethod
    def remove_product(self, product_id: str) -> bool:
        """
        Description
        -----------
        Método abstracto para eliminar un producto de la persistencia.

        Attributes
        ----------
        product_id : str
            Id del producto a eliminar.

        Returns
        -------
        bool
            Retorna True si el producto fue eliminado, False en caso contrario.
        """
        pass


    @abstractmethod
    def get_product(self, product_id: str) -> Product | None:
        """
        Description
        -----------
        Método abstracto para obtener un producto específico de la persistencia.

        Attributes
        ----------
        product_id : str
            Id del producto a buscar

        Returns
        -------
        Product | None
            Retorna el producto encontrado, o None en caso contrario.
        """
        pass


    @abstractmethod
    def list_products(self) -> List[Product]:
        """
        Description
        -----------
        Método abstracto para listar todos los productos de la base de datos

        Returns
        -------
        List[Product]
            Lista de productos guardados en la persistencia.
        """
        pass