from typing import Dict, List
from domain.entities.order import Order
from domain.entities.product import Product
from interfaces.repositories.order_repo import OrderRepository


class OrderMemoryRepository(OrderRepository):
    def __init__(self):
        self._orders: Dict[str, Order] = {}

    def save(self, order: Product) -> None:
        if order.id in self._orders:
            raise ValueError(f"409 - Ya existe una orden con el id {order.id}")
        self._orders[order.id] = order


    def delete(self, order_id: str) -> None:
        if order_id not in self._orders:
            raise ValueError(f"404 - La orden con el id {order_id} no fue encontrado")
        del self._orders[order_id]


    def get(self, order_id: str) -> List[Order]:
        if order_id not in self._orders:
            raise ValueError(f"404 - La orden con el id {order_id} no fue encontrado")
        return self._orders[order_id]


    def list_all(self) -> List[Order]:
        return list(self._orders.values())