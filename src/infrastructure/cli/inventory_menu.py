import random

from application.usecases.inventory.add_product import AddProductUseCase
from application.usecases.inventory.get_product import GetProductUseCase
from application.usecases.inventory.list_products import ListProductsUseCase
from application.usecases.inventory.remove_product import RemoveProductUseCase

from interfaces.cli.console_utils import (
    GREEN, MAGENTA, RESET, pause, show_menu_options, read_option
)
from interfaces.repositories.inventory_repo import InventoryRepository

from demo.mocks.products import MOCKS_PRODUCTS


class InventoryMenu:
    def __init__(self, inventory_repo: InventoryRepository) -> None:
        self.inventory_repo = inventory_repo

    def run(self) -> None:
        while True:
            print(
                f"{GREEN}\nTe presentamos las acciones disponibles para el inventario:"
                f"{RESET} (Selecciona una opción)"
            )

            options = [
                "Añadir productos al inventario",
                "Consultar producto del inventario",
                "Listar todos los productos del inventario",
                "Eliminar producto del inventario",
                "Volver al menú principal",
            ]

            show_menu_options(options, exit_label="Salir de la demo")
            option = read_option(len(options))

            if option == 1:
                self._add_random_product()
            elif option == 2:
                self._get_product()
            elif option == 3:
                self._list_products()
            elif option == 4:
                self._remove_product()
            elif option == 5:
                return

            print("\n", "-" * 100)
            pause()


    def _add_random_product(self) -> None:
        random_product = random.choice(MOCKS_PRODUCTS)
        AddProductUseCase(self.inventory_repo).execute(random_product)
        print(f"{GREEN}\nCaso de uso `Añadir producto` ha sido ejecutado{RESET}")


    def _get_product(self) -> None:
        product_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id del producto a consultar: "
        )
        GetProductUseCase(self.inventory_repo).execute(product_id)
        print(f"{GREEN}\nCaso de uso `Obtener producto` ha sido ejecutado{RESET}")


    def _list_products(self) -> None:
        ListProductsUseCase(self.inventory_repo).execute()
        print(f"{GREEN}\nCaso de uso `Listar productos` ha sido ejecutado{RESET}")

        
    def _remove_product(self) -> None:
        product_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id del producto a eliminar: "
        )
        RemoveProductUseCase(self.inventory_repo).execute(product_id)
        print(f"{GREEN}\nCaso de uso `Remover producto` ha sido ejecutado{RESET}")
