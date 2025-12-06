from typing import List
from domain.entities.product import Product
from interfaces.repositories.inventory_repo import InventoryRepository


class ListProductsUseCase:
    def __init__(self, inventory_repo: InventoryRepository):
        """
        Description
        -----------
        Constructor del caso de uso.

        Attributes
        ----------
        inventory_repo : InventoryRepository
            Se inyecta la instancia del repositorio que está funcionando en la aplicación.
        """
        self.inventory_repo = inventory_repo

    def execute(self) -> List[Product]:
        """
        Description
        -----------
        Caso de uso agnóstico para añadir un producto en la persistencia. 
        Se hace uso del repositorio para ejecutar una función específica.

        Returns
        -------
        List[Product]
            Retorna una lista de productos.
        """
        try:
            return self.inventory_repo.list_products()
        except Exception as e:
            raise InventoryError(str(e))