from typing import Dict, List

from domain.entities.order import Order
from domain.entities.product import Product

from interfaces.repositories.order_repo import OrderRepository


class OrderMemoryRepository(OrderRepository):
    """
    Description
    -----------
    Implementación del repositorio de ordenes en memoria

    Attributes
    ----------
    _orders : Dict[str, Order]
        Diccionario que almacena las ordenes en memoria
    """
    
    def __init__(self):
        """
        Description
        -----------
        Inicializa el repositorio en memoria
        """
        self._orders: Dict[str, Order] = {}


    def save(self, order: Product) -> None:
        """
        Description
        -----------
        Guarda una orden en el repositorio en memoria

        Attributes
        ----------
        order : Product
            Orden a guardar
        """
        if order.id in self._orders:
            raise ValueError(f"409 - Ya existe una orden con el id {order.id}")
        self._orders[order.id] = order


    def delete(self, order_id: str) -> bool:
        """
        Description
        -----------
        Elimina una orden del repositorio en memoria

        Attributes
        ----------
        order_id : str
            Identificador de la orden a eliminar

        Returns
        -------
        bool
            True si se eliminó la orden, False si no se encontró.
        """
        if order_id not in self._orders:
            return False
        del self._orders[order_id]
        return True


    def get(self, order_id: str) -> Order | None:
        """
        Description
        -----------
        Obtiene una orden del repositorio en memoria

        Attributes
        ----------
        order_id : str
            Identificador de la orden a obtener

        Returns
        -------
        Order | None
            Orden si se encontró, None si no se encontró.
        """
        if order_id not in self._orders:
            return None
        return self._orders[order_id]


    def list_all(self) -> List[Order]:
        """
        Description
        -----------
        Obtiene todas las ordenes del repositorio en memoria

        Returns
        -------
        List[Order]
            Lista de todas las ordenes.
        """
        return list(self._orders.values())