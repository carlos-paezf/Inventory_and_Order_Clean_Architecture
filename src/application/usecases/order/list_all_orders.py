from domain.exceptions.order_exceptions import OrderError
from interfaces.repositories.order_repo import OrderRepository


class ListAllOrdersUseCase:
    def __init__(self, order_repo: OrderRepository):
        """
        Description
        -----------
        Inicializa el caso de uso con el repositorio de ordenes

        Attributes
        ----------
        order_repo : OrderRepository
            Repositorio de ordenes
        """
        self.order_repo = order_repo

    def execute(self):
        """
        Description
        -----------
        Lista todos los pedidos guardados en la persistencia
        """
        try:
            return self.order_repo.list_all()
        except Exception as e:
            raise OrderError(f"Error al listar todos los pedidos: {e}")