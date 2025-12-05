from domain.exceptions.order_exceptions import OrderError
from interfaces.repositories.order_repo import OrderRepository


class GetOrderUseCase:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    def execute(self, order_id: str):
        try:
            return self.order_repo.get(order_id)
        except Exception as e:
            raise OrderError(f"Error al obtener la orden con el id {order_id}: {e}")