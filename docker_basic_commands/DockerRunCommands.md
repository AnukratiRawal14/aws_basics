
<h3>Run -tag</h3>
<pre>
   <b>docker run redis:4.0<?b>
   - This will pull redis of version 4.0 which tagged
</pre>

<h3>Run -STDIN</h3>
<pre>
    <b>-i</b> (interactive mode)
    In example: <br>
	docker run -i kodeKloud/simple-prompt-docker<br>
    <b>-it </b>(sudo terminal)
    In example: <br>
    docker run -it kodeKloud/simple-prompt-docker
</pre>

<h3>Run - PORT mapping</h3>
my application is listing at port 5000 and for user browse at port 80
<pre>
   <b>docker run -p 80:5000 kodeKloud/webapp </b>(80 user: 5000 application/container)
    For example: <br>
     -p 8000:5000, -p 8001:5000, -p 3306:3306 mysql, -p 8306:3306 mysql
</pre>

<h3> Run - Volume mapping</h3>
Suppose you need to run mysql container and database is stored in location /var/lib/mysql<br>
as soon as you stop and remove it the data stored in database mysql will destroy<br>
so to persist data map the directory outside the container of the data host to a directory inside the container<br>
For example: <br>
<pre>
   docker run -v /opt/datadir:/var/lib/mysql 
  (/opt/datadir-- outside directory)(var/lib/mysql - inside container)
</pre>

<h3>Run Inspect Container</h3>
Additional detail about the container 
For example: <br>
<pre>
  docker inspect blissful_container
</pre>

<h3>Container Logs</h3>
<pre>
	docker logs blissful_container
</pre>