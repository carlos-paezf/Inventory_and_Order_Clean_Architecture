from infrastructure.repositories.inventory.inventory_sqlite import InventorySQLiteRepository
from infrastructure.repositories.order.order_sqlite import OrderSQLiteRepository
from domain.entities.product import Product, BookProduct, AccessoryProduct
from infrastructure.database.sqlite_connection import SQLiteConnection
from tests.interfaces.repositories.test_order_repo import NotTested
from demo.mocks.orders import MOCKS_ORDERS
from domain.entities.order import Order

class TestOrderSQLiteRepository(NotTested.TestOrderRepository):
    _inventory_repository: InventorySQLiteRepository

    def setUp(self):
        SQLiteConnection().close()
        SQLiteConnection.destroy()

        self._inventory_repository = InventorySQLiteRepository(db_path = "file::memory:?cache=shared", uri = True)

        products_to_insert = self._extract_products_from_orders(MOCKS_ORDERS)
        self._insert_products_to_db(products_to_insert)

        self.repository = OrderSQLiteRepository(db_path = "file::memory:?cache=shared", uri = True)

    def _insert_products_to_db(self, products: list[Product | BookProduct | AccessoryProduct]):
        for product in products:
            self._inventory_repository.add_product(product)

    def _extract_products_from_orders(self, orders: list[Order]):
        def get_order_products(order: Order):
            return list(map(lambda order_item: order_item.product, order.items))

        products_by_order = list(map(get_order_products, orders))

        return [product for order in products_by_order for product in order]
