from domain.exceptions.order_exceptions import OrderError, OrderNotFoundError
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


    def execute(self, order_id: str) -> None:
        """
        Description
        -----------
        Ejecuta la eliminación de una orden si existe,
        en caso contrario lanza un mensaje de error.

        Raise
        -----
        OrderNotFoundError
            Si la orden no existe.
        OrderError
            Si ocurre un error al eliminar la orden.
        """
        try:
            deleted = self.order_repo.delete(order_id)
            if not deleted:
                raise OrderNotFoundError(f"La orden con el id {order_id} no existe")
        except Exception as e:
            raise OrderError(f"Error al eliminar el pedido con el id {order_id}: {e}")