import os
import sys

from typing import Optional, Sequence

from application.usecases.inventory.add_product import AddProductUseCase
from application.usecases.inventory.get_product import GetProductUseCase

from domain.entities.order import Order
from domain.entities.product import Product

from interfaces.adapters.product_factory import ProductFactory
from interfaces.repositories.inventory_repo import InventoryRepository


GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


def clean_console() -> None:
    """
    Description
    -----------
    Limpia la consola.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pause() -> None:
    """
    Description
    -----------
    Pausa la ejecución del programa.
    """
    input(f"{MAGENTA}\nPresiona Enter para volver al menú...{RESET}")
    print("\n", "-" * 100)



def show_menu_options(options: Sequence[str], exit_label: str = "Salir de la demo") -> None:
    """
    Description
    -----------
    Muestra las opciones disponibles.
    """
    for i, opt in enumerate(options, start=1):
        print(f"\t{i}. {opt}")
    print(f"\t0. {exit_label}")


def read_option(n_options: int) -> int:
    """
    Description
    -----------
    Lee la opción seleccionada.
    """
    while True:
        raw = input(f"{MAGENTA}>>>{RESET} Ingrese el número de la opción a ejecutar: ")

        try:
            option = int(raw)
        except ValueError:
            print(f"{RED}Por favor, solo ingrese solo el numeral de la opción{RESET}")
            continue

        if option == 0:
            print(f"{BLUE}\nSaliendo...{RESET} Gracias por usar la demo.")
            sys.exit(0)

        if 1 <= option <= n_options:
            return option

        print(
            f"{YELLOW}La opción ingresada no es válida.{RESET} "
            f"Ingrese un número entre 0 y {n_options}."
        )


def capture_order_id() -> str:
    """
    Description
    -----------
    Captura el id de la orden desde consola.

    Returns
    -------
    str
        Id de la orden
    """
    return input(f"{MAGENTA}>>>{RESET} Ingrese el id de la orden: ")


def capture_product_id(prompt: str = "Ingrese el id del producto: ") -> str:
    """
    Description
    -----------
    Captura el id de un producto desde consola.

    Returns
    -------
    str
        Id del producto
    """
    return input(f"{MAGENTA}>>>{RESET} {prompt}")


def capture_quantity() -> int:
    """
    Description
    -----------
    Captura una cantidad válida (> 0) desde consola.

    Returns
    -------
    int
        Cantidad de productos para la orden
    """
    while True:
        try:
            quantity = int(input(
                f"{MAGENTA}>>>{RESET} Ingrese la cantidad del producto: "
            ))
            if quantity <= 0:
                print(f"{RED}Error:{RESET} La cantidad debe ser mayor a 0.")
                continue
            return quantity
        except ValueError:
            print(f"{RED}Error:{RESET} La cantidad debe ser un número entero.")


def capture_product() -> Optional[Product]:
    """
    Description
    -----------
    Captura los datos de un producto.

    Returns
    -------
    Optional[Product]
        Producto creado
    """
    while True:
        print(
            f"{GREEN}\nTe presentamos los tipos de categorías disponibles para el producto:"
            f"{RESET} (Selecciona una opción)"
        )

        options = [
            "Accesorio",
            "Libro",
            "Otro",
            "Volver atrás"
        ]

        show_menu_options(options, exit_label="Salir de la demo")
        option = read_option(len(options))

        category = ""

        if option == 1:
            category = "accessory"
        elif option == 2:
            category = "book"
        elif option == 4:
            return

        product_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id del producto: "
        )
        product_name = input(
            f"{MAGENTA}>>>{RESET} Ingrese el nombre del producto: "
        )
        
        while True:
            try:
                product_price = float(input(
                    f"{MAGENTA}>>>{RESET} Ingrese el precio del producto: "
                ))
                break
            except ValueError:
                print(f"{RED}Error:{RESET} El precio debe ser un número válido.")
        
        product_brand = None
        product_author = None

        if category == "accessory":
            product_brand = input(
                f"{MAGENTA}>>>{RESET} Ingrese la marca del producto: "
            )
        elif category == "book":
            product_author = input(
                f"{MAGENTA}>>>{RESET} Ingrese el autor del producto: "
            )

        return ProductFactory().create_product(
            category,
            id=product_id,
            name=product_name,
            price=product_price,
            brand=product_brand,
            author=product_author
        )