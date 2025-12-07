from abc import ABC, abstractmethod
from typing import List
from domain.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        """
        Description
        -----------
        Guarda una orden en la persistencia.

        Attributes
        ----------
        order : Order
            Orden a guardar.
        """
        pass

    @abstractmethod
    def delete(self, order_id: str) -> bool:
        """
        Description
        -----------
        Elimina una orden de la persistencia.

        Attributes
        ----------
        order_id : str
            Identificador de la orden a eliminar.
        
        Returns
        -------
        bool
            True si se eliminó la orden, False si no se encontró.
        """
        pass

    @abstractmethod
    def get(self, order_id: str) -> Order | None:
        """
        Description
        -----------
        Obtiene una orden de la persistencia.

        Attributes
        ----------
        order_id : str
            Identificador de la orden a obtener.
        
        Returns
        -------
        Order | None
            Lista de ordenes si se encontró, None si no se encontró.
        """
        pass

    @abstractmethod
    def list_all(self) -> List[Order]:
        """
        Description
        -----------
        Obtiene todas las ordenes de la persistencia.
        
        Returns
        -------
        List[Order]
            Lista de todas las ordenes.
        """
        pass
