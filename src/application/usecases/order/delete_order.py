from domain.exceptions.order_exceptions import OrderError
from interfaces.repositories.order_repo import OrderRepository


class DeleteOrderUseCase:
    def __init__(self, order_repo: OrderRepository):
        """
        Description
        -----------
        Inicializa el caso de uso Eliminar orden

        Attributes
        ----------
        order_repo : OrderRepository
            Instancia activa del repositorio.
        """
        self.order_repo = order_repo


    def execute(self, order_id: str) -> bool:
        """
        Description
        -----------
        Ejecuta la eliminación de una orden si existe,
        en caso contrario lanza un mensaje de error.

        Attributes
        ----------
        order_id : str
            Id de la orden a eliminar.

        Returns
        -------
        bool
            True si la orden fue eliminada, False si no.

        Raise
        -----
        OrderNotFoundError
            Si la orden no existe.
        OrderError
            Si ocurre un error al eliminar la orden.
        """
        try:
            return self.order_repo.delete(order_id)
        except Exception as e:
            raise OrderError(f"Error al eliminar el pedido con el id {order_id}: {e}")