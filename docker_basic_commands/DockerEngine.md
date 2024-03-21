<h5> Docker Engine </h5>

When you install docker on linux host actually install 3 different components - <br>
   1. Docker CLI<br>
   2. Docker Rest API Server<br>
   3. Docker Daemon<br>
   <br>

   <li>Docker Daemon - Is a background process that manages docker objects images, container, volumes, networks</li>
   <li>Docker REST API - Is the API interface that program used to talk to daemon and provide instruction 
   also used own tool</li>
   <li>Docker CLI - is command line interface to perform actions such as running, stopping containers, destroying images.
   It uses Rest API to interact with docker </li><br>

<pre>
   <b>Can access docker cli from other machine </b>
   <b>docker-H=remote-docker-engine:2375</b>
   <b>Ex - docker -H=10.123.2.1:2375 run nginx </b>
</pre>

<h5>Containerization</h5>
<pre>
namespace- unique process id 
cgroups - cpu and memory are same for docker host and container
to restrict cpu and memory that container can use
docker run --cpus=.5 ubuntu
docker run --memory=100m ubuntu
</pre>

<h5>Docker Storage</h5>

<b>File system -</b>
<pre>
let us know how docker stores data on local file system
when we install docker on a system, it creates folder  - /var/lib/docker
    - /var/lib/docker
       -aufs
       -containers
       -image
       -volumes
</pre>

<h5>Layered Architecture</h5>
<pre>
Each file of instruction of docker file creates a layer whenever you update application code,<br>
it uses code from cache and quickly rebuild by updating the application<br>

Layer 5: Update Entrypoint with "flask"<br>
Layer 4: Source code<br>
Layer 3: changes in pip packages<br>
Layer 2: Changes in apt package<br>
Layer 1: Base ubuntu layer<br>

All these layer is created when we build image - docker build Dockerfile -t mushad/my-customr-app
When we run  - <b>docker run mumshad/my-cutom-app </b> .It creates Layer 6: Container layer on top of image layer
Life of layer is as much as container is alive
</pre>

<h5>COPY-ON-WRITE</h5>
<pre>
Image layer is read only once created but what if we need to update the code present in image layer so in that case
copy of source code is present in container layer which as read write permissionSo, image will be same until unless 
we rebuild the image form dockerfile. Suppose we don't want container in that case container data will also be deleted
</pre>
<h5> To persist the data</h5>
<pre>
   <b>docker volume create data_volume </b>
   - this command will create folder inside /var/lib/docker i.e. volumes/data_volume 
</pre>

<h5>when we run docker container using run command can mount the value inside the docker container</h5>
<pre><b>docker run -v data_volume:var/lib/mysql mysql</b></pre>

<h5>Volume Mounting </h5>
Suppose you directly write command -<b> docker run -v data_volume2:/var/lib/mysql mysql</b> <br>
this will create create new directory under the volumes and mount the data this process is called Volume Mounting <br>

<h5>Bind Mounting</h5>
Now what if we already have the data in another location, want to store data their<br>
<pre><b>docker run -v /data/mysql:/var/lib/mysql mysql</b></pre>

<h5> Volume Mounting vs Bind Mounting- </h5>
Volume Mounting - Volumes mount the data from volumes directory
Bind Mounting - Bind mounts the volumes from any location in docker host

Also, this is new way to write -- using mount instead of -v
<pre><b>docker run --mount typ=bind,source=/data/mysql,target=/var/lib/mysql mysql</b></pre>

<h5>Docker Storages</h5>
Docker uses storages driver to maintaining layer architecture, copy on write etc<br>

<ul>
<li>Storage Drivers:</li>
<li>AUFS</li>
<li>ZFS</li>
<li>BTRFS</li>
<li>Device Mapper</li>
<li>Overlay</li>
<li>Overlay2</li>
</ul>
Selection of storage drivers depend on the OS, for example
AUFS by default uses ubuntu
Docker will automatically choose the drivers based on OS.
