from typing import Iterable

from domain.entities.order import Order
from domain.exceptions.order_exceptions import OrderSeederException

from application.usecases.order.save import SaveOrderUseCase

from interfaces.repositories.order_repo import OrderRepository


class OrderSeeder:
    def __init__(self, order_repo: OrderRepository) -> None:
        """
        Description
        -----------
        Inicializa el servicio de Seeder para el módulo de ordenes

        Attributes
        ----------
        order_repo: OrderRepository
            Instancia del repositorio activo de persistencia
        """
        self.order_repo = order_repo
        self._save_uc = SaveOrderUseCase(order_repo)
    
    
    def seed(self, orders: Iterable[Order], ignore_errors: bool = True) -> None:
        """
        Description
        -----------
        Siembra la semilla con datos para las tablas asociadas
        a una Orden (orders y order_items)

        Attributes
        ----------
        orders : Iterable[Order]
            Arreglo de Ordenes a persistir
        ignore_errors: bool = True
            Mientras esté activa esta bandera, solo se alertan de los errores
            pero no se detiene la aplicación. En caso contrario, lanza una
            excepción.

        Raise
        -----
        OrderSeederException
            Si ocurre un error al poblar las ordenes.
        """
        for order in orders:
            try:
                self._save_uc.execute(order)
            except Exception as exc:
                if ignore_errors:
                    print(f"[OrderSeeder] No se pudo insertar el pedido {order.id}: {exc}")
                    continue
                raise OrderSeederException(f"Error al poblar las ordenes: {exc}")