# Coder House - Proyecto del Curso Python       
Cominsión: 55630
    
# Objetivo
El objetivo del proyecto es construir una página que permita mostrar los datos de jugadores, clubes, ligas y arenas de handball que fueron scrappeados de la página handball Base, como así también proveer formularios para introducir o actualizar registros. 
El proyecto se propone como una continuación del realizado para el curso de SQL, en el cual se diseñó el modelo de la base para almacenar dichos datos (no respetado para este proyecto).
    
# Modelos
La aplicación cuenta con 4 modelos, nombrados anteriormente:    
- Jugador: el cual almacena datos de jugadores de handball (nombre, altura, club acutal, etc)
- Club: el cual almacena datos de los clubes (nombre, liga que compite, país, etc)
- Liga: el cual almacena datos de las ligas (nombre, país, etc)
- Arena: el cual almacena datos de las canchas de handball (nombre, capacidad, país, etc)
     
# Usuarios
Existen dos usuarios cargados, con los cuales es posible loguearse en la aplicación. De todas formas, es posible registrar nuevos usuarios.    
Usuarios registrados:     
- usuario: admin - pass: admin1234
- usuario: DiegoC - pass: Diego12345

# Estructura
La aplicación cuenta con muchos archivos html. Como archivos base se crearon tres modelos de páginas y uno de barra de navegación.     
La barra de navegación se encuentra en un archivo separado, el cual es consumido por otros dos archivos base: uno es empleado para la página de inicio y de datos; el otro es empleado para las párinas de formularios y about. El tercer archivo base es una página de una sola pantalla completa que es empleada para los formularios de ABM de usuario y para la confirmación de la eliminación de los registros.     
Este último modelo de página no contine navbar para moverse, solo contiene un botón de aceptación de la tarea en curso, o un botón para cancelar y volver a la página anterior. Esta página te deja atrapado en ella con al única opción de aceptar o no lo que se está llevando a cabo.

# Aplicación
A continuación se detalla como emplear la aplicación y/o que se encontrará en la misma.    

## Navegación Sin Logueo
Al ingresar a la página de inicio, será posible moverse a diversas páginas por medio de la barra de navegación o de botones colocados al fin de la misma página de inicio.    
Al ingresar a las páginas de datos (jugadores, clubes, etc), será posible visualizar una tabla con los datos correspondientes y buscar un valor por el campo del nombre, pero no cargar, editar o eliminar registros sin loguearse como usuario.
También es posible ingrear en la página About.

#### Buscador 
Las páginas de datos cuentan con un buscador, para buscar por coincidencia de strings. Para realizar una búsqueda, ingresar un texto y clickear el botón de Buscar. Existen tres posibles resultados:     
- en caso de encontrar una coincidencia, mostrará en un texto la búsqueda realizada y el resultado de la misma en la tabla;    
- en caso de no encontrar una coincidencia, mostrará el texto "Ningún objeto cumple con el filtro!" en color rojo;    
- en caso de no ingresar nada a la búsqueda, mostrará el texto "Filtro no ingresado!" en color rojo y mostrará todos los datos.    

## Barra de Navegación
Por medio de la barra de navegación es posible moverse a cualquier sitio dentro de la aplicación. Esta se encuentra en todas las páginas, excepto en las páginas de ABM de usuario y confirmación de eliminación de registros (en estos casos con el botón cancelar se vuelve a la página de Inicio).    
El ingreso a los distintos formularios se encuentra limitado solo a usuarios logueados.     
Todos los comandos referidos al usuario, se encuentran en el ícono de de la persona ubicado en el extremo derecho de la barra, el cual desplegará las opciones.

## Usuario
Para registrar un usuario, ingresar a la página de registración, desplegando el ícino de la barra de navegación.     
Una vez registrado el usuario, es posible loguearse con ese usuario.      
Realizada la registración y login, será posible editar los datos de perfil, agregar o modificar el avatar o desloguearse. También será posible realizar tareas de ABM en los modelos.     
En caso de no ingresar un avatar, seguirá apareciendo el ícono de usuario al lado del nombre de usuario en la barra de navegación.

## Navegación con Usuario Logueado
Una vez logueado el usuario, se habilitarán el ingreso a los formularios de carga de registros por medio de la barra de navegación.     
También es posible, ingresando en una página de datos, por ej. la de jugadores, cargar, editar y eliminar un registro.

### Páginas de formularios
Existe una página de formulario para cada uno de los modelos (jugadores, equipos y ligas).    
Para cargar un registro, ingresar los datos correspondientes y clickear Agregar. Las fechas se deben ingresar con el formato 2023-01-01.      
Luego de agregar un nuevo registro, se redireccionará a la página de ese modelo, a la sección de la tabla, donde estará el registro agregado.
