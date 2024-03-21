
<h3>Run -tag</h3>
<pre>
   <b>docker run redis:4.0<?b>
   - This will pull redis of version 4.0 which tagged
</pre>

<h3>Run -STDIN</h3>
<h4>-i (interactive mode)</h4>
<b>For example:</b><br>  &nbsp;
<pre> 
<b>docker run -i kodeKloud/simple-prompt-docker</b><br>
</pre>
<h4>-it (sudo terminal)</h4>
<b>For example:</b><br>  &nbsp;
<pre>
<b>docker run -it kodeKloud/simple-prompt-docker</b>
</pre>

<h3>Run - PORT mapping</h3>
<h5>Application is listing at port 5000 and for user browse at port 80 </h5>
<pre>
<b>docker run -p 80:5000 kodeKloud/webapp </b>(80 user: 5000 application/container)
</pre>

<b>For example:</b>
<pre> 
<b> -p 8000:5000, -p 8001:5000, -p 3306:3306 mysql, -p 8306:3306 mysql</b>
</pre>

<h3> Run - Volume mapping</h3>
<h5> Suppose you need to run mysql container and database is stored in location /var/lib/mysql
as soon as you stop and remove it the data stored in database mysql will destroy
so to persist data map the directory outside the container of the data host to a directory inside the container  </h5>

<b>For example:</b><br>
<pre>
   <b>docker run -v /opt/datadir:/var/lib/mysql </b>
  (/opt/datadir-- outside directory)(var/lib/mysql - inside container)
</pre>

<h3>Run Inspect Container</h3>
<h5>Additional detail about the container </h5>
<b>For example:</b><br>  &nbsp;
<pre>
  <b>docker inspect blissful_container</b>
</pre>

<h3>Container Logs</h3>
<pre>
<b>docker logs blissful_container</b>
</pre>
