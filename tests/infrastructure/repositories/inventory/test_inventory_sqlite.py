from infrastructure.repositories.inventory.inventory_sqlite import InventorySQLiteRepository
from tests.interfaces.repositories.test_inventory_repo import NotTested

class TestInventorySQLiteRepository(NotTested.TestInventoryRepository):
    def setUp(self):
        self.repository = InventorySQLiteRepository(db_path = ":memory:")
