class InventorySeederException(Exception):
    """
    Description
    -----------
    Excepción lanzada cuando ocurre un error al poblar el inventario.
    """
    pass


class ProductNotFoundError(Exception):
    def __init__(self, product_id: str) -> None:
        """
        Description
        -----------
        Excepción lanzada cuando no se encuentra un producto con el id especificado.

        Attributes
        ----------
        product_id : str
            Id del producto que no se encontró.
        """
        self.product_id = product_id
        super().__init__(f"El producto con el id {product_id} no fue encontrado")


class ProductAlreadyExistsError(Exception):
    def __init__(self, product_id: str) -> None:
        """
        Description
        -----------
        Excepción lanzada cuando se intenta agregar un producto que ya existe.

        Attributes
        ----------
        product_id : str
            Id del producto que ya existe.
        """
        self.product_id = product_id
        super().__init__(f"El producto con el id {product_id} ya existe")


class InventoryError(Exception):
    """
    Description
    -----------
    Excepción lanzada cuando ocurre un error al manejar el inventario.
    """
    pass