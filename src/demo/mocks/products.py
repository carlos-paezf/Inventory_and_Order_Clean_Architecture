from interfaces.adapters.product_factory import ProductFactory


_factory = ProductFactory()


MOCKS_PRODUCTS = [
    _factory.create_product(
        "book",
        id="B001",
        name="Libro de Prueba",
        price=100.0,
        author="Autor X",
    ),
    _factory.create_product(
        "accessory",
        id="A001",
        name="Hoodie",
        price=50.0,
        brand="Brand Y",
    ),
    _factory.create_product(
        "book",
        id="B002",
        name="Clean Architecture",
        price=120.0,
        author="Robert C. Martin",
    ),
    _factory.create_product(
        "accessory",
        id="A002",
        name="Mouse Gamer",
        price=75.0,
        brand="Logitech",
    ),
    _factory.create_product(
        "book",
        id="B003",
        name="Python para Todos",
        price=90.0,
        author="Charles Severance",
    ),
    _factory.create_product(
        "accessory",
        id="A003",
        name="Teclado Mecánico",
        price=150.0,
        brand="Keychron",
    ),
    _factory.create_product(
        "book",
        id="B004",
        name="Clean Code",
        price=120.0,
        author="Robert C. Martin",
    ),
    _factory.create_product(
        "accessory",
        id="A004",
        name="Touchpad",
        price=150.0,
        brand="Keychron",
    ),
    _factory.create_product(
        "book",
        id="B005",
        name="Clean Code Versión Extendida",
        price=120.0,
        author="Robert C. Martin",
    ),
    _factory.create_product(
        "accessory",
        id="A005",
        name="Mouse Gamer",
        price=150.0,
        brand="Logitech",
    ),
]
