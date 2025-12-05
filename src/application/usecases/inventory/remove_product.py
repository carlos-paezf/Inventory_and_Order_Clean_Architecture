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

    def execute(self, product_id: str):
        """
        Description
        -----------
        Caso de uso agnóstico para eliminar un producto de la persistencia. 
        Se hace uso del repositorio para ejecutar una función específica.

        Attributes
        ----------
        product_id : str
            Id del producto a eliminar de la persistencia.

        Raises
        ------
        ValueError
            Si ocurre un error al eliminar el producto.
        """
        try:
            if self.inventory_repo.remove_product(product_id):
                print("200 - El producto ha sido eliminado correctamente")
            else:
                print(f"404 - El producto con el id {product_id} no fue encontrado")
        except ValueError as e:
            print(f"500 - Ha ocurrido un error al eliminar el producto: {e}")