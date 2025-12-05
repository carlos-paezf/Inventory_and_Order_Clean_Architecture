from __future__ import annotations
from typing import Dict
from domain.entities.product import AccessoryProduct, BookProduct, Product


class ProductFactory:
    """
    Description
    -----------
    Clase con método estático que crea un producto de forma dinámica
    haciendo uso del patrón Factory Method
    """
    @staticmethod
    def create_product(kind: str, **kwargs: Dict[str, Any]) -> Product:
        """
        Description
        -----------
        Mediante el patrón Factory Method, se crea un producto de forma dinámica
        
        Parameters
        ----------
        kind: str
            Tipo de producto a crear
        **kwargs: Dict[str, Any]
            Parámetros adicionales para crear el producto
        
        Returns
        -------
        Product
            Producto creado
        """
        kind = kind.lower()

        if kind == "book":
            return BookProduct(
                id=kwargs.get("id"), 
                name=kwargs.get("name"), 
                price=kwargs.get("price"), 
                category="Book",
                author=kwargs.get("author", "Unknown"))
        elif kind == "accessory":
            return AccessoryProduct(
                id=kwargs.get("id"), 
                name=kwargs.get("name"), 
                price=kwargs.get("price"), 
                category="Accessory",
                brand=kwargs.get("brand", "Generic"))
        else:
            return Product(
                id=kwargs.get("id"), 
                name=kwargs.get("name"), 
                price=kwargs.get("price"), 
                category=kwargs.get("category", "Generic"))