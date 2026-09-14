import tkinter as tk
from tkinter import messagebox, ttk


class LoginView:
    """Pantalla de acceso de la aplicación."""

    def __init__(self, root, restaurante_servicio, mostrar_principal):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_principal = mostrar_principal

        self.contenedor = ttk.Frame(root, padding=30)
        self.contenedor.pack(fill="both", expand=True)

        ttk.Label(
            self.contenedor,
            text="Restaurante App",
            font=("Arial", 20, "bold")
        ).pack(pady=(30, 20))

        ttk.Label(self.contenedor, text="Usuario").pack(anchor="w")
        self.usuario_entry = ttk.Entry(self.contenedor, width=35)
        self.usuario_entry.pack(fill="x", pady=(5, 15))

        ttk.Label(self.contenedor, text="Contraseña").pack(anchor="w")
        self.contrasena_entry = ttk.Entry(
            self.contenedor,
            width=35,
            show="*"
        )
        self.contrasena_entry.pack(fill="x", pady=(5, 15))

        ttk.Button(
            self.contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        ).pack(pady=10)

        self.mensaje = ttk.Label(self.contenedor, text="")
        self.mensaje.pack(pady=10)

        self.usuario_entry.focus()

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje.config(text="Ingrese usuario y contraseña.")
            return

        usuario_validado = self.restaurante_servicio.validar_acceso(
            usuario,
            contrasena
        )

        if usuario_validado is None:
            self.mensaje.config(text="Usuario o contraseña incorrectos.")
            return

        self.mostrar_principal()
