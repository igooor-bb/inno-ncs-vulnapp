# inno-ncs-vulnapp
Vulnerable application for Network and Cybersecurity course at Innopolis University

# Launch

It consists of three services: an application, a database and a reverse proxy (so that the user can only ping one port). Each of these is deployed in a separate container using `docker-compose`.

Therefore, it is sufficient to clone the repository to run the application:

```
git clone https://github.com/igooor-bb/inno-ncs-vulnapp.git
```

And run docker-compose to start the services in the ensemble:

```
docker-compose up
```
