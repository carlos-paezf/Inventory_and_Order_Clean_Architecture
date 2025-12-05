from domain.entities.order import Order
from domain.exceptions.order_exceptions import OrderError
from interfaces.repositories.order_repo import OrderRepository


class SaveOrderUseCase:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    
    def execute(self, order: Order):
        """
        Description
        -----------
        Ejecuta la persistencia de una orden.

        Attributes
        ----------
        order : Order
            Orden a persistir.
        """
        try:
            return self.order_repo.save(order)
        except Exception as e:
            raise OrderError(f"Error al guardar la orden con el id {order.id}: {e}")