<h5> Docker Engine </h5>
When you install docker on linux host actually install 3 different components -
   1. docker cli
   2. docker rest api server
   3. docker daemon
<pre>
Docker Daemon - Is a background process that manages docker objects 
                   images, container, volumes, networks<br>

Docker REST API - Is the API interface that program used to talk to daemon and provide instruction also used own tool<br>

Docker CLI - is command line interface to perform actions such as running, stopping containers, destroying images.
                 It uses Rest API to interact with docker <br>
<?pre>
can access docker cli from other machine - docker-H=remote-docker-engine:2375
 Ex - docker -H=10.123.2.1:2375 run nginx

containerization
namespace- unique process id 
cgroups - cpu and memory are same for docker host and container
to restrict cpu and memory that container can use
docker run --cpus=.5 ubuntu
docker run --memory=100m ubuntu

Docker Storage

File system - let us know how docker stores data on local file system
when we install docker on a system, it creates folder  - /var/lib/docker
    - /var/lib/docker
       -aufs
       -containers
       -image
       -volumes

how exactly docker store its file and what format or image or container

Layered Architecture

each file of instruction of docker file creates a layer 

whenever you update application code, it uses code from cache and quickly rebuild by updating the application

Layer 5: Update Entrypoint with "flask"
Layer 4: Source code
Layer 3: changes in pip packages
Layer 2: Changes in apt package
Layer 1: Base ubuntu layer

All these layer is created when we build image - docker build Dockerfile -t mushad/my-customr-app

When we run  - docker run mumshad/my-cutom-app 
it creates Layer 6: Container layer on top of image layer

Life of layer is as much as container is alive

COPY-ON-WRITE

image layer is read only once created but what if we need to update the code present in image layer so in that case
copy of source code is present in container layer which as read write permission
So, image will be same until unless we rebuild the image form dockerfile
Suppose we don't want container in that case container data will also be deleted

now we want to persist the data
docker volume create data_volume 
 this command will create folder inside /var/lib/docker i.e. volumes/data_volume 

when we run docker container using run command can mount the value inside the docker container
docker run -v data_volume:var/lib/mysql mysql

suppose you directly write command -  docker run -v data_volume2:/var/lib/mysql mysql
this will create create new directory under the volumes and mount the data

this process is called Volume Mounting

Bind Mounting
Now what if we already have the data in another location, want to store data their
docker run -v /data/mysql:/var/lib/mysql mysql

Volume Mounting - Volumes mount the data from volumes directory
Bind Mounting - Bind mounts the volumes from any location in docker host

Also, this is new way to write -- using mount instead of -v
docker run --mount typ=bind,source=/data/mysql,target=/var/lib/mysql mysql

Docker uses storages driver to maintaining layer architecture, copy on write etc
Storage Drivers:
AUFS
ZFS
BTRFS
Device Mapper
Overlay
Overlay2

Selection of storage drivers depend on the OS, for example
AUFS by default uses ubuntu
Docker will automatically choose the drivers based on OS.