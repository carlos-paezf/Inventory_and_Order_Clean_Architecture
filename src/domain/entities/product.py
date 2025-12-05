from dataclasses import dataclass


@dataclass
class Product:
    """
    Description
    -----------
    Clase que representa un producto.

    Attributes
    ----------
    id : str
        Identificador del producto.
    name : str
        Nombre del producto.
    price : float
        Precio del producto.
    category : str
        Categoría del producto.
    """
    id: str
    name: str
    price: float
    category: str

    def get_final_price(self) -> float:
        """
        Description
        -----------
        Retorna el precio final del producto.

        Returns
        -------
        float
            Precio final del producto.
        """
        return self.price

    def __str__(self) -> str:
        """
        Description
        -----------
        Retorna una representación en string del producto.

        Returns
        -------
        str
            Representación en string del producto.
        """
        return f"[{self.id}] {self.name} ({self.category}) - ${self.get_final_price():.2f}"


@dataclass
class BookProduct(Product):
    """
    Description
    -----------
    Clase que representa un producto de tipo libro.
    Hereda de la clase Product.

    Attributes
    ----------
    author : str
        Autor del libro.
    """
    author: str

    def get_final_price(self) -> float:
        """
        Description
        -----------
        Retorna el precio final del producto. 
        En caso de ser un libro, se aplica un descuento del 10%.

        Returns
        -------
        float
            Precio final del producto.
        """
        return self.price * 0.90


@dataclass
class AccessoryProduct(Product):
    """
    Description
    -----------
    Clase que represento un producto de tipo accesorio.
    Hereda de la clase Product.

    Attributes
    ----------
    brand: str
        Marca del producto
    """
    brand: str