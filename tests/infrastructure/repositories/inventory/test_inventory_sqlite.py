from infrastructure.repositories.inventory.inventory_sqlite import InventorySQLiteRepository
from infrastructure.database.sqlite_connection import SQLiteConnection
from tests.interfaces.repositories.test_inventory_repo import NotTested

class TestInventorySQLiteRepository(NotTested.TestInventoryRepository):
    def setUp(self):
        SQLiteConnection().close()
        SQLiteConnection.destroy()

        self.repository = InventorySQLiteRepository(db_path = ":memory:")
