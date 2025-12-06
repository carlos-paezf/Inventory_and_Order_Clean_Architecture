import random

from application.usecases.order.list_all import ListAllOrdersUseCase
from application.usecases.order.save import SaveOrderUseCase
from application.usecases.order.delete import DeleteOrderUseCase
from application.usecases.order.get import GetOrderUseCase

from demo.mocks.orders import MOCKS_ORDERS
from interfaces.cli.console_utils import (
    GREEN, RESET,
    pause, show_menu_options, read_option
)
from interfaces.repositories.order_repo import OrderRepository


class OrderMenu:
    def __init__(self, order_repo: OrderRepository) -> None:
        self.order_repo = order_repo

    def run(self) -> None:
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
        random_order = random.choice(MOCKS_ORDERS)
        SaveOrderUseCase(self.order_repo).execute(random_order)
        print(f"{GREEN}\nCaso de uso `Guardar Orden` ha sido ejecutado{RESET}")


    def _get_order(self) -> None:
        order_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id de la orden a consultar: "
        )
        GetOrderUseCase(self.order_repo).execute(order_id)
        print(f"{GREEN}\nCaso de uso `Obtener Orden` ha sido ejecutado{RESET}")


    def _list_orders(self) -> None:
        ListAllOrdersUseCase(self.order_repo).execute()
        print(f"{GREEN}\nCaso de uso `Listar Ordenes` ha sido ejecutado{RESET}")


    def _delete_order(self) -> None:
        order_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id de la orden a eliminar: "
        )
        DeleteOrderUseCase(self.order_repo).execute(order_id)
        print(f"{GREEN}\nCaso de uso `Eliminar Orden` ha sido ejecutado{RESET}")
