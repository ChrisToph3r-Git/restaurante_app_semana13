# restaurante_app - Semana 13
## Autor

Christopher Leonardo Paredes Jiménez

## Tema

Conceptos fundamentales de interfaces gráficas de usuario con Tkinter.

## Descripción

Esta versión incorpora una interfaz gráfica inicial al proyecto `restaurante_app`, manteniendo separadas las responsabilidades de modelos, servicios, datos e interfaz.

El sistema permite iniciar sesión de forma local y simulada. Después de un acceso correcto, la interfaz principal permite consultar los productos y usuarios cargados desde archivos JSON.

Las funcionalidades de ventas quedan identificadas como pendientes, de acuerdo con el alcance de la Semana 13.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Responsabilidad de los componentes

- **Producto:** representa los productos del restaurante y valida sus datos.
- **Usuario:** representa los usuarios utilizados para el acceso simulado.
- **ArchivoServicio:** lee la información almacenada en `productos.json` y `usuarios.json`.
- **RestauranteServicio:** convierte los datos en objetos, valida el acceso y proporciona las listas de usuarios y productos.
- **LoginView:** presenta la pantalla de acceso, recibe usuario y contraseña y muestra mensajes de validación.
- **MainView:** presenta la interfaz principal y muestra los usuarios y productos mediante `RestauranteServicio`.
- **main.py:** crea una única ventana principal, prepara los servicios y controla el cambio entre LoginView y MainView.
- **datos/:** contiene los archivos JSON con información local de ejemplo.

## Flujo de la aplicación

```text
Inicio
  ↓
main.py prepara Tkinter y los servicios
  ↓
LoginView
  ↓
Usuario y contraseña
  ↓
RestauranteServicio valida el acceso
  ↓
MainView
  ↓
Productos | Usuarios | Ventas (pendiente)
  ↓
Cerrar sesión
  ↓
LoginView
```

La aplicación utiliza una sola ventana principal de Tkinter y un único `mainloop()`.

## Vistas implementadas

### LoginView

Permite ingresar usuario y contraseña. Si los campos están vacíos o las credenciales son incorrectas, se muestra un mensaje visual. Las credenciales válidas se comprueban mediante `RestauranteServicio`.

### MainView

Muestra un panel principal con opciones para consultar productos y usuarios. La opción **Ventas** se muestra como funcionalidad pendiente.

Las vistas no leen directamente los archivos JSON. La información se solicita a `RestauranteServicio`.

## Credenciales de demostración

- Usuario: `admin`
- Contraseña: `1234`

También puede utilizarse:

- Usuario: `cliente`
- Contraseña: `1234`

El acceso es local y simulado con fines académicos.

## Requisitos

- Python 3.x
- Tkinter

No se requieren dependencias externas.

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

En Windows también puede utilizarse:

```bash
py main.py
```

## Comprobación del funcionamiento

1. Ejecutar `main.py`.
2. Verificar que aparezca primero el LoginView.
3. Intentar ingresar con campos vacíos y comprobar el mensaje visual.
4. Intentar ingresar con credenciales incorrectas y comprobar el mensaje visual.
5. Ingresar con `admin` y `1234`.
6. Verificar que aparezca MainView.
7. Seleccionar **Productos** y comprobar que se muestran los productos de `productos.json`.
8. Seleccionar **Usuarios** y comprobar que se muestran los usuarios de `usuarios.json`.
9. Seleccionar **Ventas** y comprobar que aparece el mensaje de funcionalidad pendiente.
10. Seleccionar **Cerrar sesión** y comprobar que la aplicación regresa al LoginView sin abrir otra ventana principal.

## Alcance de la Semana 13

En esta etapa se incorpora únicamente la base gráfica solicitada: acceso simulado, consulta de productos y consulta de usuarios no se desarrollan ventas completas, formularios avanzados, bases de datos, autenticación real ni nuevas entidades.
