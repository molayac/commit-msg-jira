# Worklog JIRA on Commit Message 

**commit-msg-jira** es un simple script que permite utilizar las bondades de uno de los [Git hooks] para reportar horas en JIRA, al mismo tiempo que realiza el commit de una funcionalidad.

Este script está desarrollado en python v3 y utiliza las librerías **jira**, **configparser** y **tzlocal** y puede ser modificado o personalizado sin ningún problema.

# Características!

  - Facilita la tarea de reporar horas
  - Evita el olvido de actividades, permitiendo reportar cuando lo acabas de hacer
  - Permite reportar horas de una funcionalidad para una fecha específica.

También puedes realizar commits sin generar el reporte en JIRA

# Uso

Lo único que hace el script es habilitar un formato para saber cuando generar o no el reporte de horas en JIRA.

Una vez se tenga diligenciado el archivo **jira.conf** con los datos de conexión a si JIRA y se haya realizado la instalación del script en los **.git/hooks** del proyecto que desea.

Lo único que requiere es recordar y utilizar el siguiente formato dentro de su commit:
> {time=5h 40m, date=2018-08-09 8:00AM, issue=JIRA-900}

Las llaves son muy importantes y los nombres de las variables tambien...
Las variables **time** e **issue** son obligatorias para poder generar el reporte de JIRA si usted utiliza las llaves y estas variables sin ningun valor, el commit será abortado.

## Ejemplos:
Este comando genera el worklog en el issue **JIRA-900**, con un tiempo de 5h (*Soporta formato de JIRA*) y con la fecha y hora actual:
```sh
$ git commit -m "AGREGANDO SUPER FUNCIONALIDAD ALPHA {time=5h, issue=JIRA-900}"
```
----
Este comando genera el worklog en el issue **JIRA-900**, con un tiempo de 1m (*Por defecto si no se especifica h o m se toma m de minutos*) y con la fecha y hora actual:
```sh
$ git commit -m "AGREGANDO SUPER FUNCIONALIDAD ALPHA {time=1, issue=JIRA-900}"
```
---

Este comando genera el worklog en el issue **JIRA-900**, con un tiempo de 5.5h (*Soporta formato de JIRA*) y con la fecha especificada:
```sh
$ git commit -m "AGREGANDO SUPER FUNCIONALIDAD ALPHA {time=5h 40m, date=2018-08-09 8:00AM, issue=JIRA-900}"
```

----
Este comando **NO** genera el worklog en JIRA pero si se realiza el commit de la funcionalidad en el repo:
```sh
$ git commit -m "AGREGANDO SUPER FUNCIONALIDAD ALPHA"
```

##### **Tener en cuenta:** *Cuando no se especifica la fecha, el timezone utilizado es el de la maquina local*

---
# Instalación

Como ya se mencionó, requiere tener instalado **Python V3**
Además debe realizar el siguiente proceso:
```sh
$ cd commit-msg-jira
$ python setup.py install
```

Luego debe renombrar en **.git/hooks/commit-msg.sample** a **.git/hooks/commit-msg**
Y en cambiar todo el contenido del archivo por: 
```sh
#!/bin/sh
commit-msg $1
```

Adicional debe crear el archivo **.git/hooks/jira.conf**
Y agregar los datos de conexión a JIRA requeridos, como se describe a continuación:

```sh
[MY-COMPANY]
HOST= https://jira.com/jira  
USER= username
PASS= password
```

#### Utilizando el código fuente
Se puede utilizar el archivo **commit-msg** y el archivo de configuracion **jira.conf** ubicados en la raíz del proyecto y en la carpeta **conf** respectivamente.
Copiar ambos archivos y pegarlos dentro de la carpeta **.git/hooks** de cada proyecto donde lo necesite. y modifique el archivo **jira.conf** con los datos requeridos.

Si se presenta algún error al ejecutar el commit, y si no realizó el comando:

```sh
$ python setup.py install
```

Es posible que deba ejecutar estos comandos para que funcione correctamente:

```sh
$ pip install tzlocal
$ pip install configparser
$ pip install jira
```
### Todos

 - Crear script de auto instalación en proyectos especificados.
 
License
----

MIT


**Software libre!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Git Hooks]: <https://git-scm.com/book/uz/v2/Customizing-Git-Git-Hooks>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
