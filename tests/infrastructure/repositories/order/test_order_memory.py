from tests.interfaces.repositories.test_order_repo import NotTested
from infrastructure.repositories.order.order_memory import OrderMemoryRepository

class TestOrderMemoryRepository(NotTested.TestOrderRepository):
    def setUp(self):
        self.repository = OrderMemoryRepository()
