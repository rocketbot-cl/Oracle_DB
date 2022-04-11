



# Oracle
  
Modulo para conectarse a una DB Oracle  
  
![banner](imgs/Banner_Oracle.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  




## Como usar este módulo
Para usar este módulo, tienes que tener una base de datos de Oracle creada, y tener los datos
 de DSN si es que se usa.


## Descripción de los comandos

### Conectarse a bd Oracle
  
Configurar credenciales de conexion
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre que se desea poner a la sesion|Conn1|
|Usuario|Nombre de usuario de la base de datos|sys|
|Contraseña|Password del usuario previamente usado|password|
|DSN Hostname de Conexion|Hostname asignado en el DSN|Oracle.host.com/ORCL|
|DSN Puerto de Conexion|Puerto asignado en el DSN|1521|
|DSN SID / Service name de Conexion|SID o nombre de servicio asignado en el DSN|pdborcl / pdborcl.example.com|
|Asignar a variable|Variable donde se desea guardar el resultado.|var|

### Ejecutar una query
  
Ejecuta una query hacia la bd Oracle
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Query|Query que se desea ejecutar en la base de datos|SELECT * from table|
|Sesión|Nombre de la sesion previamente iniciada|Conn1|
|Asignar resultado a variable|Variable donde se desea guardar el resultado.|var|

### Cerrar conexión
  
Cierra una conexión de oracle por sesión
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Nombre de la sesion previamente iniciada que se desea cerrar|Conn1|
