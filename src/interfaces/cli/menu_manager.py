from application.seed.inventory_seeder import InventorySeeder
from application.seed.order_seeder import OrderSeeder

from demo.mocks.orders import MOCKS_ORDERS
from demo.mocks.products import MOCKS_PRODUCTS

from infrastructure.repositories.inventory.inventory_memory import InventoryMemoryRepository
from infrastructure.repositories.inventory.inventory_sqlite import InventorySQLiteRepository
from infrastructure.repositories.order.order_memory import OrderMemoryRepository
from infrastructure.repositories.order.order_sqlite import OrderSQLiteRepository

from interfaces.cli.console_utils import (
    GREEN, BLUE, RESET,
    show_menu_options, read_option,
)
from interfaces.cli.inventory_menu import InventoryMenu
from interfaces.cli.order_menu import OrderMenu
from interfaces.repositories.inventory_repo import InventoryRepository
from interfaces.repositories.order_repo import OrderRepository



class MenuManager:
    EXIT_OPTION = 0

    def __init__(self):
        self.inventory_repo: InventoryRepository = None
        self.order_repo: OrderRepository = None


    def run(self) -> None:
        self._print_welcome()
        self._select_persistence()
        self._execute_seed()
        self._main_menu_loop()

    
    def _execute_seed(self):
        print("Ejecución de Seed (Selecciona una opción):")
        
        options = [
            "Ejecutar Seed",
            "No ejecutar",
        ]

        show_menu_options(options)
        option = read_option(len(options))

        if option == 1:
            InventorySeeder(self.inventory_repo).seed(MOCKS_PRODUCTS)
            OrderSeeder(self.order_repo).seed(MOCKS_ORDERS)
            print(f"{BLUE}\tSe ha ejecutado un seeder para poblar el inventario y los pedidos{RESET}")
        elif option == 2:
            print(f"{BLUE}\tSe ha seleccionado no ejecutar el seeder{RESET}")
        
        print("\n", "-" * 100)


    def _print_welcome(self):
        print(
            f"{GREEN}\n\nBienvenido(a) a la DEMO de inventario y pedidos{RESET}",
            end="\n\n",
        )


    def _select_persistence(self) -> None:
        print("Configuración inicial de persistencia de datos (Selecciona una opción):")
        
        options = [
            "Persistencia en local (memory)",
            "Persistencia en base de datos (SQLite)",
        ]

        show_menu_options(options)
        option = read_option(len(options))

        if option == 1:
            print(
                f"{BLUE}\tAtención: La aplicación almacenará los datos de manera temporal "
                f"en la memoria. Una vez cerrada la aplicación, los registros desaparecerán{RESET}"
            )
            self.inventory_repo = InventoryMemoryRepository()
            self.order_repo = OrderMemoryRepository()
        elif option == 2:
            print(
                f"{BLUE}\tAtención: La aplicación almacenará los datos de manera permanente "
                f"en la base de datos del programa. Una vez cerrada la aplicación, los registros seguirán disponibles{RESET}"
            )
            self.inventory_repo = InventorySQLiteRepository()
            self.order_repo = OrderSQLiteRepository()
        
        print("\n", "-" * 100)
       
    
    def _main_menu_loop(self):
        while True: 
            print(f"{GREEN}\nSelecciona el módulo de la aplicación con la cual deseas interactuar{RESET}")
            
            options = [
                "Inventario de productos",
                "Gestión de pedidos",
            ]
            
            show_menu_options(options)
            option = read_option(len(options))

            if option == 1:
                InventoryMenu(self.inventory_repo).run()
            elif option == 2:
                OrderMenu(self.order_repo).run()
            
            print("\n", "-" * 100)