from domain.entities.order import Order, OrderItem
from interfaces.adapters.product_factory import ProductFactory


_factory = ProductFactory()


MOCKS_ORDERS = [
    Order(
        id="O001",
        items=[
            OrderItem(
                product=_factory.create_product(
                    "book",
                    id="B001",
                    name="Libro de Prueba",
                    price=100.0,
                    author="Autor X",
                ),
                quantity=2,
            ),
            OrderItem(
                product=_factory.create_product(
                    "accessory",
                    id="A001",
                    name="Hoodie",
                    price=50.0,
                    brand="Brand Y",
                ),
                quantity=1,
            ),
        ],
    ),
    Order(
        id="O002",
        items=[
            OrderItem(
                product=_factory.create_product(
                    "book",
                    id="B002",
                    name="Clean Architecture",
                    price=120.0,
                    author="Robert C. Martin",
                ),
                quantity=2,
            ),
            OrderItem(
                product=_factory.create_product(
                    "accessory",
                    id="A002",
                    name="Mouse Gamer",
                    price=75.0,
                    brand="Logitech",
                ),
                quantity=1,
            ),
        ],
    ),
    Order(
        id="O003",
        items=[
            OrderItem(
                product=_factory.create_product(
                    "book",
                    id="B003",
                    name="Python para Todos",
                    price=90.0,
                    author="Charles Severance",
                ),
                quantity=2,
            ),
            OrderItem(
                product=_factory.create_product(
                    "accessory",
                    id="A003",
                    name="Teclado Mecánico",
                    price=150.0,
                    brand="Keychron",
                ),
                quantity=1,
            ),
        ],
    ),
    Order(
        id="O004",
        items=[
            OrderItem(
                product=_factory.create_product(
                    "book",
                    id="B004",
                    name="Clean Code",
                    price=120.0,
                    author="Robert C. Martin",
                ),
                quantity=2,
            ),
            OrderItem(
                product=_factory.create_product(
                    "accessory",
                    id="A004",
                    name="Touchpad",
                    price=150.0,
                    brand="Keychron",
                ),
                quantity=1,
            ),
        ],
    ),
    Order(
        id="O005",
        items=[
            OrderItem(
                product=_factory.create_product(
                    "book",
                    id="B005",
                    name="Clean Code Versión Extendida",
                    price=120.0,
                    author="Robert C. Martin",
                ),
                quantity=2,
            ),
            OrderItem(
                product=_factory.create_product(
                    "accessory",
                    id="A005",
                    name="Mouse Gamer",
                    price=150.0,
                    brand="Logitech",
                ),
                quantity=1,
            ),
        ],
    ),
]