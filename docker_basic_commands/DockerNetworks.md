<h5>Docker Networking<h5>
When we install docker, it creates 3 network automatically i.e. bridge, none, host<br>
Bridge is the default network, container got associated<br>
docker run ubuntu<br>
none - docker run ubuntu --network=none<br>
host - docker run ubuntu --network=host<br>

<ul>
<li>Bridge Network -
	Private internal network, created by docker on the host.All container get attached to it. they get internal ip in range 172.17.0.1<br>
        To access any of these container from the outside world map the port this container to outside port</li>
<li>Host Network
	Another way to access this container is associated to host network. This<br>
	takes out any network isolation btw docker host and docker container. Automatically<br>
    accessible on the same port without port mapping. Also mean wouldn't be able to run multiple container on same ports</li>
<li>None Network
       Container aren't attached to any network and also can't access any to the external network.</li>
</ul>

<h5>User defined Networks</h5>
what if we want to isolate the container within the docker host(bridge)<br>
By default docker bridge creates one internal bridge network, <br>
but we could create own internal network<br>

<pre>
docker network create --drive bridge --subnet 182.18.0.0/16 custom-isolated-network
docker network ls
</pre>

<h5>Inspect Network</h5>
<pre>
<b>docker inspect container_name</b>
- check in Network
</pre>

<h5>Embedded DNS</h5>
	- Container can reach each other by container names.Docker has inbuilt DNS server to resolve <br>
      each other using the container name Build in DNS Server always run on 127.0.0.11 

<h5> How are container isolated within the host</h5> 
Docker uses network namespaces that create separate namespace for each container and uses virtual ethernet pairs to connect container together.
Create a new network named wp-mysql-network using the bridge driver. Allocate subnet 182.18.0.1/24. Configure Gateway 182.18.0.1

<pre>
-------------- Scenario -----------------------

Deploy a mysql database using the mysql:5.6 image and name it mysql-db. Attach it to the newly created network wp-mysql-network
Set the database password to use db_pass123. The environment variable to set is MYSQL_ROOT_PASSWORD.

--------------- Solution ------------------
Run the command: docker network create --driver bridge --subnet 182.18.0.1/24 --gateway 182.18.0.1 wp-mysql-network
Inspect the created network by docker network inspect wp-mysql-network
Run the command: docker run -d -e MYSQL_ROOT_PASSWORD=db_pass123 --name mysql-db --network wp-mysql-network mysql:5.6

</pre>

Deploy a web application named webapp using the kodekloud/simple-webapp-mysql image. Expose the port to 38080 on the host.
The application makes use of two environment variable:
1: DB_Host with the value mysql-db.
2: DB_Password with the value db_pass123.
Make sure to attach it to the newly created network called wp-mysql-network.
Also make sure to link the MySQL and the webapp container.

Run the command: docker run --network=wp-mysql-network -e DB_Host=mysql-db -e DB_Password=db_pass123 -p 38080:8080 --name webapp --link mysql-db:mysql-db -d kodekloud/simple-webapp-mysql