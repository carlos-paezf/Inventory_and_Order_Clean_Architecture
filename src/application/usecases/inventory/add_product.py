from domain.entities.product import Product
from interfaces.repositories.inventory_repo import InventoryRepository


class AddProductUseCase:
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


    def execute(self, product: Product):
        """
        Description
        -----------
        Caso de uso agnóstico para añadir un producto en la persistencia. 
        Se hace uso del repositorio para ejecutar una función específica.

        Attributes
        ----------
        product : Product
            Producto a registrar en la persistencia.
        """
        self.inventory_repo.add_product(product)
        print(f"200 - El producto [{product}] ha sido añadido correctamente")