import random

from application.usecases.order.list_all_orders import ListAllOrdersUseCase
from application.usecases.order.save_order import SaveOrderUseCase
from application.usecases.order.delete_order import DeleteOrderUseCase
from application.usecases.order.get_order import GetOrderUseCase

from domain.entities.order import Order
from infrastructure.cli.console_utils import (
    GREEN, MAGENTA, RESET, capture_order,
    pause, show_menu_options, read_option
)

from demo.mocks.orders import MOCKS_ORDERS
from interfaces.repositories.inventory_repo import InventoryRepository
from interfaces.repositories.order_repo import OrderRepository


class OrderMenu:
    """
    Description
    -----------
    Clase que gestiona el menú de las ordenes.

    Attributes
    ----------
    order_repo : OrderRepository
        Repositorio de ordenes.
    """
    
    def __init__(self, order_repo: OrderRepository, inventory_repo: InventoryRepository) -> None:
        """
        Description
        -----------
        Inicializa el menú de las ordenes.

        Parameters
        ----------
        order_repo : OrderRepository
            Repositorio de ordenes.
        """
        self.order_repo = order_repo
        self.inventory_repo = inventory_repo


    def run(self) -> None:
        """
        Description
        -----------
        Ejecuta el menú de las ordenes.
        """
        while True:
            print(
                f"{GREEN}\nTe presentamos las acciones disponibles para las ordenes:"
                f"{RESET} (Selecciona una opción)"
            )

            options = [
                "Crear nueva orden",
                "Consultar orden existente",
                "Listar todas las ordenes",
                "Eliminar una orden",
                "Volver al menú principal",
            ]

            show_menu_options(options, exit_label="Salir de la demo")
            option = read_option(len(options))

            if option == 1:
                self._create_order()
            elif option == 2:
                self._get_order()
            elif option == 3:
                self._list_orders()
            elif option == 4:
                self._delete_order()
            elif option == 5:
                return

            print("\n", "-" * 100)
            pause()


    def _create_order(self) -> None:
        """
        Description
        -----------
        Ejecuta el caso de uso `Guardar Orden`.
        """
        order = capture_order(self.inventory_repo)
        SaveOrderUseCase(self.order_repo).execute(order)
        print(f"La orden {order.id} ha sido guardada con éxito")
        print(f"{GREEN}\nCaso de uso `Guardar Orden` ha sido ejecutado{RESET}")


    def _get_order(self) -> None:
        """
        Description
        -----------
        Ejecuta el caso de uso `Obtener Orden`.
        """
        order_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id de la orden a consultar: "
        )
        order = GetOrderUseCase(self.order_repo).execute(order_id)
        print(order if order else f"No se encontró la orden con el id {order_id}")
        print(f"{GREEN}\nCaso de uso `Obtener Orden` ha sido ejecutado{RESET}")


    def _list_orders(self) -> None:
        """
        Description
        -----------
        Ejecuta el caso de uso `Listar Ordenes`.
        """
        orders = ListAllOrdersUseCase(self.order_repo).execute()
        if len(orders) == 0:
            print("No se encontraron ordenes")
        else:
            for order in orders:
                print(order, end="\n\n")
        print(f"{GREEN}\nCaso de uso `Listar Ordenes` ha sido ejecutado{RESET}")


    def _delete_order(self) -> None:
        """
        Description
        -----------
        Ejecuta el caso de uso `Eliminar Orden`.
        """
        order_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id de la orden a eliminar: "
        )
        deleted = DeleteOrderUseCase(self.order_repo).execute(order_id)
        if deleted:
            print(f"La orden {order_id} ha sido eliminada con éxito")
        else:
            print(f"No se encontró la orden con el id {order_id}")
        print(f"{GREEN}\nCaso de uso `Eliminar Orden` ha sido ejecutado{RESET}")
