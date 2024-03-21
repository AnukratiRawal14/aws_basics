<h5> Docker Compose </h5>
<h5> docker run vs docker compose </h5>
<h5> ---- docker run ---- </h5>
<pre>
docker run
docker run mmushad/simple-webapp
docker run mongodb
docker run redis:alpine
docker run ansible
</pre>
<h5> ----- docker compose ----- </h5>
<h5> docker-compose.yaml</h5>
<pre>
service:
    web:
        image:"mumshad/simple-webapp
        database:
            image:"mongodb"
        messaging:
            image: "redis:alpine"
        orchestration:
            image: "ansible"
	
Run command --> docker-compose up
</pre>

<h5> Sample Application Demo </h5>
<pre>
voting app(python) -->
DB(redis) votes stored in redis in-memory --> <br>
worker(.net) takes votes and updates in postgress sql --> <br>
db(psotgress sql) updates the data --><br>
result-app(nodeJS) showes the result
</pre>

<h5>Running all the containers</h5>
<pre>
docker run -d --name=redis redis
docker run -d --name=db db
docker run -d --name=vote -p 5000:80 voting-app
docker run -d --name=result -p 5001:80 result-app
docker run -d --name=worker worker
---- we have successfully run all the container but haven't linked them ----
</pre>

<h5>Linking all the containers</h5>
<b>docker run --links</b>
<pre>
docker run -d --name=redis redis
docker run -d --name=db db
docker run -d --name=vote -p 5000:80 --link redis:redis voting-app  (create the entry in /etc/host file like 172.17.0.2(internal ip of redis conatiner redis 0000)
docker run -d --name=result -p 5001:80 --link db:db result-app
docker run -d --name=worker --link redis:redis --link db:db worker
(depricated)
</pre>

<h5>docker-compose.yml</h5>
<pre>
redis:
    image:redis
db:
    image: postgress:9.4
vote:
    image: voting-app
    ports:
      - 5000:80
    links:
      - redis(=redis:redis)
result:
   image: result-app
   ports:
      - 5001:80
   links:
      - db(=db:db)
worker:
    image: worker
    links:
      - redis (=redi:redis)
      - db  (=db:db)

run --> docker-compose up
</pre>

<h5>Docker Compose Build</h5>
<pre>
     redis:
        image:redis
     db:
        image: postgress:9.4
     vote:
        build: ./vote  (there is dockerfile present in example-voting-app/vote/)
        ports:
           - 5000:80
        links:
          - redis(=redis:redis)
    result:
        build: ./result
        ports:
          - 5001:80
        links:
          - db(=db:db)
    worker:
        build: ./worker
        links:
          - redis (=redi:redis)
          - db  (=db:db)
</pre>

<h5>Docker Versions</h5>
<pre>
    docker version has lot of limitation
    docker version 
        version: 2
        service:
             redis:
                image:redis
             db:
                image:postgress:9.4
             vote:
                image: voting-app
                ports:
                   - 5001:80
                depens_on: 
                   - redis<br>
               
In docker version 2, docker compose automatically creates dedicated bridge network and then
attached all container can communicate to service name to new network no need to use links also has depend on

version: 3
service
    redis:
	image:redis
     db:
	image:postgress:9.4
     vote:
	image: voting-app
	ports:
	   - 5001:80
</pre>

<h5>Docker Compose</h5>
<pre>
	need to seprate user generated traffic to backend network traffic
        version:2
        service: 
             redis:
                 image: redis
                 networks:
                     - back-end
             db:
                image:db
                networks:
                   - back-end
            vote:
                image:voting-app
                networks:
                   - front-end
                   - back-end
            result:
                image: result
                networks:
                   - front-end
                   - back-end
            worker:
                image: worker
                networks:
                   - back-end
      networks:
          fornt-end:
          back-end:
</pre>
