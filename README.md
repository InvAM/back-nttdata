# nttdata

# Hola equipo de NTT DATA, en esta oportunidad desarrolle la prueba tecnica con la tecnologia de Python/Django
# Tengo ya 2 años de experiencia desarrollando proyectos backend con Django, por lo que puedo decir que conozco a nivel intermedio 
# sobre el desarrollodo y mantinimiento de proyectos con esta tecnologia.

# Para la gestion de librerias y conflictos de versiones de las mismas estamos empleado en uso de un entorno virtual el cual esta denominado 

# venv

# se puede crear con py -3.11 -m venv venv o si no python -m venv venv

# y activar segun el SO (Windows) .\venv\Scripts\Activate o (Linux/Mac) source venv/bin/activate

# Algunas librerias a considerar se encuentran dentro del archivo requeriments.txt

# En cuanto a la base de datos esta usandose una bd local db.sqlite3

# Las configuraciones del proyecto a nivel de allowed host, cors y configuraciones de base datos se encuentra dentro de wapp/settings.py

# En la carpeta de apps se encuentra lo que es la logica completa, para ser mas especifico en models.py la estructura de la tabla

# en serializers.py es lo mas parecido a un DTO, basicamente define una estructura a validar tipo de datos segun el modelo Users

# en services/api.py se encuentra la logica de generacion y consumo de la api proporcionada
# en views.py se encuentra la apertura de un endpoint para el consumo y generacion de los datos generados

# Resaltar que el frontend esta en un index.html el cual consume directamente con axios a la url de este backend lo que genera y muestra los usuarios generados
# dichos usuarios se guardan dentro de la base de datos

# comando para levantar proyecto: python manage.py runserver

# comando para levantar el front: python -m http.server 3000