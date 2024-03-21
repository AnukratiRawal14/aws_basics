<h5>When we create image, and we don't find image on docker hub. In this case we create our own custom image</h5>
<h5>For example:</h5>
<h5>In this case, we need to containerize an app i.e. simple web app build flask</h5>
<h5>To deploy application manually, steps to taken care of:</h5>
<pre>
       <h5>----- Create my own image for single web application ------</h5>
       <li> Operation system - (ex- ubuntu)</li>
       <li> Update apt repo - (update source repo)</li>
       <li> Install dependencies using apt</li>
       <li> Install python dependencies using pip</li>
       <li> Copy source code ro /opt folder</li>
       <li> Run web server use in flask command</li>
</pre>

<h5>Need to create docker file using this:</h5>
<pre>
    <b>Dockerfile.txt</b>
    FROM Ubuntu
    RUN apt-get update && apt-get -y install python
    RUN pip install flask flask-mysql
    COPY ./opt/source-code
    ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
</pre>

<h5>Once done build your image using build command</h5>
<pre>
    <b>docker build . -f Dockerfile -t mmumshad/my-custom-app</b>
    - this will create image locally on your system
    - to make it available on public repo, run push command
    <b> docker push image_name</b> 
</pre>

<b>Docker Layered Architecture</b>
<h5> Docker build images in layered architecture, each line of instruction creates new line of layer </h5>
<pre> <b> docker build. -f Dockerfile -t mumshad/my-custom-app </b></pre>
<h5> Layers:</h5>
<pre>
    Layer 1: Base Ubuntu Layer 120mb
    Layer 2: Changes in apt packages 300 mb
    Layer 3: Changes in pip packages 6.3 mb
    Layer 4: Source Code 229 b
    Layer 5: Update Entrypoint with "flask" command 0 b
</pre>

<h3> Lab - DockerImages(commands)</h3>
<pre>
    cd /root/webapp-color
    cat /etc/*release* -  to check the os 
    ls -li/a
    nano to edit the file
    add tag using ':'
</pre>

<h3>Docker environment variables</h3>
<pre>
   <h6> ----- Scenario ------ </h6>
    color = os.environ.get('APP_COLOR')
    export APP_COLOR=blue; python app.py 
    once this is docker image
    docker run -e APP_COLOR=blue
    docker inspect and find environment variables in config section
   <h6> ----- Solution -----</h6>
   <b>docker run -p 38282:8080 --name blue-app -e APP_COLOR=blue kodeKloud/simple-webapp</b>
</pre>

<h6>Docker Command, Arguments and Entrypoint</h6>
<h5> In docker file, CMD["nginx"] - define default command <br>
we can run docker run ubuntu sleep 5 , but  we want it to be permanent in that case </h5>
<pre>
	dockerfile- ubuntu-sleeper
	FROM Ubuntu
	CMD sleep 5 or CMD["sleep","5"]
	Run command -> <b> run docker run ubuntu-sleeper </b>
</pre>

<h5> 
	Consider if we want to run for 10 instead of 5 so write cmd - docker run ubuntu-sleeper sleep 10
	but this is not a good idea, now we only want to pass the no of sec, in that case we use Entrypoint
</h5>
<pre>
	FROM Ubuntu
	ENTRYPOINT["sleep"]
	Run command -><b> docker run ubuntu-sleeper 10 </b>
</pre>

<h5>In case of cmd if we pass sleep 10 in command, it will get replaced 5 by 10 and in entrypoint it will get append by 10 <br>
so if you have to pass default value and then append in that case </h5>
<pre>
	FROM Ubuntu
	ENTRYPOINT["sleep"]
	CMD["5"]
</pre>

<h5> Now if you didn't pass then it will sleep for 5 sec </h5>
<pre>
    <b> docker run ubuntu-sleeper 10</b>
     - In this case it will override 5 sec with 10 sec
</pre>

<h5> In case we need to modify entrypoint at run time in that case</h5>
<pre>
     <b>docker run --entrypoint sleep2.0 ubuntu-sleeper 10 </b>
</pre>	
