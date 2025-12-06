from application.usecases.inventory.add_product import AddProductUseCase
from application.usecases.inventory.get_product import GetProductUseCase
from application.usecases.inventory.list_products import ListProductsUseCase
from application.usecases.inventory.remove_product import RemoveProductUseCase

from domain.entities.product import Product

from infrastructure.cli.console_utils import (
    GREEN, MAGENTA, RED, RESET, YELLOW, pause, show_menu_options, read_option
)

from interfaces.adapters.product_factory import ProductFactory
from interfaces.repositories.inventory_repo import InventoryRepository

class InventoryMenu:
    """
    Description
    -----------
    Clase que gestiona el menú de inventario.

    Attributes
    ----------
    inventory_repo : InventoryRepository
        Repositorio de inventario.
    """
    
    def __init__(self, inventory_repo: InventoryRepository) -> None:
        """
        Description
        -----------
        Inicializa el menú de inventario.

        Parameters
        ----------
        inventory_repo : InventoryRepository
            Repositorio de inventario.
        """
        self.inventory_repo = inventory_repo

    def run(self) -> None:
        """
        Description
        -----------
        Ejecuta el menú de inventario.
        """
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
                self._add_product()
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


    def _add_product(self) -> None:
        """
        Description
        -----------
        Ejecuta el caso de uso `Añadir producto`.
        """
        # TODO: Añadir el flujo de inserción manual de productos
        product = self._capture_product()
        if product is None:
            print(f"{YELLOW}Nota:{RESET} No se ha creado ningún producto")
            return
        AddProductUseCase(self.inventory_repo).execute(product)
        print(f"{GREEN}\nCaso de uso `Añadir producto` ha sido ejecutado{RESET}")

    
    def _capture_product(self) -> Product:
        """
        Description
        -----------
        Captura los datos de un producto.

        Returns
        -------
        Product
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


    def _get_product(self) -> None:
        """
        Description
        -----------
        Ejecuta el caso de uso `Obtener producto`.
        """
        product_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id del producto a consultar: "
        )
        product = GetProductUseCase(self.inventory_repo).execute(product_id)
        print(product if product else f"No se encontró el producto con el id {product_id}")
        print(f"{GREEN}\nCaso de uso `Obtener producto` ha sido ejecutado{RESET}")


    def _list_products(self) -> None:
        """
        Description
        -----------
        Ejecuta el caso de uso `Listar productos`.
        """
        products = ListProductsUseCase(self.inventory_repo).execute()
        if len(products) == 0:
            print("No se encontraron productos")
        else:
            for idx, product in enumerate(products):
                print(f"{idx + 1}. {product}")
        print(f"{GREEN}\nCaso de uso `Listar productos` ha sido ejecutado{RESET}")

        
    def _remove_product(self) -> None:
        """
        Description
        -----------
        Ejecuta el caso de uso `Remover producto`.
        """
        product_id = input(
            f"{MAGENTA}>>>{RESET} Ingrese el id del producto a eliminar: "
        )
        deleted = RemoveProductUseCase(self.inventory_repo).execute(product_id)
        if deleted:
            print(f"El producto {product_id} ha sido eliminado con éxito")
        else:
            print(f"No se encontró el producto con el id {product_id}")
        print(f"{GREEN}\nCaso de uso `Remover producto` ha sido ejecutado{RESET}")
