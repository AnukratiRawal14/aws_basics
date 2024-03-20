
<h3>docker run </h3>
run the container of an image.<br>
In example:<br>&emsp;
  <pre><b>docker run nginx</b> </pre>
  this will run an instance of nginx<b></b><br>
  If docker exist it will take it form the docker host if image is not present then it will go to docker hub and pull the image.<br>


<h3>docker ps</h3>
list all running containers<br>
It will give container id, name, created, image id and also shows only running containers<br>
In example:<br>&emsp;
  <pre><b>docker ps</b> </pre>
  

<h3>docker ps -a</h3>
check all the containers checking which containers are running or not<br>
It will give container id, name, created, image id and also shows exited, paused, running<br>
In example:<br> &emsp;
  <pre><b>docker ps -a</b> </pre>
  


<pre>
    <h3>docker stop</h3>
        to stop the container
        In example:
              docker stop silly_sammet
              To stop docker container we need to specify the container name or container id.
    Or else run command
            docker ps (checked the running containers)
            docker stop container_name/id (stop the container)
            docker ps -a (check the status)
</pre>

<pre>
     <h3>docker rm</h3> 
     to remove the stop or get rid of the stopped or exited container or to just free up the space
           In example:
               docker rm silly_sammet
               This should print the docker name once it is removed
     Or else run
           In example:
               docker rm silly_sammet
               docker ps -a (this should not be showing the removed(stopped or exited conatiner)
</pre>

<pre>
    <h3>docker images</h3> 
    to list all the images and their sizes
</pre>

<pre>
   <h3>docker rmi</h3>
        to remove the docker image
        In example:
          docker rmi nginx 
  	Make sure to delete all dependent conatiners to remove image
</pre>

<pre>
    <h3>docker pull</h3>
    to pull the image or to keep image instaed of running or downloading
    In example:
       docker pull nginx
</pre>

Container are run to specific task, once the container task is completed the container will be in exited status
even if container is crashed or stopped then also container will in exited status because it contains only image not anything else inside it

<pre>
  <h3>docker run.... sleep 5 </h3>
    if container is not running any service and to make it run without any service (to keep alive)
	In example: 
        <b>docker run ubuntu sleep 5 </b>
        so now once the docker start the container ubuntu it will then sleep for 5 sec then to get exited
</pre>

<pre>
    <h3>docker exec</h3>
     to execute the commands on running containers
	 In example: 
        <b>docker exec distracted_mcclintock cat /etc/host</b>
	    it will run the command in the given file- etc host file
</pre>

when we run docker run image_name, it runs in the foreground but to make it run in background we run attach and detach command

<pre>
    <h3>docker run -d image_name</h3>
    to run container in detach mode. 
    It means this docker image will run in background and to view run docker ps command
</pre>

<pre>
   <h3>docker attach</h3>
   to attach back to running container( docker attach name or id of docker conatiner)
   In example:
      <b>docker attach ae043</b> (id can be used short in this)
</pre>
