# E-ntrenate-WebApp

Este repositorio contiene el proyecto que se desarollara para la clase de Ingeniería de Software 1 de la Universidad Nacional de Colombia Semestre 2021-2

# Getting Started

Antes de correr este proyecto, asegurate de que tus dependencias esten al día ( preferiblemente en un entorno virtual).

`pip install -r requirements.txt`

Estoy usando pipenv para generar un ambiente virtual, pero pueden usar el que quieran cuando lo clonen. La API ya funciona solo falta terminar los modelos de cursos, usuarios secciones y reviews. Cada una de las anteriores sera una aplicación aparte (solo estan creadas las de usuarios y cursos). Cuando habran test.py encontrarn el connection string con mis credenciales de atlas pero seria mejor que colocaran las suyas para evitar problemas de conección multiple.

Estos días he estado intentando mirar como valido los datos desde django pero no he podido, asi que creo que sera mejor hacer la validación entera desde la base de datos creando los Schemas en test.py.

Falta agregar el index.html y el css.

# Por si lo necesitan:

Como crear un virtual environment con pipenv:

1. pip install pipenv
2. pipenv install django (Les crea por defecto un virtual enviroment y dos carpetas Pipfile y Pipfile.lock)
3. ctrl+shift+p y seleccionan el interprete que les creo la anterior acción
4. pipenv shell (activan el venv)
5. Abren una nueva terminal.

### Todas las instalaciones las haran de ahora en adelante con pipenv no con pip.

### Cuidado

Cuando descargue pymongo tenia que instarle unas extensiones entonces tuve que hacer:
pipenv install pymongo[gssapi,aws,ocsp,srv,zstd,encryption]
