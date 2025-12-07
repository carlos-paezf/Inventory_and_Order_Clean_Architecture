from domain.entities.order import Order
from domain.exceptions.order_exceptions import OrderError
from interfaces.repositories.order_repo import OrderRepository


class GetOrderUseCase:
    def __init__(self, order_repo: OrderRepository):
        """
        Description
        -----------
        Inicializa el caso de uso Obtener orden.

        Attributes
        ----------
        order_repo : OrderRepository
            Instancia activa del repositorio.
        """
        self.order_repo = order_repo


    def execute(self, order_id: str) -> Order | None:
        """
        Description
        -----------
        Ejecuta el caso de uso Obtener orden.

        Attributes
        ----------
        order_id : str
            Identificador de la orden a obtener.
        
        Returns
        -------
        Order | None
            Retorna la orden si se encontró. None en caso contrario.
        """
        try:
            return self.order_repo.get(order_id)
        except Exception as e:
            raise OrderError(f"Error al obtener la orden con el id {order_id}: {e}")