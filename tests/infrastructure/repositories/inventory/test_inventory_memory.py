from infrastructure.repositories.inventory.inventory_memory import InventoryMemoryRepository
from tests.interfaces.repositories.test_inventory_repo import NotTested

class TestInventoryMemoryRepository(NotTested.TestInventoryRepository):
    def setUp(self):
        self.repository = InventoryMemoryRepository()
