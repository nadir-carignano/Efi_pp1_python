# EFI practica profesionalizante parte 2 

#### Este semestre, expandimos nuestro miniblog desarrollado en Flask, incorporando dos herramientas poderosas: Marshmallow y MethodView. Estas adiciones permitirán la creación de endpoints robustos para interactuar con nuestra aplicación de manera eficiente. 

#####  Esta vez decidimos que nuestro miniblog se pueda consumir como API.Esto quiere decir que no se va apoder usar o ver como aplicacion web.

**A continuacion se encuentra un instructivo para levantar el repositorio**

Instrutivo para levantar el repositorio:  
------------
1. Antes de clonar el repositorio,lo mejor seriá ubucarte sobre la carpeta donde lo quieras clonar, desde la terminal de git.  
2. Ahora ya puedes clonar el repositorio dentro de la carpeta seleccionada.Para ello, puedes clonar el repositorio en la terminal de git con el comando `git clone git@github.com:nadir-carignano/Efi_pp1_python.git` o descargarlo en formato zip desde **"code"** para descomprimirlo despues dentro de la carpeta. 

**A partir de este punto, para correrlo pueden hacerlo de dos formas diferentes, en su maquina local o en docker**

Como correrlo en su maquina local:
----------------

1. Luego de clonar el repositorio, entra en la carpeta que contiene todos los archivos del repositorio para hacer un entorno virtual,esa carpeta es seria **practico_efi_2**,tambien **desde la terminal**. 

    Puedes hacer el entorno con el comando:
`python -m venv entorno`

    O con el comando:
`virtualenv entorno`

2. Ahora tienes que activar tu entorno virtual con el comando:

    Para windows
`entorno\Scripts\activate.bat`

    Para unix o mac
`source entorno/bin/activate`

3. Lo siguiente que tenes que hacer es instalar todas las librerias necesarias para usar el proyecto,para ello usaras el **requirements.txt** (un archivo en el repositorio clonado)para instalarlas vas a usar el siguiente comando:

`pip install -r requirements.txt`

4. Ahora tenes que crear la base de datos que vas a usar para el proyecto y despues de crear la base de datos tenes que completar el archivo **.env**,el cual no lo tenes en el repositorio,pero si tenes el archivo **.env.sample** que vas a usarlo editando su nombre para llamarlo **.env**.En este archivo vas a completar las variables (ROOT_USER,MYSQL_ROOT_PASSWORD,MYSQL_CONTAINER_NAME y MYSQL_DATABASE) con los datos que correspondan en cada lugar.

5. Despues tenes que correr los siguientes comandos para crear las tablas que van a estar en la base de datos que vas a usar:

`flask db init`

`flask db migrate -m "creando tablas del blog"`

`flask db upgrade`

6. Por ultimo puedes correr el proyecto para empezar a usarlo:

`flask run --reload`


Como correrlo con docker:
-------------

1. Tenes que completar el archivo **.env**,el cual no lo tenes en el repositorio,pero si tenes el archivo **.env.sample** que vas a usarlo editando su nombre para llamarlo **.env**.En este archivo vas a completar las variables (ROOT_USER,MYSQL_ROOT_PASSWORD,MYSQL_CONTAINER_NAME,MYSQL_PASSWORD y MYSQL_DATABASE) con los datos que correspondan en cada lugar.

2. Despues tenes que correr el siguiente comando para crear una imagen para mysql y para flask_app pero antes asegurate que estas parado en la carpeta donde tenes el proyecto,esa carpeta es seria **practico_efi_2**(si estas en windows asegurate de tener la aplicacion docker abierta antes de correr el comando):

`docker-compose build`

NOTA:si estas en linux agrega delante  de todos los comandos de docker la palabra **sudo**

3. Ahora tenes que correr el siguiente comando para crear y correr el contenedor de mysql y flask_app:

`docker-compose up`

**NOTA:Puedes unificar los pasos 2 y 3 con el comando:**

`docker-compose build && docker-compose up`

4. Luego pega la siguiente ruta en tu navegador para ver si el contenedor esta funcionando:

 `localhost:5005`


COMANDOS QUE TE PUEDEN AYUDAR:

- Para ver que creaste la imagen podes usar el comando `docker images`
- Para verificar que el contenedor este corriendo puedes usar el comando `docker ps` ,en caso de que el contenedor no se vea,puedes usar el comando `docker ps -a` para saber si te lo creo y esta detenido solamente.
- En caso de que el contenedor este corriendo puedes detenerlo con el comando `docker stop <container_id>` y en caso de que el contenedor se encuentre detenido puedes correrlo con el comando `docker start <container_id>`
- En caso de querer eliminar el contenedor puedes hacerlo con el comando `docker container rm <container_id>` y en caso de querer eliminar una imagen puedes hacerlo con el comando `docker image rm <image_id>`
- Si queres abrir el contenedor para ver que tenes dentro en una terminal shell podes usar el comando `docker exec -it <container_id> sh` y para salir de la shell el comando `exit`
- Si queres borrar los volúmenes asociados al docker-compose del proyecto podes usar el comando `docker-compose down -v`
- Si tenes que borrar todas las imágenes, contenedores y volúmenes que tengas puedes usar el comando `docker system prune -a --volumes`
- Para detener y eliminar todos los contenedores puedes usar el comando `docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)`

#### A continuacion voy a deja una ayuda para la API ,asi se facilita un poco el uso y  su entendimiento:

##### Sobre el usuario:
-----------
**Para ver informacion de los usuario:**
GET:
Para ver los datos de todos los usuario: /user
Para ver los datos de un solo usuario: /user/id

**json para cargar un usuario**
POST:
/user
```{json}
{
    "name":"nombre usuario",
    "correo":"correo del usuario",
    "password":"contraseña del usuario"
}
```

**json para editar un usuario**
PUT:
/user/id
```{json}
{
    "old_name":"nombre actual del usuario(para vefificar los identidad antes de permitir cambiarlos)",
    "old_password":"contraseña actual",
    "new_name":"nombre nuevo",
    "new_password":"contraseña nueva"
}
```

**json para eliminar un usuario**
DELETE:
/user/id
```{json}
{
    "name":"nombre del usuario(para vefificar los identidad antes de permitir eliminar el usuario)",
    "password":"contraseña"
}
```


##### Sobre las categorias de post:
------------
**Para ver informacion de las categorias:**
GET:
Para ver los datos de todas las categorias: /category
Para ver los datos de una sola categoria : /category/id

**json para agregar categoria**
POST:
/category
```{json}
{
    "etiqueta":"nombre de la categoria"
}
```

**json para editar un categoria**
PUT:
/category/id
```{json}
{
    "etiqueta":"nombre nuevo de la categoria"
}
```

**Para eliminar un categoria:**
DELETE:
/category/id


##### Sobre el post:
-----------------
**Para ver informacion de los posteos:**
GET:
Para ver los datos de todos los post: /post
Para ver los datos de un solo post: /post/id

**json para agregar post**
POST:
/post
```{json}
{
    "title":"titulo del post",
    "content":"contenido del post",
    "user":"id del usuario que poste",
    "category":"id de la categoria del posteo"
}
```

**json para editar un post**
PUT:
/post/id
```{json}
{
    "title":"titulo editado del post",
    "content":"contenido editado del post"
}
```

**Para eliminar un post:**
DELETE:
/post/id


##### Sobre los comentarios de post:
-------------
**Para ver informacion de los comentario:**
GET:
Para ver los datos de todos los comentarios: /coment
Para ver los datos de un solo comentario: /coment/id

**json para agregar un comentario**
POST:
/coment
```{json}
{
    "coment":"comentario",
    "user":"id del usuario que comento",
    "post":"id del posteo"
}
```

**json para editar un comentario**
PUT:
/coment/id
```{json}
{
    "coment":"comentario editado"
}
```

**Para eliminar un comentario:**
DELETE:
/coment/id
