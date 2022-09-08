# Oracle
  
Module to connect to an Oracle DB

*Read this in other languages: [English](Manual_Oracle.md), [Español](Manual_Oracle.es.md).*

*[How to use](how_to_use.md)*
  
![banner](imgs/Banner_Oracle.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module
In order to use this module, you need to have a Oracle's database, and the information of the DSN (hostname, port, SID or service name) if you use one.
The 'bin.zip' file must also be unzipped inside the Oracle folder.


## Description of the commands

### Connect to a Oracle DB
  
Configurate connection credenctials
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name for identify the session|Conn1|
|User|Name of the user to connect to the data base|sys|
|Password|Password from the user previously used|password|
|Path to folder of the client|Folder with the client of the correct version|C:/Oracle/Client|
|DSN data|Data necessary for the conextion to the DSN|(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=dbhost.example.com)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=orclpdb1)))|
|Assign to variable|Varialbe where to store the result.|var|

### Execute a query
  
Execute query
|Parameters|Description|example|
| --- | --- | --- |
|Query|Query to execute in the database|SELECT * from table|
|Session|Name of the session previously started|Conn1|
|Set result to var|Varialbe where to store the result.|var|

### Execute a procedure
  
Execute procedure in the Oracle Database
|Parameters|Description|example|
| --- | --- | --- |
|Name of the procedure|Name of the procedure in the database|get_order|
|Session|Name of the session previously started|Conn1|
|Procedure parameters|||

### Close connection
  
Close oracle connection for session
|Parameters|Description|example|
| --- | --- | --- |
|Session|Name of the session previously started that you want to close|Conn1|
