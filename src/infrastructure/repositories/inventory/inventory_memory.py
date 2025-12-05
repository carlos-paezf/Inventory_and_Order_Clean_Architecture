from typing import Dict, List
from domain.entities.product import Product
from interfaces.repositories.inventory_repo import InventoryRepository


class InventoryMemoryRepository(InventoryRepository):
    def __init__(self):
        self._products: Dict[str, Product] = {}


    def add_product(self, product: Product) -> None:
        if product.id in self._products:
            raise ValueError(f"409 - Ya existe un producto con el id {product.id}")
        self._products[product.id] = product


    def remove_product(self, product_id: str) -> bool:
        if product_id not in self._products:
            return False
        else:
            del self._products[product_id]
            return True

    
    def get_product(self, product_id: str) -> Product | None:
        return self._products.get(product_id) if product_id in self._products else None


    def list_products(self) -> List[Product]:
        return list(self._products.values())