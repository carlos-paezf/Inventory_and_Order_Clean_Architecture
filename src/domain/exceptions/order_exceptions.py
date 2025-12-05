class OrderNotFoundError(Exception):
    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        super().__init__(f"La orden con el id {order_id} no fue encontrado")

class OrderError(Exception):
    pass
