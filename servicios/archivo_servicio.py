import json
from pathlib import Path


class ArchivoServicio:
    """Lee los datos locales almacenados en archivos JSON."""

    def __init__(self, carpeta_datos):
        self.carpeta_datos = Path(carpeta_datos)
        self.ruta_productos = self.carpeta_datos / "productos.json"
        self.ruta_usuarios = self.carpeta_datos / "usuarios.json"

    def cargar_productos(self):
        return self._cargar_json(self.ruta_productos)

    def cargar_usuarios(self):
        return self._cargar_json(self.ruta_usuarios)

    def _cargar_json(self, ruta):
        try:
            with ruta.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        if not isinstance(datos, list):
            return []

        return datos
