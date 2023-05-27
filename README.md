SQLServer to BigQuery

Configuración del proxy

Para efectos de ejecución local, es posible instalar el controlador de SQLServer que permite la conexión mediante un Proxy, este paso es mandatorio para establecer una conexión segura. En una siguiente fase, este
requerimiento será añadido a una imagen Dockerizada.

Orquestación mediante Airflow.

Conexión y escritura en BigQuery

Instalar OBDC en Linux
Esto se va a un Docerfile o a un .sh

----------------------------------------------------------
sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

#Download appropriate package for the OS version
#Choose only ONE of the following, corresponding to your OS version

#Debian 9
curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list

#Debian 10
curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

#Debian 11
curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

exit
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
# optional: for unixODBC development headers
sudo apt-get install -y unixodbc-dev
# optional: kerberos library for debian-slim distributions
sudo apt-get install -y libgssapi-krb5-2

-------------------------------------------------------------------------------


Instalar cloud-sql-proxy

curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.2.0/cloud-sql-proxy.linux.amd64

Que sea ejecutable

chmod +x cloud-sql-proxy

Iniciar el proxy y en caso de ser necesario dar una service account

./cloud-sql-proxy DATABASENAMECONNECTION

Luego de inicializar el comando anterior, ejecutar las consultar apuntando a localhost:1433

https://cloud.google.com/sql/docs/sqlserver/connect-auth-proxy?hl=es-419#tcp-sockets


