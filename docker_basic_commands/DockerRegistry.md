<h4>Docker Registry</h4>

Docker registry is where docker images are stored 
<pre>
docker run nginx -> image name /repository name it also uses nginx/nginx
if you create you own respository in that case we write
    image: user or account /image or repo
where are the images are pulled or stored assumed that it is in dockerhub

gcr.io/kubernetes-test-images/dnsutile  ---> image holder/registry
</pre>

<h5>Private Registry</h5>
    Only can access via credentials
<pre>
    docker login private-registry.io
       Username: registry-user
       Password: *******
    Run Command - > docker run private-registry.io/apps/internal-app

Deploy Private Registry
 docker run -d -p 5000:5000 --name registry registry:2  -->custom registry running on port 5000 on this dockerhost
 docker image tag my-image localhost:5000/my-image  --> use image tag to tag the image for private registry url in this
 docker push localhost:5000/my-image -->  now can push with docker registry detail
 docker pull localhost:5000/my-image --> can pull form their
 docker pull 192.168.56.100:50000/my-image --> if access form other laptop
</pre>


Let practice deploying a registry server on our own.
<pre>
--------- scenario -----------
Run a registry server with name equals to my-registry using registry:2 image with host port set to 5000, and restart policy set to always.
Note: Registry server is exposed on port 5000 in the image.
Here we are hosting our own registry using the open source Docker Registry.
--------- Solution -----------
docker run -p 5000:5000 --name my-registry --restart=always registry:2
</pre>

<pre>
Now, its time to push some images to our registry server. Let's push two images for now .i.e. nginx:latest and httpd:latest.
Note: Don't forget to pull them first.
To check the list of images pushed , use curl -X GET localhost:5000/v2/_catalog

<b>Run:docker pull nginx:latest </b>

then docker image tag nginx:latest localhost:5000/nginx:latest 
and finally push it using docker push localhost:5000/nginx:latest.
We will use the same steps for the second image docker pull httpd:latest and 
then docker image tag httpd:latest localhost:5000/httpd:latest and finally push it 
using docker push localhost:5000/httpd:latest
</pre>

