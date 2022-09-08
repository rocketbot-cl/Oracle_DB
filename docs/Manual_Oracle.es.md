# Oracle
  
Modulo para conectarse a una DB Oracle  

*Read this in other languages: [English](Manual_Oracle.md), [Español](Manual_Oracle.es.md).*

*[How to use](how_to_use.md)*
  
![banner](imgs/Banner_Oracle.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  


## Como usar este módulo
Para usar este módulo, tienes que tener una base de datos de Oracle creada, y tener los datos de DSN si es que se usa.
También se debe descomprimir el archivo 'bin.zip' dentro de la carpeta Oracle.


## Descripción de los comandos

### Conectarse a bd Oracle
  
Configurar credenciales de conexion
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre que se desea poner a la sesion|Conn1|
|Usuario|Nombre de usuario de la base de datos|sys|
|Contraseña|Password del usuario previamente usado|password|
|Ruta a carpeta del Cliente|Es la carpeta del cliente con la version correspondiente|C:/Oracle/Client|
|Datos del DSN|Datos necesarios para la conexion al DSN|(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=dbhost.example.com)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=orclpdb1)))|
|Asignar a variable|Variable donde se desea guardar el resultado.|var|

### Ejecutar una query
  
Ejecuta una query hacia la bd Oracle
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Query|Query que se desea ejecutar en la base de datos|SELECT * from table|
|Sesión|Nombre de la sesion previamente iniciada|Conn1|
|Asignar resultado a variable|Variable donde se desea guardar el resultado.|var|

### Ejecutar una procedure
  
Ejecuta una procedure hacia la bd Oracle
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del procedure|Nombre dado al procedure en la base de datos|get_order|
|Sesión|Nombre de la sesion previamente iniciada|Conn1|
|Parámetros del Procedure|||

### Cerrar conexión
  
Cierra una conexión de oracle por sesión
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesion previamente iniciada que se desea cerrar|Conn1|
