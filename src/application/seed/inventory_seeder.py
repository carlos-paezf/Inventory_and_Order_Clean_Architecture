from typing import Iterable

from application.usecases.inventory.add_product import AddProductUseCase
from domain.entities.product import Product
from interfaces.repositories.inventory_repo import InventoryRepository


class InventorySeeder:
    """
    Description
    -----------
    Seeder para poblar el inventario con productos mock.

    Usa el caso de uso AddProductUseCase para respetar las reglas
    de negocio y la arquitectura limpia.
    """

    def __init__(self, inventory_repo: InventoryRepository) -> None:
        """
        Description
        -----------
        Inicializa el seeder con el repositorio de inventario y el caso de uso AddProductUseCase.

        Attributes
        ----------
        inventory_repo : InventoryRepository
            Repositorio de inventario.
        _add_product_uc : AddProductUseCase
            Caso de uso AddProductUseCase.
        """
        self.inventory_repo = inventory_repo
        self._add_product_uc = AddProductUseCase(inventory_repo)


    def seed(self, products: Iterable[Product], ignore_errors: bool = True) -> None:
        """
        Description
        -----------
        Inserta una colección de productos en el inventario.

        Attributes
        ----------
        products : Iterable[object]
            Iterable de entidades Product (o lo que devuelva tu ProductFactory).
        ignore_errors : bool
            Si True, continúa aunque ocurra un error con algún producto.
        """
        for product in products:
            try:
                self._add_product_uc.execute(product)
            except Exception as exc:
                if ignore_errors:
                    print(f"[InventorySeeder] No se pudo insertar el producto {product.id}: {exc}")
                    continue
                raise
