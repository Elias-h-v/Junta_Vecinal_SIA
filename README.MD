# Paso:1 Redirigete a la carpeta del proyecto con CD, si está en MacOS debe usar "/"
 
# Paso 2: Cree el ambiente virtual
python -m venv envsia

# Paso 3: Activar el entorno virtual
envsia\Scripts\activate

# Instalar las librerias del archivo requirements.txt
pip install -r requirements.txt

# Crear nuevo proyecto
django-admin startproject myproject

# abrir el proyecto
cd myproject

# Hacer migraciones
python manage.py makemigrations
# Iniciar las migraciones
python manage.py migrate



# Ejecutar la aplicación manage.py
python manage.py runserver

