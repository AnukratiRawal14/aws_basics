
<h3>docker run </h3>
run the container of an image<br>
<b>In example:</b><br>  &nbsp;
  <pre>
  <b>docker run nginx</b><br>
  - this will run an instance of nginx<b></b><br> 
  - If docker exist it will take it form the docker host if image is not present then it will go to docker hub and pull the image.
  </pre>
  
<h3>docker ps</h3>
list all running containers<br>
<b>In example:</b><br>  &nbsp;
  <pre>
  <b>docker ps</b> <br>
  - It will give container id, name, created, image id and also shows only running containers
  </pre>
  
<h3>docker ps -a</h3>
check all the containers checking which containers are running or not<br>
<b>In example:</b><br>  &nbsp;
  <pre>
  <b>docker ps -a</b> <br> 
  - It will give container id, name, created, image id and also shows exited, paused, running
  </pre>

<h3>docker stop</h3>
to stop the container
<b>In example:</b><br>  &nbsp;
   <pre>
    <b>docker stop silly_sammet</b><br>
    - To stop docker container we need to specify the container name or container id.</pre>
Or else run command<br>   &nbsp;
  <pre>
    <b>docker ps</b> (checked the running containers)
    <b>docker stop container_name/id</b> (stop the container)
    <b>docker ps -a</b> (check the status)
</pre>

<h3>docker rm</h3> 
to remove the stop or get rid of the stopped or exited container or to just free up the space
<b>In example:</b><br>  &nbsp;
<pre>
  <b>docker rm silly_sammet</b>
  - This should print the docker name once it is removed
</pre>
Or else run
<b>In example:</b><br>  &nbsp;
<pre>
   <b> docker rm silly_sammet</b> 
   <b> docker ps -a </b> (this should not be showing the removed(stopped or exited conatiner)
</pre>


<h3>docker images</h3> 
to list all the images and their sizes
<b>In example:</b><br>  &nbsp;
<pre>
docker images
</pre>

<h3>docker rmi</h3>
to remove the docker image
<b>In example:</b><br>  &nbsp;
<pre>
  <b>docker rmi nginx </b>
  - Make sure to delete all dependent conatiners to remove image
</pre>


<h3>docker pull</h3>
to pull the image or to keep image instaed of running or downloading
<b>In example:</b><br>  &nbsp;
<pre><b>docker pull nginx</b></pre>


Container are run to specific task, once the container task is completed the container will be in exited status
even if container is crashed or stopped then also container will in exited status because it contains only image not anything else inside it


<h3>docker run.... sleep 5 </h3>
If container is not running any service and to make it run without any service (to keep alive)
<b>In example:</b><br>  &nbsp;
<pre>
   <b>docker run ubuntu sleep 5 </b>
    - Once the docker start the container ubuntu, it will then sleep for 5 sec then to get exited
</pre>

<h3>docker exec</h3>
to execute the commands on running containers
<b>In example:</b><br>  &nbsp;
<pre>
    <b>docker exec distracted_mcclintock cat /etc/host</b>
    - It will run the command in the given file- etc host file
</pre>

<h3>Run image in background</h3>
when we run docker run image_name, it runs in the foreground but to make it run in background we run attach and detach command
<pre>
    <b>docker run -d image_name</b>
    - to run container in detach mode. 
    - It means this docker image will run in background and to view run docker ps command
</pre>

<h3>docker attach</h3>
to attach back to running container( docker attach name or id of docker conatiner)
<b>In example:</b><br>  &nbsp;
<pre>
    <b>docker attach ae043</b> 
    - Id can be used short in this
</pre>
