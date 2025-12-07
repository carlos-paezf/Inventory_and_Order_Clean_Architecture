from __future__ import annotations

from domain.entities.order import Order


class OrderPresenter:
    """
    Description
    -----------
    Clase que representa un presentador de ordenes
    """
    @staticmethod
    def format_order_as_table(order: Order) -> str:
        """
        Description
        -----------
        Devuelve una representación en string de la orden

        Attributes
        ----------
        order : Order
            Orden a representar

        Returns
        -------
        str
            Representación en string de la orden
        """
        header = f"Detalles de la orden {order.id}:"
        sub_header = f"{'Producto':<30} {'Cantidad':<10} {'Subtotal':<10}"
        separator = "-" * len(sub_header)

        rows = []
        for item in order.items:
            rows.append(
                f"{item.product.name:<30} {item.quantity:<10} {item.get_subtotal():<10.2f}"
            )

        total_line = f"{'TOTAL':<30} {'':<10} {order.calculate_total():<10.2f}"

        table = "\n".join([header, sub_header, separator] + rows + [separator, total_line])
        return table