from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    """Administra usuarios y productos de la aplicación."""

    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.productos = []
        self.cargar_datos()

    def cargar_datos(self):
        self.usuarios = [
            Usuario.desde_diccionario(datos)
            for datos in self.archivo_servicio.cargar_usuarios()
        ]
        self.productos = [
            Producto.desde_diccionario(datos)
            for datos in self.archivo_servicio.cargar_productos()
        ]

    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado
        return None

    def listar_usuarios(self):
        return self.usuarios.copy()

    def listar_productos(self):
        return self.productos.copy()
