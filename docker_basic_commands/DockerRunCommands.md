Run -tag
	docker run redis:4.0
	This will pull redis of version 4.0 which tagged

Run -STDIN
    -i (interactive mode)
	docker run -i kodekloud/simple-prompt-docker
    -it (sudo terminal)
        docker run -it kodekloud/simple-prompt-docker

Run - PORT mapping
	my application is listing at port 5000 and for user browse at port 80
      docker run -p 80:5000 kodekloud/webapp (80 user: 5000 application/container)
        for example - -p 8000:5000, -p 8001:5000, -p 3306:3306 mysql, -p 8306:3306 mysql

Run - Volume mapping
	Suppose you need to run mysql container and database is stored in location /var/lib/mysql
        as soon as you stop and remove it the data stored in database mysql will destroy
        so to persist data map the directory outside the container of the data host to a directory inside the container
     docker run -v /opt/datadir:/var/lib/mysql  (/opt/datadir-- outside directory)(var/lib/mysql - inside container)

Run Inspect Container --> additional detail about the container 
         docker inspect blissful_container

Container Logs
	docker logs blissful_container