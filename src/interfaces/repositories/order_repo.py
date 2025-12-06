from abc import ABC, abstractmethod
from typing import List
from domain.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def delete(self, order_id: str) -> bool:
        pass

    @abstractmethod
    # TODO: Maybe should not return a list?
    def get(self, order_id: str) -> List[Order] | None:
        pass

    @abstractmethod
    def list_all(self) -> List[Order]:
        pass
