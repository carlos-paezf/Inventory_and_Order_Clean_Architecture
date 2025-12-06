import sqlite3
from threading import Lock


class SQLiteConnection:
    """
    Description
    -----------
    Clase que representa la conexión a la base de datos

    Attributes
    ----------
    _instance : SQLiteConnection
        Instancia de la conexión a la base de datos
    _lock : Lock
        Lock para la sincronización de la instancia
    """
    _instance = None
    _lock = Lock()


    def __new__(cls, db_path: str = "database.db") -> "SQLiteConnection":
        """
        Description
        -----------
        Crea una instancia de la conexión a la base de datos

        Attributes
        ----------
        db_path : str
            Ruta de la base de datos

        Returns
        -------
        SQLiteConnection
            Instancia de la conexión a la base de datos
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(SQLiteConnection, cls).__new__(cls)
                    cls._instance.conn = sqlite3.connect(db_path, check_same_thread=False)
        return cls._instance

    
    def get_connection(self) -> sqlite3.Connection:
        """
        Description
        -----------
        Obtiene la conexión a la base de datos

        Returns
        -------
        sqlite3.Connection
            Conexión a la base de datos
        """
        return self.conn