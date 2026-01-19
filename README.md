# nttdata

# Hola equipo de NTT DATA, en esta oportunidad desarrolle la prueba tecnica con la tecnologia de Python/Django
# Tengo ya 2 años de experiencia desarrollando proyectos backend con Django, por lo que puedo decir que conozco a nivel intermedio 
# sobre el desarrollodo y mantinimiento de proyectos con esta tecnologia.

# Para la gestion de librerias y conflictos de versiones de las mismas estamos empleado en uso de un entorno virtual el cual esta denominado 

# venv

# se puede crear con py -3.11 -m venv venv o si no python -m venv venv

# y activar segun el SO (Windows) .\venv\Scripts\Activate o (Linux/Mac) source venv/bin/activate

# Asi como variables de entorno dentro del archivo .env que deben crear en la carpeta wapp/ 

# Ejemplo del .env

# DEBUG=True
# SECRET_KEY="django-insecure-25&b+#p-w__!mvt^6=x4z2@@9#5gxz*_d&j(iaq#0dp6em&5zc"

# API_URL = "https://randomuser.me/api/"
# DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
# CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3003
# CSRF_TRUSTED_ORIGINS=http://localhost:3000,http://localhost:3003

# Algunas librerias a considerar se encuentran dentro del archivo requeriments.txt, las cuales podemos instalar una vez tengamos habilitado el entorno virtual
# con el comando pip install -r requeriments.txt


# En cuanto a la base de datos esta usandose una bd local db.sqlite3

# Las configuraciones del proyecto a nivel de allowed host, cors y configuraciones de base datos se encuentra dentro de wapp/settings.py

# asi como tambien el registro de las aplicaciones en este users dentro del campo INSTALLED_APPS
#
# En la carpeta de apps se encuentra lo que es la logica completa, para ser mas especifico en models.py la estructura de la tabla

# en serializers.py es lo mas parecido a un DTO, basicamente define una estructura a validar tipo de datos segun el modelo Users

# en services/api.py se encuentra la logica de generacion y consumo de la api proporcionada
# en views.py se encuentra la apertura de un endpoint para el consumo y generacion de los datos generados

# Resaltar que el frontend esta en un index.html el cual consume directamente con axios a la url de este backend lo que genera y muestra los usuarios generados
# dichos usuarios se guardan dentro de la base de datos



# comando para levantar proyecto: python manage.py runserver

# comando para levantar el front: python -m http.server 3000