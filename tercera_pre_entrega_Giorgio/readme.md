
--- Hostel Django ---


## Características

- **Inicio de sesión**: Autenticación de usuarios.
- **Gestión de habitaciones**: Crear, actualizar y eliminar habitaciones.
- **Gestión de empleados**: Crear, buscar, actualizar y eliminar empleados.
- **Gestión de clientes**: Crear y gestionar clientes.

- **Sección de contacto**: Información de contacto del hostel.

## Instalación

### Prerrequisitos

- Python 3.8+
- Django 3.2+
- SQLite (incluido con Django)
- Git (para clonar el repositorio)

### Clonar el Repositorio

```sh
git clone https://github.com/JoseGiorgio/Coderhouse.git
cd Coder
Crear un Entorno Virtual
sh

python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instalar Dependencias
sh

pip install -r requirements.txt
Configurar el Proyecto
Crear y aplicar migraciones:
sh

python manage.py makemigrations
python manage.py migrate
Crear un superusuario para acceder al panel de administración:
sh

python manage.py createsuperuser
Ejecutar el Servidor
sh

python manage.py runserver
Abre tu navegador web y navega a http://127.0.0.1:8000 para ver la aplicación en acción.

Uso
Navegación de la Aplicación
Inicio: Página de bienvenida.
Crear Cuartos: Permite crear nuevas habitaciones.
Buscar Empleados: Permite buscar empleados existentes.
Crear Empleados: Permite añadir nuevos empleados.
Lista de Empleados: Muestra una lista de empleados registrados si estas logueado con un superuser podes editar los empleados. el superuser ya creado tiene estas credenciales: usuario: jose contraseña 123
Crear Clientes: Permite añadir nuevos clientes.
Sobre Nosotros: Información sobre el hostel.
Entrar: Página de inicio de sesión para usuarios.
Avatares de Usuario
Los usuarios pueden subir y actualizar su avatar desde la sección correspondiente.