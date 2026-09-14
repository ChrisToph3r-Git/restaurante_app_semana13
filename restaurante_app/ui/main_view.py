import tkinter as tk
from tkinter import messagebox, ttk


class MainView:
    """Interfaz principal del restaurante."""

    def __init__(self, root, restaurante_servicio, cerrar_sesion):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.cerrar_sesion = cerrar_sesion

        self.contenedor = ttk.Frame(root, padding=20)
        self.contenedor.pack(fill="both", expand=True)

        self._crear_encabezado()
        self._crear_menu()
        self.area_contenido = ttk.Frame(self.contenedor)
        self.area_contenido.pack(fill="both", expand=True, pady=15)

        self.mostrar_inicio()

    def _crear_encabezado(self):
        ttk.Label(
            self.contenedor,
            text="Restaurante App",
            font=("Arial", 20, "bold")
        ).pack(anchor="w")

    def _crear_menu(self):
        menu = ttk.Frame(self.contenedor)
        menu.pack(fill="x", pady=10)

        ttk.Button(
            menu,
            text="Inicio",
            command=self.mostrar_inicio
        ).pack(side="left", padx=5)

        ttk.Button(
            menu,
            text="Productos",
            command=self.mostrar_productos
        ).pack(side="left", padx=5)

        ttk.Button(
            menu,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).pack(side="left", padx=5)

        ttk.Button(
            menu,
            text="Ventas",
            command=self.mostrar_ventas_pendientes
        ).pack(side="left", padx=5)

        ttk.Button(
            menu,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).pack(side="right", padx=5)

    def limpiar_contenido(self):
        for widget in self.area_contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenido()
        ttk.Label(
            self.area_contenido,
            text="Bienvenido al sistema del restaurante.",
            font=("Arial", 14)
        ).pack(pady=30)
        ttk.Label(
            self.area_contenido,
            text="Seleccione una opción para consultar la información."
        ).pack()

    def mostrar_productos(self):
        self.limpiar_contenido()
        ttk.Label(
            self.area_contenido,
            text="Productos registrados",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", pady=(0, 10))

        productos = self.restaurante_servicio.listar_productos()

        if not productos:
            ttk.Label(
                self.area_contenido,
                text="No hay productos registrados."
            ).pack(anchor="w")
            return

        for producto in productos:
            texto = (
                f"{producto.codigo} - {producto.nombre} | "
                f"{producto.categoria} | ${producto.precio:.2f} | "
                f"Stock: {producto.stock}"
            )
            ttk.Label(self.area_contenido, text=texto).pack(anchor="w", pady=3)

    def mostrar_usuarios(self):
        self.limpiar_contenido()
        ttk.Label(
            self.area_contenido,
            text="Usuarios registrados",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", pady=(0, 10))

        usuarios = self.restaurante_servicio.listar_usuarios()

        if not usuarios:
            ttk.Label(
                self.area_contenido,
                text="No hay usuarios registrados."
            ).pack(anchor="w")
            return

        for usuario in usuarios:
            texto = f"{usuario.usuario} - {usuario.nombre} | {usuario.correo}"
            ttk.Label(self.area_contenido, text=texto).pack(anchor="w", pady=3)

    def mostrar_ventas_pendientes(self):
        messagebox.showinfo(
            "Ventas",
            "La funcionalidad de ventas será incorporada posteriormente."
        )
