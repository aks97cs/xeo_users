[![Build Status](https://travis-ci.org/vmudigal/microservices-sample.svg?branch=master)](https://travis-ci.org/vmudigal/microservices-sample)
[![Docker Repository on Quay](https://quay.io/repository/microservices-sample/api-gateway/status "Docker Repository on Quay")](https://quay.io/repository/microservices-sample/api-gateway)
[![Docker Repository on Quay](https://quay.io/repository/microservices-sample/service-one/status "Docker Repository on Quay")](https://quay.io/repository/microservices-sample/service-one)
[![Docker Repository on Quay](https://quay.io/repository/microservices-sample/service-two/status "Docker Repository on Quay")](https://quay.io/repository/microservices-sample/service-two)
[![Docker Repository on Quay](https://quay.io/repository/microservices-sample/web-application/status "Docker Repository on Quay")](https://quay.io/repository/microservices-sample/web-application)

# User Microservice


` Project Setup`
```
Prerequisite
```
Install docker and docker-compose in your OS
</br> 
please refere the <a href="https://docs.docker.com/engine/install/ubuntu/">Link</a>

```
 Up/Running with service
 ```
 <ul>
    <li> Go to project root directory </li>
    <li> To start project: Run <b> docker-compose up -d </b> </li>
    -   now visit on http://127.0.0.1:8000 </br>
    - Note: Make sure port 8000 and 5432 is open in your machine
    <li> To stop your project: Run <b>docker-compose down</b> </li>
 </ul>

 ```
 API Endpoint
 ```
 1. 127.0.0.1:8000/user => GET
 2. 127.0.0.1:8000/user/ => POST
 3. 127.0.0.1:8000/user/user_id => PUT
 4. 127.0.0.1:8000/user/user_id => DELETE

` API Specification` <a href="#comming-soon">DOC </a>
```
Troubleshoot
```
In case of any issue run command with sudo or take reference of log
</br>
To view container log
</br>
Run: docker logs ##container-name##
</br>
Or 
</br>
RUN: docker-compose down and then docker-compose up
now see the log in terminal

```buildoutcfg
Building fixture from existing DB
- docker-compose run xeo_web ./manage.py dumpdata app_name.model_name --indent 4 > service/fixture/users.json

Loading fixture in db
- docker-compose run xeo_web ./manage.py loaddata service/fixtures/users.json --app app.model_name

```

#### Command to run test
` docker-compose run xeo_web ./manage.py test
`

</br>
Anuj Kumar Singh</br>
anuj.dev@hotmail.com</br>
Happy to help you !!