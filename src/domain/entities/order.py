from typing import List, Optional
from dataclasses import dataclass
from domain.entities.product import Product


@dataclass
class OrderItem:
    """
    Description
    -----------
    Clase que representa un item de una orden de pedido.

    Attributes
    ----------
    product: Product
        Producto que se va a comprar.
    quantity: int
        Cantidad del producto que se va a comprar.
    """
    product: Product
    quantity: int

    def get_subtotal(self) -> float:
        """
        Description
        -----------
        Calcula el subtotal de un item de una orden de pedido.

        Returns
        -------
        float
            Subtotal de la orden de pedido para un producto especifico.
        """
        return self.product.get_final_price() * self.quantity


class Order:
    """
    Description
    -----------
    Clase que representa una orden de compra

    Attributes
    ----------
    id : str
        Id del pedido
    items : List[OrderItem]
        Lista de items de la orden
    """
    def __init__(self, id, items: Optional[List[OrderItem]] = None) -> None:
        """
        Description
        -----------
        Constructor de la clase Order. Inicializa una lista vacía de items

        Parameters
        ----------
        id : str
            Id del pedido
        items : Optional[List[OrderItem]]
            Lista de items de la orden
        """
        self.id: str = id
        self.items: List[OrderItem] = items or []
        

    def add_item(self, product: Product, quantity: int) -> None:
        """
        Description
        -----------
        Agrega un item a la orden

        Parameters
        ----------
        product : Product
            Producto a agregar
        quantity : int
            Cantidad del producto

        Raises
        ------
        ValueError
            Si la cantidad es menor o igual a 0
        """
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        self.items.append(OrderItem(product, quantity))


    def remove_item(self, product_id: str) -> None:
        """
        Description
        -----------
        Elimina un item de la orden

        Parameters
        ----------
        product_id : str
            ID del producto a eliminar
        """
        self.items = [item for item in self.items if item.product.id != product_id]


    def calculate_total(self) -> float:
        """
        Description
        -----------
        Calcula el total de la orden

        Returns
        -------
        float
            Total de la orden
        """
        return sum(item.get_subtotal() for item in self.items)


    def __str__(self) -> str:
        """
        Description
        -----------
        Devuelve una representación en string de la orden para debugging simple

        Returns
        -------
        str
            Representación en string de la orden
        """
        return f"Orden id: {self.id}. Cantidad de items: {len(self.items)}"