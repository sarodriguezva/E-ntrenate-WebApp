# E-ntrenate-WebApp

Este repositorio contiene el proyecto que se desarollara para la clase de Ingeniería de Software 1 de la Universidad Nacional de Colombia Semestre 2021-2

# Getting Started

Antes de correr este proyecto, asegurate de que tus dependencias esten al día ( preferiblemente en un entorno virtual).

`pip install -r requirements.txt`

<ROOT>/.virtualenvs/E-ntrenate-WebApp-ySmmBlwN/Scripts/activate.bat

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
