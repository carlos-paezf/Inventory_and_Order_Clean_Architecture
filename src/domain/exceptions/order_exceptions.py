class OrderNotFoundError(Exception):
    def __init__(self, order_id: str) -> None:
        """
        Description
        -----------
        Excepción lanzada cuando no se encuentra una orden con el id especificado.

        Attributes
        ----------
        order_id : str
            Id de la orden que no se encontró.
        """
        self.order_id = order_id
        super().__init__(f"La orden con el id {order_id} no fue encontrado")


class OrderAlreadyExists(Exception):
    def __init__(self, order_id: str) -> None:
        """
        Description
        -----------
        Excepción lanzada cuando se intenta agregar una orden que ya existe.

        Attributes
        ----------
        order_id : str
            Id del producto que ya existe.
        """
        self.order_id = order_id
        super().__init__(f"La orden con el id {order_id} ya existe")


class OrderError(Exception):
    """
    Description
    -----------
    Excepción lanzada cuando ocurre un error al manejar una orden.
    """
    pass