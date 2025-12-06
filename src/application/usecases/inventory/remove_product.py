from domain.exceptions.inventory_exceptions import ProductNotFoundError
from interfaces.repositories.inventory_repo import InventoryRepository


class RemoveProductUseCase:
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


    def execute(self, product_id: str) -> bool:
        """
        Description
        -----------
        Caso de uso agnóstico para eliminar un producto de la persistencia. 
        Se hace uso del repositorio para ejecutar una función específica.

        Attributes
        ----------
        product_id : str
            Id del producto a eliminar de la persistencia.

        Returns
        -------
        bool
            Retorna True si el producto fue eliminado, False en caso contrario.

        Raises
        ------
        ValueError
            Si ocurre un error al eliminar el producto.
        """
        try:
            return self.inventory_repo.remove_product(product_id)
        except ProductNotFoundError as e:
            raise ProductNotFoundError(e.product_id)
        except ValueError as e:
            raise InventoryError(str(e))