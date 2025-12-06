from domain.entities.product import Product
from interfaces.repositories.inventory_repo import InventoryRepository


class GetProductUseCase:
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


    def execute(self, product_id: str) -> Product | None:
        """
        Description
        -----------
        Caso de uso agnóstico para obtener un producto de la persistencia. 
        Se hace uso del repositorio para ejecutar una función específica.

        Attributes
        ----------
        product_id : str
            Id del producto a buscar en la persistencia.

        Returns
        -------
        Product | None
            En caso de encontrar un registro, retorna un producto.
            En caso contrario retorna None
        """
        try:
            return self.inventory_repo.get_product(product_id)
        except Exception as e:
            raise InventoryError(str(e))