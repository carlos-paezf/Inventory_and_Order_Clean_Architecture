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

    def execute(self):
        """
        Description
        -----------
        Caso de uso agnóstico para añadir un producto en la persistencia. 
        Se hace uso del repositorio para ejecutar una función específica.
        """
        products = self.inventory_repo.list_products()
        print(f"200 - Listado de productos guardados en la persistencia")
        for i, product in enumerate(products):
            print(f"\t{i+1}. {product}")